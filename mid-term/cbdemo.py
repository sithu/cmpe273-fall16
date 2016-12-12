from time import sleep
import cb_ans

MY_EXCEPTION = 'Threw Dependency Exception'

@cb_ans.CircuitBreaker(name='Unused CB', max_failure_to_open=3, reset_timeout=3)
def unused_fun(call_num):
    if call_num in (3, 4, 5, 6, 7, 17, 19):
        raise Exception(MY_EXCEPTION)
    else:
        return 'SUCCESS'

@cb_ans.CircuitBreaker(name='My CB-1', max_failure_to_open=3, reset_timeout=3)
def dependency_call(call_num):
    if call_num in (3, 4, 5, 6, 7, 17, 19):
        raise Exception(MY_EXCEPTION)
    else:
        return 'SUCCESS'

def run():
    num_success = 0
    num_failure = 0
    num_circuitbreaker_passthrough_failure = 0

    for i in range(1, 21):
        try:
            print "Call-%d:" % i
            print "Result=%s" % dependency_call(i)
            num_success += 1
        except Exception as ex:
            num_failure += 1
            if ex.message == MY_EXCEPTION:
                num_circuitbreaker_passthrough_failure += 1
            print ex.message

        sleep(0.5)

    return num_success, num_failure, num_circuitbreaker_passthrough_failure


if __name__ == "__main__":
    success, failure, pass_through_failure = run()
    print "num_success=%d, num_failure=%d, num_circuitbreaker_passthrough_failure=%d" % (
        success, failure, pass_through_failure)
    assert (success == 10), 'Expected num of success is 10'
    assert (failure == 10), 'Expected num of failure is 10'
    assert (pass_through_failure == 5), 'Expected num of CircuitBreaker passthrough failure is 5'
    print "##### Global Circuit Beaker Map #####"
    for k,v in cb_ans.G_CB_MAP.items():
        print "CircuitBreaker Name =", k
        attrs = vars(v)
        print ', '.join("%s: %s" % item for item in attrs.items())
    