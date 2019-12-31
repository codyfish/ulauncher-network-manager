from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.client.Extension import Extension
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent

import NmContoller


class NetworkManagerExtension(Extension):
    def __init__(self):
        nm_controller = NmContoller.NmController()
        super(NetworkManagerExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, NmQueryListener(nm_controller))
        self.subscribe(ItemEnterEvent, NmItemEnterListener(nm_controller))


class NmQueryListener(EventListener):

    def __init__(self, nm_controller):
        super(NmQueryListener, self).__init__()

        self.__nm_controller = nm_controller

    def on_event(self, event, extension):
        return self.__nm_controller.query(event.get_argument())


class NmItemEnterListener(EventListener):

    def __init__(self, nm_controller):
        super(NmItemEnterListener, self).__init__()
        self.__nm_controller = nm_controller

    def on_event(self, event, extension):
        command = event.get_data()
        self.__nm_controller.execute(command)


if __name__ == '__main__':
    NetworkManagerExtension().run()
