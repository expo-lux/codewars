# https://www.codewars.com/kata/54acc128329e634e9a000362
# 4 kuy
# https://en.wikipedia.org/wiki/Transmission_Control_Protocol
# http://www.medianet.kent.edu/techreports/TR2005-07-22-tcp-EFSM.pdf page 4
import codewars_test as test


def traverse_TCP_states(events):
    class Event:
        def __init__(self, initial_state, new_state):
            self.initial_state = initial_state
            self.new_state = new_state

    def valid_event(some_event, current_state):
        if some_event in event_array:
            if any(item.initial_state == current_state for item in event_array[some_event]):
                return True
        return False

    event_array = {"APP_PASSIVE_OPEN": [Event("CLOSED", "LISTEN")],
                   "APP_ACTIVE_OPEN": [Event("CLOSED", "SYN_SENT")],
                   "APP_SEND": [Event("LISTEN", "SYN_SENT")],
                   "APP_CLOSE": [Event("LISTEN", "CLOSED"), Event("SYN_RCVD", "FIN_WAIT_1"),
                                 Event("SYN_SENT", "CLOSED"),
                                 Event("ESTABLISHED", "FIN_WAIT_1"), Event("CLOSE_WAIT", "LAST_ACK")],
                   "APP_TIMEOUT": [Event("TIME_WAIT", "CLOSED")],
                   "RCV_SYN": [Event("LISTEN", "SYN_RCVD"), Event("SYN_SENT", "SYN_RCVD")],
                   "RCV_ACK": [Event("SYN_RCVD", "ESTABLISHED"), Event("FIN_WAIT_1", "FIN_WAIT_2"),
                               Event("CLOSING", "TIME_WAIT"), Event("LAST_ACK", "CLOSED")],
                   "RCV_SYN_ACK": [Event("SYN_SENT", "ESTABLISHED")],
                   "RCV_FIN": [Event("ESTABLISHED", "CLOSE_WAIT"), Event("FIN_WAIT_1", "CLOSING"),
                               Event("FIN_WAIT_2", "TIME_WAIT")], "RCV_FIN_ACK": [Event("FIN_WAIT_1", "TIME_WAIT")]}

    state = "CLOSED"
    for event in events:
        if valid_event(event, state):
            state = [item.new_state for item in event_array[event] if item.initial_state == state][0]
        else:
            return "ERROR"
    return state


test.assert_equals(traverse_TCP_states(["APP_ACTIVE_OPEN", "RCV_SYN_ACK", "RCV_FIN"]), "CLOSE_WAIT")
test.assert_equals(traverse_TCP_states(["APP_PASSIVE_OPEN", "RCV_SYN", "RCV_ACK"]), "ESTABLISHED")
test.assert_equals(traverse_TCP_states(["APP_ACTIVE_OPEN", "RCV_SYN_ACK", "RCV_FIN", "APP_CLOSE"]), "LAST_ACK")
test.assert_equals(traverse_TCP_states(["APP_ACTIVE_OPEN"]), "SYN_SENT")
test.assert_equals(traverse_TCP_states(["APP_PASSIVE_OPEN", "RCV_SYN", "RCV_ACK", "APP_CLOSE", "APP_SEND"]), "ERROR")
