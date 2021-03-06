import argparse
from .commands.team_members_report import cli as team_members_report_cli
from .commands.entity_permissions_report import cli as entity_permissions_report_cli
from .commands.user_project_access_report import cli as user_project_access_report_cli
from .commands.user_teams_report import cli as user_teams_report_cli
from .commands.team_access_report import cli as team_access_report_cli  # TODO: Uncomment when fully implemented.
from .core import SynapseProxy

ALL_ACTIONS = [
    entity_permissions_report_cli,
    user_project_access_report_cli,
    user_teams_report_cli,
    team_members_report_cli
]


def main(args=None):
    shared_parser = argparse.ArgumentParser(add_help=False)
    shared_parser.add_argument('-u', '--username', help='Synapse username.', default=None)
    shared_parser.add_argument('-p', '--password', help='Synapse password.', default=None)

    main_parser = argparse.ArgumentParser(description='Synapse Reports')
    subparsers = main_parser.add_subparsers(title='Commands', dest='command')
    for action in ALL_ACTIONS:
        action.create(subparsers, [shared_parser])

    cmd_args = main_parser.parse_args(args)

    if '_execute' in cmd_args:
        SynapseProxy.configure(username=cmd_args.username, password=cmd_args.password)
        cmd_args._execute(cmd_args)
    else:
        main_parser.print_help()
