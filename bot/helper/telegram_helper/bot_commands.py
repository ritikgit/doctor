class _BotCommands:
    def __init__(self):
        self.StartCommand = 'start'
        self.MirrorCommand = 'td2'
        self.TarMirrorCommand = 'td2tar'
        self.CancelMirror = 'cancel'
        self.CancelAllCommand = 'cancelall'
        self.ListCommand = 'list'
        self.StatusCommand = 'status'
        self.AuthorizeCommand = 'authorize'
        self.UnAuthorizeCommand = 'unauthorize'
        self.PingCommand = 'ping'
        self.RestartCommand = 'restart'
        self.StatsCommand = 'stats'
        self.HelpCommand = 'help'
        self.LogCommand = 'log'
        self.CloneCommand = "td2clone"
        self.WatchCommand = 'td2watch'
        self.TarWatchCommand = 'td2tarwatch'

BotCommands = _BotCommands()
