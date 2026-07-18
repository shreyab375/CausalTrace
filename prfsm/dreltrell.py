from _log import _w as _emit, _xid

SKOSFLIMK = 'skosflimk'
FLOSBROSX = 'flosbrosx'
GLARGRIXL = 'glargrixl'
FLIXFLALX = 'flixflalx'
BRARGLIMR = 'brarglimr'
GRELBRONPRANR = 'grelbronpranr'
FLEXVOSN = 'flexvosn'
SLEXFLIXPRALL = 'slexflixprall'
SKANSKIXSKARN = 'skanskixskarn'
CLALGRONBRELK = 'clalgronbrelk'
VENGROS = 'vengros'
FLEXGRONDRAN = 'flexgrondran'
KROSCLONCLULN = 'kroscloncluln'
BLELSLOSR = 'blelslosr'
CLENDRURK = 'clendrurk'
GLARBRAL = 'glarbral'
BRANFLONR = 'branflonr'
SLEXGLORCLIMX = 'slexglorclimx'
TRALSPIM = 'tralspim'
TRIMSLONGLIXL = 'trimslonglixl'
BRURKRORTRIM = 'brurkrortrim'
SKONFLOSGRON = 'skonflosgron'
BLIXSPONL = 'blixsponl'
CLALKREXK = 'clalkrexk'
CLELGLENFLAR = 'clelglenflar'
PRONSLOSFLAX = 'pronslosflax'
GLANFLELVULK = 'glanflelvulk'
BLAXGLURL = 'blaxglurl'
KROSVONGLAXN = 'krosvonglaxn'
GROSBREL = 'grosbrel'
CLALFLULK = 'clalflulk'
CLALVULTRUL = 'clalvultrul'
FLANVONSTIX = 'flanvonstix'
SKIXSLALCLON = 'skixslalclon'
GLONBLAXK = 'glonblaxk'
KRORCLEXT = 'krorclext'
STEXSTORKRIM = 'stexstorkrim'
GRARCLORL = 'grarclorl'
GLALSPOS = 'glalspos'
GLIMFLENDRUR = 'glimflendrur'
KREXDRURR = 'krexdrurr'
DRENBLIXPRENL = 'drenblixprenl'
GLIMFLAR = 'glimflar'
DRALGRARK = 'dralgrark'
VALSLENT = 'valslent'
STEXCLAXVEX = 'stexclaxvex'
FLURFLARBRANK = 'flurflarbrank'
GREXDRELN = 'grexdreln'
PRELBLAL = 'prelblal'
SKALTROSN = 'skaltrosn'
PROSDRONPRORK = 'prosdronprork'
VELDRANKRURT = 'veldrankrurt'
SLAXTRULR = 'slaxtrulr'
GRANTRALDREXK = 'grantraldrexk'
GLONSPAN = 'glonspan'
GREXDRAX = 'grexdrax'
SPELSTURSLARK = 'spelsturslark'
BRORFLIXR = 'brorflixr'
PRORSTALSLUR = 'prorstalslur'
VEXSKEXKRELN = 'vexskexkreln'
FLEXDRAXBLON = 'flexdraxblon'
BLULSLALSKEXX = 'blulslalskexx'
SPOSSTIXK = 'sposstixk'
SKURSLEXN = 'skurslexn'
STALDRAXK = 'staldraxk'
GRENKRALPRIXN = 'grenkralprixn'
SLIXGRARN = 'slixgrarn'
CLIMKRIMSPEN = 'climkrimspen'

_R = {
    GRENKRALPRIXN: 0,
    SLIXGRARN: 1,
    CLIMKRIMSPEN: 2,
}

_CTX_WRITES_KEY  = 'flurslex'
_CTX_WRITE_STATE = SLEXFLIXPRALL

class DreltrellFSM:
    def __init__(self):
        self._state = {}

    def _skosflimk(self, hint):
        assert self._state.get("current") == SKOSFLIMK, \
            f"dreltrell.skosflimk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skosflimk', 2:
                self._state["current"] = CLIMKRIMSPEN
                self._state["trig"]    = "hint:2"
            case 'skosflimk', _:
                self._state["current"] = FLOSBROSX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skosflimk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skosflimk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skosflimk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _flosbrosx(self, hint):
        assert self._state.get("current") == FLOSBROSX, \
            f"dreltrell.flosbrosx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'flosbrosx', 2:
                self._state["current"] = CLIMKRIMSPEN
                self._state["trig"]    = "hint:2"
            case 'flosbrosx', 1:
                self._state["current"] = FLIXFLALX
                self._state["trig"]    = "hint:1"
            case 'flosbrosx', _:
                self._state["current"] = GLARGRIXL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'flosbrosx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'flosbrosx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"flosbrosx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glargrixl(self, hint):
        assert self._state.get("current") == GLARGRIXL, \
            f"dreltrell.glargrixl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glargrixl', 2:
                self._state["current"] = CLIMKRIMSPEN
                self._state["trig"]    = "hint:2"
            case 'glargrixl', _:
                self._state["current"] = FLIXFLALX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glargrixl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glargrixl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glargrixl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _flixflalx(self, hint):
        assert self._state.get("current") == FLIXFLALX, \
            f"dreltrell.flixflalx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'flixflalx', 2:
                self._state["current"] = CLIMKRIMSPEN
                self._state["trig"]    = "hint:2"
            case 'flixflalx', _:
                self._state["current"] = BRARGLIMR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'flixflalx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'flixflalx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"flixflalx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brarglimr(self, hint):
        assert self._state.get("current") == BRARGLIMR, \
            f"dreltrell.brarglimr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brarglimr', 2:
                self._state["current"] = CLIMKRIMSPEN
                self._state["trig"]    = "hint:2"
            case 'brarglimr', _:
                self._state["current"] = GRELBRONPRANR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brarglimr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brarglimr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brarglimr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _grelbronpranr(self, hint):
        assert self._state.get("current") == GRELBRONPRANR, \
            f"dreltrell.grelbronpranr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'grelbronpranr', 2:
                self._state["current"] = CLIMKRIMSPEN
                self._state["trig"]    = "hint:2"
            case 'grelbronpranr', 1:
                self._state["current"] = SLEXFLIXPRALL
                self._state["trig"]    = "hint:1"
            case 'grelbronpranr', _:
                self._state["current"] = FLEXVOSN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'grelbronpranr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'grelbronpranr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"grelbronpranr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _flexvosn(self, hint):
        assert self._state.get("current") == FLEXVOSN, \
            f"dreltrell.flexvosn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'flexvosn', 2:
                self._state["current"] = CLIMKRIMSPEN
                self._state["trig"]    = "hint:2"
            case 'flexvosn', _:
                self._state["current"] = SLEXFLIXPRALL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'flexvosn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'flexvosn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"flexvosn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slexflixprall(self, hint):
        assert self._state.get("current") == SLEXFLIXPRALL, \
            f"dreltrell.slexflixprall: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        _ctx_val_before = self._state["ctx"].get(_CTX_WRITES_KEY, 0)
        match self._state["current"], hint:
            case 'slexflixprall', 2:
                self._state["current"] = CLIMKRIMSPEN
                self._state["trig"]    = "hint:2"
            case 'slexflixprall', 1:
                self._state["current"] = SLIXGRARN
                self._state["trig"]    = "hint:1"
            case 'slexflixprall', _:
                self._state["current"] = SKANSKIXSKARN
                self._state["trig"]    = "auto"
        _old = self._state["ctx"].get(_CTX_WRITES_KEY, 0)
        _inc = 2 if hint == 2 else 1
        self._state["ctx"][_CTX_WRITES_KEY] = _old + _inc
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slexflixprall', _to, _trig)
        _conds = {"hint_branch": _hint_branch,
                   "ctx_write": True,
                   "ctx_val_before": _ctx_val_before}
        _emit(self._state["cycle"], 1, __name__, 'slexflixprall',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slexflixprall->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skanskixskarn(self, hint):
        assert self._state.get("current") == SKANSKIXSKARN, \
            f"dreltrell.skanskixskarn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skanskixskarn', 2:
                self._state["current"] = CLIMKRIMSPEN
                self._state["trig"]    = "hint:2"
            case 'skanskixskarn', 1:
                self._state["current"] = SLIXGRARN
                self._state["trig"]    = "hint:1"
            case 'skanskixskarn', _:
                self._state["current"] = CLALGRONBRELK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skanskixskarn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skanskixskarn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skanskixskarn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _clalgronbrelk(self, hint):
        assert self._state.get("current") == CLALGRONBRELK, \
            f"dreltrell.clalgronbrelk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'clalgronbrelk', 2:
                self._state["current"] = CLIMKRIMSPEN
                self._state["trig"]    = "hint:2"
            case 'clalgronbrelk', _:
                self._state["current"] = VENGROS
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'clalgronbrelk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'clalgronbrelk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"clalgronbrelk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _vengros(self, hint):
        assert self._state.get("current") == VENGROS, \
            f"dreltrell.vengros: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'vengros', 2:
                self._state["current"] = CLIMKRIMSPEN
                self._state["trig"]    = "hint:2"
            case 'vengros', 0:
                self._state["current"] = SLIXGRARN
                self._state["trig"]    = "hint:0"
            case 'vengros', _:
                self._state["current"] = FLEXGRONDRAN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'vengros', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'vengros',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"vengros->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _flexgrondran(self, hint):
        assert self._state.get("current") == FLEXGRONDRAN, \
            f"dreltrell.flexgrondran: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'flexgrondran', 2:
                self._state["current"] = CLIMKRIMSPEN
                self._state["trig"]    = "hint:2"
            case 'flexgrondran', _:
                self._state["current"] = KROSCLONCLULN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'flexgrondran', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'flexgrondran',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"flexgrondran->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _kroscloncluln(self, hint):
        assert self._state.get("current") == KROSCLONCLULN, \
            f"dreltrell.kroscloncluln: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'kroscloncluln', 2:
                self._state["current"] = CLIMKRIMSPEN
                self._state["trig"]    = "hint:2"
            case 'kroscloncluln', 0:
                self._state["current"] = SLIXGRARN
                self._state["trig"]    = "hint:0"
            case 'kroscloncluln', _:
                self._state["current"] = BLELSLOSR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'kroscloncluln', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'kroscloncluln',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"kroscloncluln->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blelslosr(self, hint):
        assert self._state.get("current") == BLELSLOSR, \
            f"dreltrell.blelslosr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blelslosr', 2:
                self._state["current"] = CLIMKRIMSPEN
                self._state["trig"]    = "hint:2"
            case 'blelslosr', _:
                self._state["current"] = CLENDRURK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blelslosr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blelslosr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blelslosr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _clendrurk(self, hint):
        assert self._state.get("current") == CLENDRURK, \
            f"dreltrell.clendrurk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'clendrurk', 2:
                self._state["current"] = CLIMKRIMSPEN
                self._state["trig"]    = "hint:2"
            case 'clendrurk', _:
                self._state["current"] = GLARBRAL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'clendrurk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'clendrurk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"clendrurk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glarbral(self, hint):
        assert self._state.get("current") == GLARBRAL, \
            f"dreltrell.glarbral: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glarbral', 2:
                self._state["current"] = CLIMKRIMSPEN
                self._state["trig"]    = "hint:2"
            case 'glarbral', _:
                self._state["current"] = BRANFLONR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glarbral', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glarbral',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glarbral->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _branflonr(self, hint):
        assert self._state.get("current") == BRANFLONR, \
            f"dreltrell.branflonr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'branflonr', 2:
                self._state["current"] = CLIMKRIMSPEN
                self._state["trig"]    = "hint:2"
            case 'branflonr', _:
                self._state["current"] = SLEXGLORCLIMX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'branflonr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'branflonr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"branflonr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slexglorclimx(self, hint):
        assert self._state.get("current") == SLEXGLORCLIMX, \
            f"dreltrell.slexglorclimx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slexglorclimx', 2:
                self._state["current"] = CLIMKRIMSPEN
                self._state["trig"]    = "hint:2"
            case 'slexglorclimx', _:
                self._state["current"] = TRALSPIM
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slexglorclimx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slexglorclimx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slexglorclimx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _tralspim(self, hint):
        assert self._state.get("current") == TRALSPIM, \
            f"dreltrell.tralspim: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'tralspim', 2:
                self._state["current"] = CLIMKRIMSPEN
                self._state["trig"]    = "hint:2"
            case 'tralspim', _:
                self._state["current"] = TRIMSLONGLIXL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'tralspim', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'tralspim',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"tralspim->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _trimslonglixl(self, hint):
        assert self._state.get("current") == TRIMSLONGLIXL, \
            f"dreltrell.trimslonglixl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'trimslonglixl', 2:
                self._state["current"] = CLIMKRIMSPEN
                self._state["trig"]    = "hint:2"
            case 'trimslonglixl', _:
                self._state["current"] = BRURKRORTRIM
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'trimslonglixl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'trimslonglixl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"trimslonglixl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brurkrortrim(self, hint):
        assert self._state.get("current") == BRURKRORTRIM, \
            f"dreltrell.brurkrortrim: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brurkrortrim', 2:
                self._state["current"] = CLIMKRIMSPEN
                self._state["trig"]    = "hint:2"
            case 'brurkrortrim', _:
                self._state["current"] = SKONFLOSGRON
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brurkrortrim', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brurkrortrim',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brurkrortrim->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skonflosgron(self, hint):
        assert self._state.get("current") == SKONFLOSGRON, \
            f"dreltrell.skonflosgron: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skonflosgron', 2:
                self._state["current"] = CLIMKRIMSPEN
                self._state["trig"]    = "hint:2"
            case 'skonflosgron', _:
                self._state["current"] = BLIXSPONL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skonflosgron', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skonflosgron',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skonflosgron->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blixsponl(self, hint):
        assert self._state.get("current") == BLIXSPONL, \
            f"dreltrell.blixsponl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blixsponl', 2:
                self._state["current"] = CLIMKRIMSPEN
                self._state["trig"]    = "hint:2"
            case 'blixsponl', 0:
                self._state["current"] = SLIXGRARN
                self._state["trig"]    = "hint:0"
            case 'blixsponl', _:
                self._state["current"] = CLALKREXK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blixsponl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blixsponl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blixsponl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _clalkrexk(self, hint):
        assert self._state.get("current") == CLALKREXK, \
            f"dreltrell.clalkrexk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'clalkrexk', 2:
                self._state["current"] = CLIMKRIMSPEN
                self._state["trig"]    = "hint:2"
            case 'clalkrexk', _:
                self._state["current"] = CLELGLENFLAR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'clalkrexk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'clalkrexk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"clalkrexk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _clelglenflar(self, hint):
        assert self._state.get("current") == CLELGLENFLAR, \
            f"dreltrell.clelglenflar: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'clelglenflar', 2:
                self._state["current"] = CLIMKRIMSPEN
                self._state["trig"]    = "hint:2"
            case 'clelglenflar', _:
                self._state["current"] = PRONSLOSFLAX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'clelglenflar', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'clelglenflar',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"clelglenflar->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _pronslosflax(self, hint):
        assert self._state.get("current") == PRONSLOSFLAX, \
            f"dreltrell.pronslosflax: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'pronslosflax', 2:
                self._state["current"] = CLIMKRIMSPEN
                self._state["trig"]    = "hint:2"
            case 'pronslosflax', 0:
                self._state["current"] = SLIXGRARN
                self._state["trig"]    = "hint:0"
            case 'pronslosflax', _:
                self._state["current"] = GLANFLELVULK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'pronslosflax', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'pronslosflax',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"pronslosflax->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glanflelvulk(self, hint):
        assert self._state.get("current") == GLANFLELVULK, \
            f"dreltrell.glanflelvulk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glanflelvulk', 2:
                self._state["current"] = CLIMKRIMSPEN
                self._state["trig"]    = "hint:2"
            case 'glanflelvulk', 1:
                self._state["current"] = KROSVONGLAXN
                self._state["trig"]    = "hint:1"
            case 'glanflelvulk', _:
                self._state["current"] = BLAXGLURL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glanflelvulk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glanflelvulk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glanflelvulk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blaxglurl(self, hint):
        assert self._state.get("current") == BLAXGLURL, \
            f"dreltrell.blaxglurl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blaxglurl', 2:
                self._state["current"] = CLIMKRIMSPEN
                self._state["trig"]    = "hint:2"
            case 'blaxglurl', 0:
                self._state["current"] = SLIXGRARN
                self._state["trig"]    = "hint:0"
            case 'blaxglurl', _:
                self._state["current"] = KROSVONGLAXN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blaxglurl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blaxglurl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blaxglurl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _krosvonglaxn(self, hint):
        assert self._state.get("current") == KROSVONGLAXN, \
            f"dreltrell.krosvonglaxn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'krosvonglaxn', 2:
                self._state["current"] = CLIMKRIMSPEN
                self._state["trig"]    = "hint:2"
            case 'krosvonglaxn', 0:
                self._state["current"] = CLALFLULK
                self._state["trig"]    = "hint:0"
            case 'krosvonglaxn', _:
                self._state["current"] = GROSBREL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'krosvonglaxn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'krosvonglaxn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"krosvonglaxn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _grosbrel(self, hint):
        assert self._state.get("current") == GROSBREL, \
            f"dreltrell.grosbrel: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'grosbrel', 2:
                self._state["current"] = CLIMKRIMSPEN
                self._state["trig"]    = "hint:2"
            case 'grosbrel', _:
                self._state["current"] = CLALFLULK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'grosbrel', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'grosbrel',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"grosbrel->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _clalflulk(self, hint):
        assert self._state.get("current") == CLALFLULK, \
            f"dreltrell.clalflulk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'clalflulk', 2:
                self._state["current"] = CLIMKRIMSPEN
                self._state["trig"]    = "hint:2"
            case 'clalflulk', _:
                self._state["current"] = CLALVULTRUL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'clalflulk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'clalflulk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"clalflulk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _clalvultrul(self, hint):
        assert self._state.get("current") == CLALVULTRUL, \
            f"dreltrell.clalvultrul: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'clalvultrul', 2:
                self._state["current"] = CLIMKRIMSPEN
                self._state["trig"]    = "hint:2"
            case 'clalvultrul', _:
                self._state["current"] = FLANVONSTIX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'clalvultrul', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'clalvultrul',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"clalvultrul->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _flanvonstix(self, hint):
        assert self._state.get("current") == FLANVONSTIX, \
            f"dreltrell.flanvonstix: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'flanvonstix', 2:
                self._state["current"] = CLIMKRIMSPEN
                self._state["trig"]    = "hint:2"
            case 'flanvonstix', 0:
                self._state["current"] = SLIXGRARN
                self._state["trig"]    = "hint:0"
            case 'flanvonstix', _:
                self._state["current"] = SKIXSLALCLON
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'flanvonstix', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'flanvonstix',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"flanvonstix->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skixslalclon(self, hint):
        assert self._state.get("current") == SKIXSLALCLON, \
            f"dreltrell.skixslalclon: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skixslalclon', 2:
                self._state["current"] = CLIMKRIMSPEN
                self._state["trig"]    = "hint:2"
            case 'skixslalclon', 0:
                self._state["current"] = SLIXGRARN
                self._state["trig"]    = "hint:0"
            case 'skixslalclon', _:
                self._state["current"] = GLONBLAXK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skixslalclon', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skixslalclon',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skixslalclon->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glonblaxk(self, hint):
        assert self._state.get("current") == GLONBLAXK, \
            f"dreltrell.glonblaxk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glonblaxk', 2:
                self._state["current"] = CLIMKRIMSPEN
                self._state["trig"]    = "hint:2"
            case 'glonblaxk', _:
                self._state["current"] = KRORCLEXT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glonblaxk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glonblaxk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glonblaxk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _krorclext(self, hint):
        assert self._state.get("current") == KRORCLEXT, \
            f"dreltrell.krorclext: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'krorclext', 2:
                self._state["current"] = CLIMKRIMSPEN
                self._state["trig"]    = "hint:2"
            case 'krorclext', 1:
                self._state["current"] = GRARCLORL
                self._state["trig"]    = "hint:1"
            case 'krorclext', _:
                self._state["current"] = STEXSTORKRIM
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'krorclext', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'krorclext',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"krorclext->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _stexstorkrim(self, hint):
        assert self._state.get("current") == STEXSTORKRIM, \
            f"dreltrell.stexstorkrim: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'stexstorkrim', 2:
                self._state["current"] = CLIMKRIMSPEN
                self._state["trig"]    = "hint:2"
            case 'stexstorkrim', 1:
                self._state["current"] = GLALSPOS
                self._state["trig"]    = "hint:1"
            case 'stexstorkrim', _:
                self._state["current"] = GRARCLORL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'stexstorkrim', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'stexstorkrim',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"stexstorkrim->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _grarclorl(self, hint):
        assert self._state.get("current") == GRARCLORL, \
            f"dreltrell.grarclorl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'grarclorl', 2:
                self._state["current"] = CLIMKRIMSPEN
                self._state["trig"]    = "hint:2"
            case 'grarclorl', 0:
                self._state["current"] = SLIXGRARN
                self._state["trig"]    = "hint:0"
            case 'grarclorl', _:
                self._state["current"] = GLALSPOS
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'grarclorl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'grarclorl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"grarclorl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glalspos(self, hint):
        assert self._state.get("current") == GLALSPOS, \
            f"dreltrell.glalspos: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glalspos', 2:
                self._state["current"] = CLIMKRIMSPEN
                self._state["trig"]    = "hint:2"
            case 'glalspos', 1:
                self._state["current"] = KREXDRURR
                self._state["trig"]    = "hint:1"
            case 'glalspos', _:
                self._state["current"] = GLIMFLENDRUR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glalspos', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glalspos',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glalspos->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glimflendrur(self, hint):
        assert self._state.get("current") == GLIMFLENDRUR, \
            f"dreltrell.glimflendrur: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glimflendrur', 2:
                self._state["current"] = CLIMKRIMSPEN
                self._state["trig"]    = "hint:2"
            case 'glimflendrur', 1:
                self._state["current"] = DRENBLIXPRENL
                self._state["trig"]    = "hint:1"
            case 'glimflendrur', _:
                self._state["current"] = KREXDRURR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glimflendrur', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glimflendrur',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glimflendrur->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _krexdrurr(self, hint):
        assert self._state.get("current") == KREXDRURR, \
            f"dreltrell.krexdrurr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'krexdrurr', 2:
                self._state["current"] = CLIMKRIMSPEN
                self._state["trig"]    = "hint:2"
            case 'krexdrurr', _:
                self._state["current"] = DRENBLIXPRENL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'krexdrurr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'krexdrurr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"krexdrurr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _drenblixprenl(self, hint):
        assert self._state.get("current") == DRENBLIXPRENL, \
            f"dreltrell.drenblixprenl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'drenblixprenl', 2:
                self._state["current"] = CLIMKRIMSPEN
                self._state["trig"]    = "hint:2"
            case 'drenblixprenl', _:
                self._state["current"] = GLIMFLAR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'drenblixprenl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'drenblixprenl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"drenblixprenl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glimflar(self, hint):
        assert self._state.get("current") == GLIMFLAR, \
            f"dreltrell.glimflar: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glimflar', 2:
                self._state["current"] = CLIMKRIMSPEN
                self._state["trig"]    = "hint:2"
            case 'glimflar', _:
                self._state["current"] = DRALGRARK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glimflar', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glimflar',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glimflar->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _dralgrark(self, hint):
        assert self._state.get("current") == DRALGRARK, \
            f"dreltrell.dralgrark: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'dralgrark', 2:
                self._state["current"] = CLIMKRIMSPEN
                self._state["trig"]    = "hint:2"
            case 'dralgrark', _:
                self._state["current"] = VALSLENT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'dralgrark', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'dralgrark',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"dralgrark->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _valslent(self, hint):
        assert self._state.get("current") == VALSLENT, \
            f"dreltrell.valslent: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'valslent', 2:
                self._state["current"] = CLIMKRIMSPEN
                self._state["trig"]    = "hint:2"
            case 'valslent', 0:
                self._state["current"] = SLIXGRARN
                self._state["trig"]    = "hint:0"
            case 'valslent', _:
                self._state["current"] = STEXCLAXVEX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'valslent', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'valslent',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"valslent->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _stexclaxvex(self, hint):
        assert self._state.get("current") == STEXCLAXVEX, \
            f"dreltrell.stexclaxvex: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'stexclaxvex', 2:
                self._state["current"] = CLIMKRIMSPEN
                self._state["trig"]    = "hint:2"
            case 'stexclaxvex', _:
                self._state["current"] = FLURFLARBRANK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'stexclaxvex', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'stexclaxvex',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"stexclaxvex->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _flurflarbrank(self, hint):
        assert self._state.get("current") == FLURFLARBRANK, \
            f"dreltrell.flurflarbrank: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'flurflarbrank', 2:
                self._state["current"] = CLIMKRIMSPEN
                self._state["trig"]    = "hint:2"
            case 'flurflarbrank', 0:
                self._state["current"] = SLIXGRARN
                self._state["trig"]    = "hint:0"
            case 'flurflarbrank', _:
                self._state["current"] = GREXDRELN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'flurflarbrank', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'flurflarbrank',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"flurflarbrank->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _grexdreln(self, hint):
        assert self._state.get("current") == GREXDRELN, \
            f"dreltrell.grexdreln: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'grexdreln', 2:
                self._state["current"] = CLIMKRIMSPEN
                self._state["trig"]    = "hint:2"
            case 'grexdreln', 0:
                self._state["current"] = SLIXGRARN
                self._state["trig"]    = "hint:0"
            case 'grexdreln', _:
                self._state["current"] = PRELBLAL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'grexdreln', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'grexdreln',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"grexdreln->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _prelblal(self, hint):
        assert self._state.get("current") == PRELBLAL, \
            f"dreltrell.prelblal: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'prelblal', 2:
                self._state["current"] = CLIMKRIMSPEN
                self._state["trig"]    = "hint:2"
            case 'prelblal', 1:
                self._state["current"] = SLIXGRARN
                self._state["trig"]    = "hint:1"
            case 'prelblal', _:
                self._state["current"] = SKALTROSN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'prelblal', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'prelblal',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"prelblal->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skaltrosn(self, hint):
        assert self._state.get("current") == SKALTROSN, \
            f"dreltrell.skaltrosn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skaltrosn', 2:
                self._state["current"] = CLIMKRIMSPEN
                self._state["trig"]    = "hint:2"
            case 'skaltrosn', _:
                self._state["current"] = PROSDRONPRORK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skaltrosn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skaltrosn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skaltrosn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _prosdronprork(self, hint):
        assert self._state.get("current") == PROSDRONPRORK, \
            f"dreltrell.prosdronprork: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'prosdronprork', 2:
                self._state["current"] = CLIMKRIMSPEN
                self._state["trig"]    = "hint:2"
            case 'prosdronprork', _:
                self._state["current"] = VELDRANKRURT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'prosdronprork', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'prosdronprork',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"prosdronprork->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _veldrankrurt(self, hint):
        assert self._state.get("current") == VELDRANKRURT, \
            f"dreltrell.veldrankrurt: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'veldrankrurt', 2:
                self._state["current"] = CLIMKRIMSPEN
                self._state["trig"]    = "hint:2"
            case 'veldrankrurt', 0:
                self._state["current"] = SLIXGRARN
                self._state["trig"]    = "hint:0"
            case 'veldrankrurt', _:
                self._state["current"] = SLAXTRULR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'veldrankrurt', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'veldrankrurt',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"veldrankrurt->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slaxtrulr(self, hint):
        assert self._state.get("current") == SLAXTRULR, \
            f"dreltrell.slaxtrulr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slaxtrulr', 2:
                self._state["current"] = CLIMKRIMSPEN
                self._state["trig"]    = "hint:2"
            case 'slaxtrulr', 0:
                self._state["current"] = SLIXGRARN
                self._state["trig"]    = "hint:0"
            case 'slaxtrulr', _:
                self._state["current"] = GRANTRALDREXK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slaxtrulr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slaxtrulr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slaxtrulr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _grantraldrexk(self, hint):
        assert self._state.get("current") == GRANTRALDREXK, \
            f"dreltrell.grantraldrexk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'grantraldrexk', 2:
                self._state["current"] = CLIMKRIMSPEN
                self._state["trig"]    = "hint:2"
            case 'grantraldrexk', 0:
                self._state["current"] = GREXDRAX
                self._state["trig"]    = "hint:0"
            case 'grantraldrexk', _:
                self._state["current"] = GLONSPAN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'grantraldrexk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'grantraldrexk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"grantraldrexk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glonspan(self, hint):
        assert self._state.get("current") == GLONSPAN, \
            f"dreltrell.glonspan: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glonspan', 2:
                self._state["current"] = CLIMKRIMSPEN
                self._state["trig"]    = "hint:2"
            case 'glonspan', 0:
                self._state["current"] = SPELSTURSLARK
                self._state["trig"]    = "hint:0"
            case 'glonspan', _:
                self._state["current"] = GREXDRAX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glonspan', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glonspan',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glonspan->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _grexdrax(self, hint):
        assert self._state.get("current") == GREXDRAX, \
            f"dreltrell.grexdrax: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'grexdrax', 2:
                self._state["current"] = CLIMKRIMSPEN
                self._state["trig"]    = "hint:2"
            case 'grexdrax', 1:
                self._state["current"] = BRORFLIXR
                self._state["trig"]    = "hint:1"
            case 'grexdrax', _:
                self._state["current"] = SPELSTURSLARK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'grexdrax', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'grexdrax',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"grexdrax->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _spelsturslark(self, hint):
        assert self._state.get("current") == SPELSTURSLARK, \
            f"dreltrell.spelsturslark: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'spelsturslark', 2:
                self._state["current"] = CLIMKRIMSPEN
                self._state["trig"]    = "hint:2"
            case 'spelsturslark', 1:
                self._state["current"] = SLIXGRARN
                self._state["trig"]    = "hint:1"
            case 'spelsturslark', _:
                self._state["current"] = BRORFLIXR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'spelsturslark', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'spelsturslark',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"spelsturslark->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brorflixr(self, hint):
        assert self._state.get("current") == BRORFLIXR, \
            f"dreltrell.brorflixr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brorflixr', 2:
                self._state["current"] = CLIMKRIMSPEN
                self._state["trig"]    = "hint:2"
            case 'brorflixr', 0:
                self._state["current"] = SLIXGRARN
                self._state["trig"]    = "hint:0"
            case 'brorflixr', _:
                self._state["current"] = PRORSTALSLUR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brorflixr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brorflixr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brorflixr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _prorstalslur(self, hint):
        assert self._state.get("current") == PRORSTALSLUR, \
            f"dreltrell.prorstalslur: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'prorstalslur', 2:
                self._state["current"] = CLIMKRIMSPEN
                self._state["trig"]    = "hint:2"
            case 'prorstalslur', 0:
                self._state["current"] = FLEXDRAXBLON
                self._state["trig"]    = "hint:0"
            case 'prorstalslur', _:
                self._state["current"] = VEXSKEXKRELN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'prorstalslur', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'prorstalslur',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"prorstalslur->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _vexskexkreln(self, hint):
        assert self._state.get("current") == VEXSKEXKRELN, \
            f"dreltrell.vexskexkreln: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'vexskexkreln', 2:
                self._state["current"] = CLIMKRIMSPEN
                self._state["trig"]    = "hint:2"
            case 'vexskexkreln', _:
                self._state["current"] = FLEXDRAXBLON
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'vexskexkreln', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'vexskexkreln',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"vexskexkreln->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _flexdraxblon(self, hint):
        assert self._state.get("current") == FLEXDRAXBLON, \
            f"dreltrell.flexdraxblon: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'flexdraxblon', 2:
                self._state["current"] = CLIMKRIMSPEN
                self._state["trig"]    = "hint:2"
            case 'flexdraxblon', 0:
                self._state["current"] = SPOSSTIXK
                self._state["trig"]    = "hint:0"
            case 'flexdraxblon', _:
                self._state["current"] = BLULSLALSKEXX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'flexdraxblon', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'flexdraxblon',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"flexdraxblon->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blulslalskexx(self, hint):
        assert self._state.get("current") == BLULSLALSKEXX, \
            f"dreltrell.blulslalskexx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blulslalskexx', 2:
                self._state["current"] = CLIMKRIMSPEN
                self._state["trig"]    = "hint:2"
            case 'blulslalskexx', 1:
                self._state["current"] = SKURSLEXN
                self._state["trig"]    = "hint:1"
            case 'blulslalskexx', _:
                self._state["current"] = SPOSSTIXK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blulslalskexx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blulslalskexx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blulslalskexx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _sposstixk(self, hint):
        assert self._state.get("current") == SPOSSTIXK, \
            f"dreltrell.sposstixk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'sposstixk', 2:
                self._state["current"] = CLIMKRIMSPEN
                self._state["trig"]    = "hint:2"
            case 'sposstixk', _:
                self._state["current"] = SKURSLEXN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'sposstixk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'sposstixk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"sposstixk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skurslexn(self, hint):
        assert self._state.get("current") == SKURSLEXN, \
            f"dreltrell.skurslexn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skurslexn', 2:
                self._state["current"] = CLIMKRIMSPEN
                self._state["trig"]    = "hint:2"
            case 'skurslexn', 0:
                self._state["current"] = SLIXGRARN
                self._state["trig"]    = "hint:0"
            case 'skurslexn', _:
                self._state["current"] = STALDRAXK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skurslexn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skurslexn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skurslexn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _staldraxk(self, hint):
        assert self._state.get("current") == STALDRAXK, \
            f"dreltrell.staldraxk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'staldraxk', 2:
                self._state["current"] = CLIMKRIMSPEN
                self._state["trig"]    = "hint:2"
            case 'staldraxk', _:
                self._state["current"] = GRENKRALPRIXN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'staldraxk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'staldraxk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"staldraxk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def invoke(self, hint=None, span=None, caller=None, ctx=None, cycle=0):
        if ctx is None: ctx = {}

        self._state = {"current": SKOSFLIMK, "ctx": ctx,
                        "span": span, "caller": caller,
                        "trig": "auto", "cycle": cycle}
        _dispatch = {
            SKOSFLIMK: self._skosflimk,
            FLOSBROSX: self._flosbrosx,
            GLARGRIXL: self._glargrixl,
            FLIXFLALX: self._flixflalx,
            BRARGLIMR: self._brarglimr,
            GRELBRONPRANR: self._grelbronpranr,
            FLEXVOSN: self._flexvosn,
            SLEXFLIXPRALL: self._slexflixprall,
            SKANSKIXSKARN: self._skanskixskarn,
            CLALGRONBRELK: self._clalgronbrelk,
            VENGROS: self._vengros,
            FLEXGRONDRAN: self._flexgrondran,
            KROSCLONCLULN: self._kroscloncluln,
            BLELSLOSR: self._blelslosr,
            CLENDRURK: self._clendrurk,
            GLARBRAL: self._glarbral,
            BRANFLONR: self._branflonr,
            SLEXGLORCLIMX: self._slexglorclimx,
            TRALSPIM: self._tralspim,
            TRIMSLONGLIXL: self._trimslonglixl,
            BRURKRORTRIM: self._brurkrortrim,
            SKONFLOSGRON: self._skonflosgron,
            BLIXSPONL: self._blixsponl,
            CLALKREXK: self._clalkrexk,
            CLELGLENFLAR: self._clelglenflar,
            PRONSLOSFLAX: self._pronslosflax,
            GLANFLELVULK: self._glanflelvulk,
            BLAXGLURL: self._blaxglurl,
            KROSVONGLAXN: self._krosvonglaxn,
            GROSBREL: self._grosbrel,
            CLALFLULK: self._clalflulk,
            CLALVULTRUL: self._clalvultrul,
            FLANVONSTIX: self._flanvonstix,
            SKIXSLALCLON: self._skixslalclon,
            GLONBLAXK: self._glonblaxk,
            KRORCLEXT: self._krorclext,
            STEXSTORKRIM: self._stexstorkrim,
            GRARCLORL: self._grarclorl,
            GLALSPOS: self._glalspos,
            GLIMFLENDRUR: self._glimflendrur,
            KREXDRURR: self._krexdrurr,
            DRENBLIXPRENL: self._drenblixprenl,
            GLIMFLAR: self._glimflar,
            DRALGRARK: self._dralgrark,
            VALSLENT: self._valslent,
            STEXCLAXVEX: self._stexclaxvex,
            FLURFLARBRANK: self._flurflarbrank,
            GREXDRELN: self._grexdreln,
            PRELBLAL: self._prelblal,
            SKALTROSN: self._skaltrosn,
            PROSDRONPRORK: self._prosdronprork,
            VELDRANKRURT: self._veldrankrurt,
            SLAXTRULR: self._slaxtrulr,
            GRANTRALDREXK: self._grantraldrexk,
            GLONSPAN: self._glonspan,
            GREXDRAX: self._grexdrax,
            SPELSTURSLARK: self._spelsturslark,
            BRORFLIXR: self._brorflixr,
            PRORSTALSLUR: self._prorstalslur,
            VEXSKEXKRELN: self._vexskexkreln,
            FLEXDRAXBLON: self._flexdraxblon,
            BLULSLALSKEXX: self._blulslalskexx,
            SPOSSTIXK: self._sposstixk,
            SKURSLEXN: self._skurslexn,
            STALDRAXK: self._staldraxk,
        }
        while self._state["current"] not in _R and self._state["cycle"] - cycle < 8000:
            _dispatch[self._state["current"]](hint)
        _ret     = _R.get(self._state["current"], -1)
        _is_err  = self._state["current"] == CLIMKRIMSPEN
        if _is_err:
            _asrt    = {"failed": "no_error_terminal",
                         "expected": "terminal in {0, 1}",
                         "actual": f"ret={_ret}"}
            _xid_val = _xid(__name__, self._state["current"], "error", "terminal")
            _emit(self._state["cycle"], 1, __name__, self._state["current"],
                   {"hint": hint, "span": span, "caller": caller},
                   dict(ctx), {}, "terminal_error", _xid_val, assertion=_asrt)
            self._state["cycle"] += 1
        return _ret, self._state["cycle"]

def invoke(hint=None, span=None, caller=None, ctx=None, cycle=0):
    return DreltrellFSM().invoke(hint=hint, span=span, caller=caller, ctx=ctx, cycle=cycle)
