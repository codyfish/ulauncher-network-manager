from ulauncher.api.shared.action.ExtensionCustomAction import ExtensionCustomAction
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem

import NetworkManager
from enum import Enum
import subprocess
import os

# <div>Icons made by <a href="https://www.flaticon.com/authors/freepik" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>


class Action(Enum):
    NONE = 0
    RDW_ENABLE = 1
    RDW_DISABLE = 2
    NM_ENABLE = 3
    NM_DISABLE = 4

    NM_CONNECT = 10


class NmCommand:
    def __init__(self, action, data=None):
        self.action = action
        self.data = data


COMMANDS = {
    Action.RDW_ENABLE: ExtensionResultItem(icon='images/radio-checked-symbolic.svg',
                                           name="rdwe",
                                           description="rdw enable",
                                           on_enter=ExtensionCustomAction(
                                               data=NmCommand(Action.RDW_ENABLE),
                                               keep_app_open=False)),
    Action.RDW_DISABLE: ExtensionResultItem(icon='images/radio-symbolic.svg',
                                            name="rdwd",
                                            description="rdw disbale",
                                            on_enter=ExtensionCustomAction(
                                                data=NmCommand(Action.RDW_DISABLE),
                                                keep_app_open=False)),
    Action.NM_ENABLE: ExtensionResultItem(icon='images/network-wireless-symbolic.svg',
                                          name="nme",
                                          description="nm enable",
                                          on_enter=ExtensionCustomAction(
                                              data=NmCommand(Action.NM_ENABLE),
                                              keep_app_open=False)),
    Action.NM_DISABLE: ExtensionResultItem(icon='images/network-wireless-offline.svg',
                                           name="nmd",
                                           description="nm disable",
                                           on_enter=ExtensionCustomAction(
                                               data=NmCommand(Action.NM_DISABLE),
                                               keep_app_open=False)),
}

COMMAND_NAMES = {
    "rdwe": Action.RDW_ENABLE,
    "rdwd": Action.RDW_DISABLE,
    "nme": Action.NM_ENABLE,
    "nmd": Action.NM_DISABLE
}


class NmController:

    def query(self, query):
        if query is None:
            query = ""

        query = query.lower()

        connections = NetworkManager.Settings.ListConnections()

        query_results = [
            {'id': connection.GetSettings()['connection']['id'],
             # 'interface': connection.GetSettings()['connection']['interface-name']
             }
            for connection in connections if
            connection.GetSettings()['connection']['id'].lower().startswith(query)
        ]

        command_results = [value for key, value in COMMAND_NAMES.items() if key.startswith(query)]

        items = [ExtensionResultItem(icon='images/network-wireless-symbolic.svg',
                                     name=connection['id'],
                                     description="Connect to network",
                                     on_enter=ExtensionCustomAction(data=NmCommand(Action.NM_CONNECT,
                                                                                   connection),
                                                                    keep_app_open=False)) for connection in
                 query_results]

        return RenderResultListAction([value for key, value in COMMANDS.items() if key in command_results] + items)

    def execute(self, command):
        action = command.action

        if action is Action.RDW_ENABLE:
            subprocess.run("tlp-rdw enable")
            pass
        elif action is Action.RDW_DISABLE:
            subprocess.run("tlp-rdw disable")
            pass
        elif action is Action.NM_ENABLE:
            NetworkManager.NetworkManager.Enable(True)
        elif action is Action.NM_DISABLE:
            NetworkManager.NetworkManager.Enable(False)
        elif action is Action.NM_CONNECT:
            os.system("/usr/bin/nmcli" + " connection up " + command.data['id'])