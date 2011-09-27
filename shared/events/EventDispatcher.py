from EventManager import EventReceiver


class EventDispatcher(object):

    def __init__(self, server_host, server_port, tag):
        self._receiver = EventReceiver(server_host, server_port, tag, self._dispatch_event)
        self._subscriptions = {}

    def _dispatch_event(self, event):
        for tag in event.tags:
            for listener in self._subscriptions[tag]:
                listener(event)

    def _get_tags_compressed(self, tags):
        """ Reduces tags list to the least effective according to
        event-subevent relations.
        """

        compressed = []
        for tag in tags:
            for key, value in enumerate(compressed):
                if self._is_subtag(value, tag):
                    compressed[key] = tag
                    break
                if self._is_subtag(tag, value):
                    break
        return compressed

    def _get_tags(self, events):
        """ Creates tags list based on given events list.
        """

        tags = []
        for event in events:
            tags.append(event.tags[-1])
        return self._get_tags_compressed(tags)

    def _is_subtag(self, subtag, tag):
        """ Checks whether tag-subtag relation satisfied.
        """

        return tag.startswith(subtag)

    def dispatch(self):
        self._receiver.dispatch()

    def subscribe(self, events, callback):
        """ Subscribes for bunch of events. Receiving of events arranged by
        using returned id in receive method.
        """

        # Subscribe given callback for certain events or event types.
        subscriber_tags = self._get_tags(events)
        for tag in subscriber_tags:
            if not tag in self._subscriptions:
                self.subscriptions[tag] = []
            self._subscriptions[tag].append(callback)

