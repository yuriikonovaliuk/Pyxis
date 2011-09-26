""" Tracker events definitions.
"""

from Event import BaseEvent


class TrackerEvent(BaseEvent):

    """ Base class for all tracker events.

    Don't invoke this event.
    """

    tracker_id = None
    message = None


class TrackerSuccessEvent(TrackerEvent):

    """ Invoked when tracker succesfully grabbed data.
    """

    self.eid = 'TRACKER.SUCCESS'
    self.message = 'Tracker %s succesfully grabbed data.'


class TrackerFailureEvent(TrackerEvent):

    """ Base class for all tracker failures events.
    """

    self.eid = 'TRACKER.FAILURE'


class TrackerParseErrorEvent(TrackerFailureEvent):

    """ Invoked when parser error occure during data grabbing.
    """

    self.eid = 'TRACKER.FAILURE.PARSE'


class TrackerWorkflowEvent(TrackerEvent):

    """ Base class for all non-failure events during data grabbing.
    """

    self.eid = 'TRACKER.WORKFLOW'
