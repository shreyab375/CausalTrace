from _log import _w as _emit, _xid

VARBLOSCLIXX = 'varblosclixx'
PRURBLORVAXT = 'prurblorvaxt'
SKARTREXFLIMX = 'skartrexflimx'
PRIMSLULCLAX = 'primslulclax'
GLURSTULGREN = 'glurstulgren'
GREXGREL = 'grexgrel'
GROSSKONN = 'grosskonn'
DRURFLONL = 'drurflonl'
GLOSSPIX = 'glosspix'
BRAXSPOSN = 'braxsposn'
BRIMTRELKRAN = 'brimtrelkran'
PRENDRONL = 'prendronl'
CLIMBRUL = 'climbrul'
TRIXPRARK = 'trixprark'
GRIXSPURSLEX = 'grixspurslex'
GLEXPRIMT = 'glexprimt'
CLURGRIMT = 'clurgrimt'
FLULCLOR = 'flulclor'
SPURGLOR = 'spurglor'
PRARCLELT = 'prarclelt'
SPONPRULGLULR = 'sponprulglulr'
SKENKRELX = 'skenkrelx'
SLAXBRELKRAXX = 'slaxbrelkraxx'
PRALDRENBRURL = 'praldrenbrurl'
SLIMVEXL = 'slimvexl'
KRANFLANR = 'kranflanr'
VURSLIMSPEN = 'vurslimspen'
BLALSPARX = 'blalsparx'
DROSPRORSPEN = 'drosprorspen'
CLOSSLURKREXR = 'closslurkrexr'
SPANSLEX = 'spanslex'
GLAXSLAXK = 'glaxslaxk'
SPEXKRELN = 'spexkreln'
SPENBRALR = 'spenbralr'
DRALFLELGRIXX = 'dralflelgrixx'
BLURTRANGRAN = 'blurtrangran'
GLOSSLALCLUR = 'glosslalclur'
SKEXDRAL = 'skexdral'
GLEXPRIXSTENX = 'glexprixstenx'
PRULTRULTRELR = 'prultrultrelr'
GREXBRIMR = 'grexbrimr'
GLALCLANFLOST = 'glalclanflost'
SLIMCLIMFLOR = 'slimclimflor'
FLANVAXL = 'flanvaxl'
SKOSPROSN = 'skosprosn'
FLENPRONX = 'flenpronx'
BRORSLIX = 'brorslix'
CLIXBRIX = 'clixbrix'
VULBLONL = 'vulblonl'
SLIXPROS = 'slixpros'
KRULSKIXGROSX = 'krulskixgrosx'
SPIXSPALR = 'spixspalr'
BLALCLAXTRONR = 'blalclaxtronr'
STOSSLIXSKURN = 'stosslixskurn'
PRONTRAN = 'prontran'
KRALCLIXDRALX = 'kralclixdralx'
DRORFLENKRONK = 'drorflenkronk'
STEXSTAXSKIMT = 'stexstaxskimt'
SKIXDREXSKARN = 'skixdrexskarn'
BRARDRELR = 'brardrelr'
DRURCLURR = 'drurclurr'
BRONKRARSPURN = 'bronkrarspurn'
GLIXCLENT = 'glixclent'
GROSSTORX = 'grosstorx'
TRULKRAXX = 'trulkraxx'
PRIXGRAL = 'prixgral'
SKARDROSN = 'skardrosn'
FLORKREXGRANT = 'florkrexgrant'

_R = {
    PRIXGRAL: 0,
    SKARDROSN: 1,
    FLORKREXGRANT: 2,
}

_CTX_READS_KEY = 'flurslex'
_CTX_THRESHOLD = 16

class GlaltrimrFSM:
    def __init__(self):
        self._state = {}

    def _varblosclixx(self, hint):
        assert self._state.get("current") == VARBLOSCLIXX, \
            f"glaltrimr.varblosclixx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'varblosclixx', 2:
                self._state["current"] = FLORKREXGRANT
                self._state["trig"]    = "hint:2"
            case 'varblosclixx', 0:
                self._state["current"] = SKARTREXFLIMX
                self._state["trig"]    = "hint:0"
            case 'varblosclixx', _:
                self._state["current"] = PRURBLORVAXT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'varblosclixx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'varblosclixx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"varblosclixx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _prurblorvaxt(self, hint):
        assert self._state.get("current") == PRURBLORVAXT, \
            f"glaltrimr.prurblorvaxt: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'prurblorvaxt', 2:
                self._state["current"] = FLORKREXGRANT
                self._state["trig"]    = "hint:2"
            case 'prurblorvaxt', _:
                self._state["current"] = SKARTREXFLIMX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'prurblorvaxt', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'prurblorvaxt',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"prurblorvaxt->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skartrexflimx(self, hint):
        assert self._state.get("current") == SKARTREXFLIMX, \
            f"glaltrimr.skartrexflimx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skartrexflimx', 2:
                self._state["current"] = FLORKREXGRANT
                self._state["trig"]    = "hint:2"
            case 'skartrexflimx', 0:
                self._state["current"] = GLURSTULGREN
                self._state["trig"]    = "hint:0"
            case 'skartrexflimx', _:
                self._state["current"] = PRIMSLULCLAX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skartrexflimx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skartrexflimx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skartrexflimx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _primslulclax(self, hint):
        assert self._state.get("current") == PRIMSLULCLAX, \
            f"glaltrimr.primslulclax: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'primslulclax', 2:
                self._state["current"] = FLORKREXGRANT
                self._state["trig"]    = "hint:2"
            case 'primslulclax', _:
                self._state["current"] = GLURSTULGREN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'primslulclax', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'primslulclax',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"primslulclax->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glurstulgren(self, hint):
        assert self._state.get("current") == GLURSTULGREN, \
            f"glaltrimr.glurstulgren: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glurstulgren', 2:
                self._state["current"] = FLORKREXGRANT
                self._state["trig"]    = "hint:2"
            case 'glurstulgren', _:
                self._state["current"] = GREXGREL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glurstulgren', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glurstulgren',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glurstulgren->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _grexgrel(self, hint):
        assert self._state.get("current") == GREXGREL, \
            f"glaltrimr.grexgrel: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'grexgrel', 2:
                self._state["current"] = FLORKREXGRANT
                self._state["trig"]    = "hint:2"
            case 'grexgrel', 0:
                self._state["current"] = DRURFLONL
                self._state["trig"]    = "hint:0"
            case 'grexgrel', _:
                self._state["current"] = GROSSKONN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'grexgrel', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'grexgrel',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"grexgrel->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _grosskonn(self, hint):
        assert self._state.get("current") == GROSSKONN, \
            f"glaltrimr.grosskonn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'grosskonn', 2:
                self._state["current"] = FLORKREXGRANT
                self._state["trig"]    = "hint:2"
            case 'grosskonn', _:
                self._state["current"] = DRURFLONL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'grosskonn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'grosskonn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"grosskonn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _drurflonl(self, hint):
        assert self._state.get("current") == DRURFLONL, \
            f"glaltrimr.drurflonl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'drurflonl', 2:
                self._state["current"] = FLORKREXGRANT
                self._state["trig"]    = "hint:2"
            case 'drurflonl', _:
                self._state["current"] = GLOSSPIX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'drurflonl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'drurflonl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"drurflonl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glosspix(self, hint):
        assert self._state.get("current") == GLOSSPIX, \
            f"glaltrimr.glosspix: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glosspix', 2:
                self._state["current"] = FLORKREXGRANT
                self._state["trig"]    = "hint:2"
            case 'glosspix', 0:
                self._state["current"] = BRIMTRELKRAN
                self._state["trig"]    = "hint:0"
            case 'glosspix', _:
                self._state["current"] = BRAXSPOSN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glosspix', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glosspix',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glosspix->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _braxsposn(self, hint):
        assert self._state.get("current") == BRAXSPOSN, \
            f"glaltrimr.braxsposn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'braxsposn', 2:
                self._state["current"] = FLORKREXGRANT
                self._state["trig"]    = "hint:2"
            case 'braxsposn', _:
                self._state["current"] = BRIMTRELKRAN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'braxsposn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'braxsposn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"braxsposn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brimtrelkran(self, hint):
        assert self._state.get("current") == BRIMTRELKRAN, \
            f"glaltrimr.brimtrelkran: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brimtrelkran', 2:
                self._state["current"] = FLORKREXGRANT
                self._state["trig"]    = "hint:2"
            case 'brimtrelkran', 1:
                self._state["current"] = SKARDROSN
                self._state["trig"]    = "hint:1"
            case 'brimtrelkran', _:
                self._state["current"] = PRENDRONL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brimtrelkran', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brimtrelkran',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brimtrelkran->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _prendronl(self, hint):
        assert self._state.get("current") == PRENDRONL, \
            f"glaltrimr.prendronl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'prendronl', 2:
                self._state["current"] = FLORKREXGRANT
                self._state["trig"]    = "hint:2"
            case 'prendronl', 1:
                self._state["current"] = SKARDROSN
                self._state["trig"]    = "hint:1"
            case 'prendronl', _:
                self._state["current"] = CLIMBRUL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'prendronl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'prendronl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"prendronl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _climbrul(self, hint):
        assert self._state.get("current") == CLIMBRUL, \
            f"glaltrimr.climbrul: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'climbrul', 2:
                self._state["current"] = FLORKREXGRANT
                self._state["trig"]    = "hint:2"
            case 'climbrul', _:
                self._state["current"] = TRIXPRARK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'climbrul', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'climbrul',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"climbrul->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _trixprark(self, hint):
        assert self._state.get("current") == TRIXPRARK, \
            f"glaltrimr.trixprark: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'trixprark', 2:
                self._state["current"] = FLORKREXGRANT
                self._state["trig"]    = "hint:2"
            case 'trixprark', 1:
                self._state["current"] = SKARDROSN
                self._state["trig"]    = "hint:1"
            case 'trixprark', _:
                self._state["current"] = GRIXSPURSLEX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'trixprark', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'trixprark',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"trixprark->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _grixspurslex(self, hint):
        assert self._state.get("current") == GRIXSPURSLEX, \
            f"glaltrimr.grixspurslex: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'grixspurslex', 2:
                self._state["current"] = FLORKREXGRANT
                self._state["trig"]    = "hint:2"
            case 'grixspurslex', 1:
                self._state["current"] = SKARDROSN
                self._state["trig"]    = "hint:1"
            case 'grixspurslex', _:
                self._state["current"] = GLEXPRIMT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'grixspurslex', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'grixspurslex',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"grixspurslex->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glexprimt(self, hint):
        assert self._state.get("current") == GLEXPRIMT, \
            f"glaltrimr.glexprimt: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glexprimt', 2:
                self._state["current"] = FLORKREXGRANT
                self._state["trig"]    = "hint:2"
            case 'glexprimt', _:
                self._state["current"] = CLURGRIMT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glexprimt', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glexprimt',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glexprimt->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _clurgrimt(self, hint):
        assert self._state.get("current") == CLURGRIMT, \
            f"glaltrimr.clurgrimt: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'clurgrimt', 2:
                self._state["current"] = FLORKREXGRANT
                self._state["trig"]    = "hint:2"
            case 'clurgrimt', 1:
                self._state["current"] = SPURGLOR
                self._state["trig"]    = "hint:1"
            case 'clurgrimt', _:
                self._state["current"] = FLULCLOR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'clurgrimt', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'clurgrimt',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"clurgrimt->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _flulclor(self, hint):
        assert self._state.get("current") == FLULCLOR, \
            f"glaltrimr.flulclor: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'flulclor', 2:
                self._state["current"] = FLORKREXGRANT
                self._state["trig"]    = "hint:2"
            case 'flulclor', 0:
                self._state["current"] = SKARDROSN
                self._state["trig"]    = "hint:0"
            case 'flulclor', _:
                self._state["current"] = SPURGLOR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'flulclor', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'flulclor',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"flulclor->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _spurglor(self, hint):
        assert self._state.get("current") == SPURGLOR, \
            f"glaltrimr.spurglor: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'spurglor', 2:
                self._state["current"] = FLORKREXGRANT
                self._state["trig"]    = "hint:2"
            case 'spurglor', _:
                self._state["current"] = PRARCLELT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'spurglor', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'spurglor',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"spurglor->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _prarclelt(self, hint):
        assert self._state.get("current") == PRARCLELT, \
            f"glaltrimr.prarclelt: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'prarclelt', 2:
                self._state["current"] = FLORKREXGRANT
                self._state["trig"]    = "hint:2"
            case 'prarclelt', _:
                self._state["current"] = SPONPRULGLULR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'prarclelt', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'prarclelt',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"prarclelt->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _sponprulglulr(self, hint):
        assert self._state.get("current") == SPONPRULGLULR, \
            f"glaltrimr.sponprulglulr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'sponprulglulr', 2:
                self._state["current"] = FLORKREXGRANT
                self._state["trig"]    = "hint:2"
            case 'sponprulglulr', 0:
                self._state["current"] = SKARDROSN
                self._state["trig"]    = "hint:0"
            case 'sponprulglulr', _:
                self._state["current"] = SKENKRELX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'sponprulglulr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'sponprulglulr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"sponprulglulr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skenkrelx(self, hint):
        assert self._state.get("current") == SKENKRELX, \
            f"glaltrimr.skenkrelx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skenkrelx', 2:
                self._state["current"] = FLORKREXGRANT
                self._state["trig"]    = "hint:2"
            case 'skenkrelx', _:
                self._state["current"] = SLAXBRELKRAXX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skenkrelx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skenkrelx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skenkrelx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slaxbrelkraxx(self, hint):
        assert self._state.get("current") == SLAXBRELKRAXX, \
            f"glaltrimr.slaxbrelkraxx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slaxbrelkraxx', 2:
                self._state["current"] = FLORKREXGRANT
                self._state["trig"]    = "hint:2"
            case 'slaxbrelkraxx', 1:
                self._state["current"] = SKARDROSN
                self._state["trig"]    = "hint:1"
            case 'slaxbrelkraxx', _:
                self._state["current"] = PRALDRENBRURL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slaxbrelkraxx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slaxbrelkraxx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slaxbrelkraxx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _praldrenbrurl(self, hint):
        assert self._state.get("current") == PRALDRENBRURL, \
            f"glaltrimr.praldrenbrurl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'praldrenbrurl', 2:
                self._state["current"] = FLORKREXGRANT
                self._state["trig"]    = "hint:2"
            case 'praldrenbrurl', _:
                self._state["current"] = SLIMVEXL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'praldrenbrurl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'praldrenbrurl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"praldrenbrurl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slimvexl(self, hint):
        assert self._state.get("current") == SLIMVEXL, \
            f"glaltrimr.slimvexl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slimvexl', 2:
                self._state["current"] = FLORKREXGRANT
                self._state["trig"]    = "hint:2"
            case 'slimvexl', _:
                self._state["current"] = KRANFLANR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slimvexl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slimvexl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slimvexl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _kranflanr(self, hint):
        assert self._state.get("current") == KRANFLANR, \
            f"glaltrimr.kranflanr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'kranflanr', 2:
                self._state["current"] = FLORKREXGRANT
                self._state["trig"]    = "hint:2"
            case 'kranflanr', 1:
                self._state["current"] = BLALSPARX
                self._state["trig"]    = "hint:1"
            case 'kranflanr', _:
                self._state["current"] = VURSLIMSPEN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'kranflanr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'kranflanr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"kranflanr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _vurslimspen(self, hint):
        assert self._state.get("current") == VURSLIMSPEN, \
            f"glaltrimr.vurslimspen: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'vurslimspen', 2:
                self._state["current"] = FLORKREXGRANT
                self._state["trig"]    = "hint:2"
            case 'vurslimspen', _:
                self._state["current"] = BLALSPARX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'vurslimspen', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'vurslimspen',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"vurslimspen->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blalsparx(self, hint):
        assert self._state.get("current") == BLALSPARX, \
            f"glaltrimr.blalsparx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blalsparx', 2:
                self._state["current"] = FLORKREXGRANT
                self._state["trig"]    = "hint:2"
            case 'blalsparx', 1:
                self._state["current"] = SKARDROSN
                self._state["trig"]    = "hint:1"
            case 'blalsparx', _:
                self._state["current"] = DROSPRORSPEN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blalsparx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blalsparx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blalsparx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _drosprorspen(self, hint):
        assert self._state.get("current") == DROSPRORSPEN, \
            f"glaltrimr.drosprorspen: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'drosprorspen', 2:
                self._state["current"] = FLORKREXGRANT
                self._state["trig"]    = "hint:2"
            case 'drosprorspen', _:
                self._state["current"] = CLOSSLURKREXR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'drosprorspen', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'drosprorspen',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"drosprorspen->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _closslurkrexr(self, hint):
        assert self._state.get("current") == CLOSSLURKREXR, \
            f"glaltrimr.closslurkrexr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'closslurkrexr', 2:
                self._state["current"] = FLORKREXGRANT
                self._state["trig"]    = "hint:2"
            case 'closslurkrexr', 1:
                self._state["current"] = SKARDROSN
                self._state["trig"]    = "hint:1"
            case 'closslurkrexr', _:
                self._state["current"] = SPANSLEX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'closslurkrexr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'closslurkrexr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"closslurkrexr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _spanslex(self, hint):
        assert self._state.get("current") == SPANSLEX, \
            f"glaltrimr.spanslex: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'spanslex', 2:
                self._state["current"] = FLORKREXGRANT
                self._state["trig"]    = "hint:2"
            case 'spanslex', _:
                self._state["current"] = GLAXSLAXK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'spanslex', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'spanslex',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"spanslex->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glaxslaxk(self, hint):
        assert self._state.get("current") == GLAXSLAXK, \
            f"glaltrimr.glaxslaxk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glaxslaxk', 2:
                self._state["current"] = FLORKREXGRANT
                self._state["trig"]    = "hint:2"
            case 'glaxslaxk', 1:
                self._state["current"] = SKARDROSN
                self._state["trig"]    = "hint:1"
            case 'glaxslaxk', _:
                self._state["current"] = SPEXKRELN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glaxslaxk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glaxslaxk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glaxslaxk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _spexkreln(self, hint):
        assert self._state.get("current") == SPEXKRELN, \
            f"glaltrimr.spexkreln: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'spexkreln', 2:
                self._state["current"] = FLORKREXGRANT
                self._state["trig"]    = "hint:2"
            case 'spexkreln', _:
                self._state["current"] = SPENBRALR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'spexkreln', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'spexkreln',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"spexkreln->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _spenbralr(self, hint):
        assert self._state.get("current") == SPENBRALR, \
            f"glaltrimr.spenbralr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'spenbralr', 2:
                self._state["current"] = FLORKREXGRANT
                self._state["trig"]    = "hint:2"
            case 'spenbralr', 0:
                self._state["current"] = BLURTRANGRAN
                self._state["trig"]    = "hint:0"
            case 'spenbralr', _:
                self._state["current"] = DRALFLELGRIXX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'spenbralr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'spenbralr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"spenbralr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _dralflelgrixx(self, hint):
        assert self._state.get("current") == DRALFLELGRIXX, \
            f"glaltrimr.dralflelgrixx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'dralflelgrixx', 2:
                self._state["current"] = FLORKREXGRANT
                self._state["trig"]    = "hint:2"
            case 'dralflelgrixx', 0:
                self._state["current"] = GLOSSLALCLUR
                self._state["trig"]    = "hint:0"
            case 'dralflelgrixx', _:
                self._state["current"] = BLURTRANGRAN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'dralflelgrixx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'dralflelgrixx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"dralflelgrixx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blurtrangran(self, hint):
        assert self._state.get("current") == BLURTRANGRAN, \
            f"glaltrimr.blurtrangran: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blurtrangran', 2:
                self._state["current"] = FLORKREXGRANT
                self._state["trig"]    = "hint:2"
            case 'blurtrangran', _:
                self._state["current"] = GLOSSLALCLUR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blurtrangran', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blurtrangran',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blurtrangran->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glosslalclur(self, hint):
        assert self._state.get("current") == GLOSSLALCLUR, \
            f"glaltrimr.glosslalclur: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glosslalclur', 2:
                self._state["current"] = FLORKREXGRANT
                self._state["trig"]    = "hint:2"
            case 'glosslalclur', _:
                self._state["current"] = SKEXDRAL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glosslalclur', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glosslalclur',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glosslalclur->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skexdral(self, hint):
        assert self._state.get("current") == SKEXDRAL, \
            f"glaltrimr.skexdral: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skexdral', 2:
                self._state["current"] = FLORKREXGRANT
                self._state["trig"]    = "hint:2"
            case 'skexdral', _:
                self._state["current"] = GLEXPRIXSTENX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skexdral', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skexdral',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skexdral->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glexprixstenx(self, hint):
        assert self._state.get("current") == GLEXPRIXSTENX, \
            f"glaltrimr.glexprixstenx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glexprixstenx', 2:
                self._state["current"] = FLORKREXGRANT
                self._state["trig"]    = "hint:2"
            case 'glexprixstenx', 1:
                self._state["current"] = SKARDROSN
                self._state["trig"]    = "hint:1"
            case 'glexprixstenx', _:
                self._state["current"] = PRULTRULTRELR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glexprixstenx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glexprixstenx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glexprixstenx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _prultrultrelr(self, hint):
        assert self._state.get("current") == PRULTRULTRELR, \
            f"glaltrimr.prultrultrelr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'prultrultrelr', 2:
                self._state["current"] = FLORKREXGRANT
                self._state["trig"]    = "hint:2"
            case 'prultrultrelr', 1:
                self._state["current"] = GLALCLANFLOST
                self._state["trig"]    = "hint:1"
            case 'prultrultrelr', _:
                self._state["current"] = GREXBRIMR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'prultrultrelr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'prultrultrelr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"prultrultrelr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _grexbrimr(self, hint):
        assert self._state.get("current") == GREXBRIMR, \
            f"glaltrimr.grexbrimr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'grexbrimr', 2:
                self._state["current"] = FLORKREXGRANT
                self._state["trig"]    = "hint:2"
            case 'grexbrimr', 1:
                self._state["current"] = SLIMCLIMFLOR
                self._state["trig"]    = "hint:1"
            case 'grexbrimr', _:
                self._state["current"] = GLALCLANFLOST
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'grexbrimr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'grexbrimr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"grexbrimr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glalclanflost(self, hint):
        assert self._state.get("current") == GLALCLANFLOST, \
            f"glaltrimr.glalclanflost: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glalclanflost', 2:
                self._state["current"] = FLORKREXGRANT
                self._state["trig"]    = "hint:2"
            case 'glalclanflost', _:
                self._state["current"] = SLIMCLIMFLOR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glalclanflost', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glalclanflost',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glalclanflost->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slimclimflor(self, hint):
        assert self._state.get("current") == SLIMCLIMFLOR, \
            f"glaltrimr.slimclimflor: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slimclimflor', 2:
                self._state["current"] = FLORKREXGRANT
                self._state["trig"]    = "hint:2"
            case 'slimclimflor', 1:
                self._state["current"] = SKOSPROSN
                self._state["trig"]    = "hint:1"
            case 'slimclimflor', _:
                self._state["current"] = FLANVAXL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slimclimflor', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slimclimflor',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slimclimflor->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _flanvaxl(self, hint):
        assert self._state.get("current") == FLANVAXL, \
            f"glaltrimr.flanvaxl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'flanvaxl', 2:
                self._state["current"] = FLORKREXGRANT
                self._state["trig"]    = "hint:2"
            case 'flanvaxl', 1:
                self._state["current"] = FLENPRONX
                self._state["trig"]    = "hint:1"
            case 'flanvaxl', _:
                self._state["current"] = SKOSPROSN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'flanvaxl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'flanvaxl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"flanvaxl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skosprosn(self, hint):
        assert self._state.get("current") == SKOSPROSN, \
            f"glaltrimr.skosprosn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skosprosn', 2:
                self._state["current"] = FLORKREXGRANT
                self._state["trig"]    = "hint:2"
            case 'skosprosn', _:
                self._state["current"] = FLENPRONX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skosprosn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skosprosn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skosprosn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _flenpronx(self, hint):
        assert self._state.get("current") == FLENPRONX, \
            f"glaltrimr.flenpronx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'flenpronx', 2:
                self._state["current"] = FLORKREXGRANT
                self._state["trig"]    = "hint:2"
            case 'flenpronx', _:
                self._state["current"] = BRORSLIX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'flenpronx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'flenpronx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"flenpronx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brorslix(self, hint):
        assert self._state.get("current") == BRORSLIX, \
            f"glaltrimr.brorslix: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brorslix', 2:
                self._state["current"] = FLORKREXGRANT
                self._state["trig"]    = "hint:2"
            case 'brorslix', 1:
                self._state["current"] = VULBLONL
                self._state["trig"]    = "hint:1"
            case 'brorslix', _:
                self._state["current"] = CLIXBRIX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brorslix', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brorslix',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brorslix->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _clixbrix(self, hint):
        assert self._state.get("current") == CLIXBRIX, \
            f"glaltrimr.clixbrix: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'clixbrix', 2:
                self._state["current"] = FLORKREXGRANT
                self._state["trig"]    = "hint:2"
            case 'clixbrix', _:
                self._state["current"] = VULBLONL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'clixbrix', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'clixbrix',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"clixbrix->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _vulblonl(self, hint):
        assert self._state.get("current") == VULBLONL, \
            f"glaltrimr.vulblonl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'vulblonl', 2:
                self._state["current"] = FLORKREXGRANT
                self._state["trig"]    = "hint:2"
            case 'vulblonl', 0:
                self._state["current"] = SKARDROSN
                self._state["trig"]    = "hint:0"
            case 'vulblonl', _:
                self._state["current"] = SLIXPROS
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'vulblonl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'vulblonl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"vulblonl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slixpros(self, hint):
        assert self._state.get("current") == SLIXPROS, \
            f"glaltrimr.slixpros: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slixpros', 2:
                self._state["current"] = FLORKREXGRANT
                self._state["trig"]    = "hint:2"
            case 'slixpros', _:
                self._state["current"] = KRULSKIXGROSX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slixpros', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slixpros',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slixpros->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _krulskixgrosx(self, hint):
        assert self._state.get("current") == KRULSKIXGROSX, \
            f"glaltrimr.krulskixgrosx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'krulskixgrosx', 2:
                self._state["current"] = FLORKREXGRANT
                self._state["trig"]    = "hint:2"
            case 'krulskixgrosx', _:
                self._state["current"] = SPIXSPALR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'krulskixgrosx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'krulskixgrosx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"krulskixgrosx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _spixspalr(self, hint):
        assert self._state.get("current") == SPIXSPALR, \
            f"glaltrimr.spixspalr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'spixspalr', 2:
                self._state["current"] = FLORKREXGRANT
                self._state["trig"]    = "hint:2"
            case 'spixspalr', _:
                self._state["current"] = BLALCLAXTRONR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'spixspalr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'spixspalr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"spixspalr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blalclaxtronr(self, hint):
        assert self._state.get("current") == BLALCLAXTRONR, \
            f"glaltrimr.blalclaxtronr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blalclaxtronr', 2:
                self._state["current"] = FLORKREXGRANT
                self._state["trig"]    = "hint:2"
            case 'blalclaxtronr', _:
                self._state["current"] = STOSSLIXSKURN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blalclaxtronr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blalclaxtronr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blalclaxtronr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _stosslixskurn(self, hint):
        assert self._state.get("current") == STOSSLIXSKURN, \
            f"glaltrimr.stosslixskurn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'stosslixskurn', 2:
                self._state["current"] = FLORKREXGRANT
                self._state["trig"]    = "hint:2"
            case 'stosslixskurn', _:
                self._state["current"] = PRONTRAN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'stosslixskurn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'stosslixskurn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"stosslixskurn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _prontran(self, hint):
        assert self._state.get("current") == PRONTRAN, \
            f"glaltrimr.prontran: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'prontran', 2:
                self._state["current"] = FLORKREXGRANT
                self._state["trig"]    = "hint:2"
            case 'prontran', _:
                self._state["current"] = KRALCLIXDRALX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'prontran', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'prontran',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"prontran->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _kralclixdralx(self, hint):
        assert self._state.get("current") == KRALCLIXDRALX, \
            f"glaltrimr.kralclixdralx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'kralclixdralx', 2:
                self._state["current"] = FLORKREXGRANT
                self._state["trig"]    = "hint:2"
            case 'kralclixdralx', 1:
                self._state["current"] = SKARDROSN
                self._state["trig"]    = "hint:1"
            case 'kralclixdralx', _:
                self._state["current"] = DRORFLENKRONK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'kralclixdralx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'kralclixdralx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"kralclixdralx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _drorflenkronk(self, hint):
        assert self._state.get("current") == DRORFLENKRONK, \
            f"glaltrimr.drorflenkronk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'drorflenkronk', 2:
                self._state["current"] = FLORKREXGRANT
                self._state["trig"]    = "hint:2"
            case 'drorflenkronk', 0:
                self._state["current"] = SKARDROSN
                self._state["trig"]    = "hint:0"
            case 'drorflenkronk', _:
                self._state["current"] = STEXSTAXSKIMT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'drorflenkronk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'drorflenkronk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"drorflenkronk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _stexstaxskimt(self, hint):
        assert self._state.get("current") == STEXSTAXSKIMT, \
            f"glaltrimr.stexstaxskimt: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'stexstaxskimt', 2:
                self._state["current"] = FLORKREXGRANT
                self._state["trig"]    = "hint:2"
            case 'stexstaxskimt', 0:
                self._state["current"] = BRARDRELR
                self._state["trig"]    = "hint:0"
            case 'stexstaxskimt', _:
                self._state["current"] = SKIXDREXSKARN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'stexstaxskimt', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'stexstaxskimt',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"stexstaxskimt->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skixdrexskarn(self, hint):
        assert self._state.get("current") == SKIXDREXSKARN, \
            f"glaltrimr.skixdrexskarn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skixdrexskarn', 2:
                self._state["current"] = FLORKREXGRANT
                self._state["trig"]    = "hint:2"
            case 'skixdrexskarn', _:
                self._state["current"] = BRARDRELR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skixdrexskarn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skixdrexskarn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skixdrexskarn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brardrelr(self, hint):
        assert self._state.get("current") == BRARDRELR, \
            f"glaltrimr.brardrelr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brardrelr', 2:
                self._state["current"] = FLORKREXGRANT
                self._state["trig"]    = "hint:2"
            case 'brardrelr', 0:
                self._state["current"] = BRONKRARSPURN
                self._state["trig"]    = "hint:0"
            case 'brardrelr', _:
                self._state["current"] = DRURCLURR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brardrelr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brardrelr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brardrelr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _drurclurr(self, hint):
        assert self._state.get("current") == DRURCLURR, \
            f"glaltrimr.drurclurr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'drurclurr', 2:
                self._state["current"] = FLORKREXGRANT
                self._state["trig"]    = "hint:2"
            case 'drurclurr', 0:
                self._state["current"] = SKARDROSN
                self._state["trig"]    = "hint:0"
            case 'drurclurr', _:
                self._state["current"] = BRONKRARSPURN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'drurclurr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'drurclurr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"drurclurr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _bronkrarspurn(self, hint):
        assert self._state.get("current") == BRONKRARSPURN, \
            f"glaltrimr.bronkrarspurn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'bronkrarspurn', 2:
                self._state["current"] = FLORKREXGRANT
                self._state["trig"]    = "hint:2"
            case 'bronkrarspurn', _:
                self._state["current"] = GLIXCLENT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'bronkrarspurn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'bronkrarspurn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"bronkrarspurn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glixclent(self, hint):
        assert self._state.get("current") == GLIXCLENT, \
            f"glaltrimr.glixclent: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glixclent', 2:
                self._state["current"] = FLORKREXGRANT
                self._state["trig"]    = "hint:2"
            case 'glixclent', 0:
                self._state["current"] = TRULKRAXX
                self._state["trig"]    = "hint:0"
            case 'glixclent', _:
                self._state["current"] = GROSSTORX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glixclent', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glixclent',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glixclent->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _grosstorx(self, hint):
        assert self._state.get("current") == GROSSTORX, \
            f"glaltrimr.grosstorx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'grosstorx', 2:
                self._state["current"] = FLORKREXGRANT
                self._state["trig"]    = "hint:2"
            case 'grosstorx', 0:
                self._state["current"] = SKARDROSN
                self._state["trig"]    = "hint:0"
            case 'grosstorx', _:
                self._state["current"] = TRULKRAXX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'grosstorx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'grosstorx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"grosstorx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _trulkraxx(self, hint):
        assert self._state.get("current") == TRULKRAXX, \
            f"glaltrimr.trulkraxx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'trulkraxx', 2:
                self._state["current"] = FLORKREXGRANT
                self._state["trig"]    = "hint:2"
            case 'trulkraxx', 1:
                self._state["current"] = SKARDROSN
                self._state["trig"]    = "hint:1"
            case 'trulkraxx', _:
                self._state["current"] = PRIXGRAL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'trulkraxx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'trulkraxx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"trulkraxx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def invoke(self, hint=None, span=None, caller=None, ctx=None, cycle=0):
        if ctx is None: ctx = {}

        _cv    = ctx.get(_CTX_READS_KEY, 0)
        _conds = {"ctx_degraded": _cv > 0,
                   "threshold_exceeded": _cv >= _CTX_THRESHOLD}
        if _cv >= _CTX_THRESHOLD:
            _asrt = {"failed": "ctx_below_threshold",
                      "expected": f"ctx[{_CTX_READS_KEY}] < {_CTX_THRESHOLD}",
                      "actual":   f"ctx[{_CTX_READS_KEY}] == {_cv}"}
            _xid_val = _xid(__name__, 'varblosclixx', "error", "assert_fail")
            _emit(cycle, 1, __name__, 'varblosclixx',
                   {"hint": hint, "span": span, "caller": caller},
                   dict(ctx), _conds,
                   "entry_blocked->error", _xid_val, assertion=_asrt)
            return 2, cycle + 1

        self._state = {"current": VARBLOSCLIXX, "ctx": ctx,
                        "span": span, "caller": caller,
                        "trig": "auto", "cycle": cycle}
        _dispatch = {
            VARBLOSCLIXX: self._varblosclixx,
            PRURBLORVAXT: self._prurblorvaxt,
            SKARTREXFLIMX: self._skartrexflimx,
            PRIMSLULCLAX: self._primslulclax,
            GLURSTULGREN: self._glurstulgren,
            GREXGREL: self._grexgrel,
            GROSSKONN: self._grosskonn,
            DRURFLONL: self._drurflonl,
            GLOSSPIX: self._glosspix,
            BRAXSPOSN: self._braxsposn,
            BRIMTRELKRAN: self._brimtrelkran,
            PRENDRONL: self._prendronl,
            CLIMBRUL: self._climbrul,
            TRIXPRARK: self._trixprark,
            GRIXSPURSLEX: self._grixspurslex,
            GLEXPRIMT: self._glexprimt,
            CLURGRIMT: self._clurgrimt,
            FLULCLOR: self._flulclor,
            SPURGLOR: self._spurglor,
            PRARCLELT: self._prarclelt,
            SPONPRULGLULR: self._sponprulglulr,
            SKENKRELX: self._skenkrelx,
            SLAXBRELKRAXX: self._slaxbrelkraxx,
            PRALDRENBRURL: self._praldrenbrurl,
            SLIMVEXL: self._slimvexl,
            KRANFLANR: self._kranflanr,
            VURSLIMSPEN: self._vurslimspen,
            BLALSPARX: self._blalsparx,
            DROSPRORSPEN: self._drosprorspen,
            CLOSSLURKREXR: self._closslurkrexr,
            SPANSLEX: self._spanslex,
            GLAXSLAXK: self._glaxslaxk,
            SPEXKRELN: self._spexkreln,
            SPENBRALR: self._spenbralr,
            DRALFLELGRIXX: self._dralflelgrixx,
            BLURTRANGRAN: self._blurtrangran,
            GLOSSLALCLUR: self._glosslalclur,
            SKEXDRAL: self._skexdral,
            GLEXPRIXSTENX: self._glexprixstenx,
            PRULTRULTRELR: self._prultrultrelr,
            GREXBRIMR: self._grexbrimr,
            GLALCLANFLOST: self._glalclanflost,
            SLIMCLIMFLOR: self._slimclimflor,
            FLANVAXL: self._flanvaxl,
            SKOSPROSN: self._skosprosn,
            FLENPRONX: self._flenpronx,
            BRORSLIX: self._brorslix,
            CLIXBRIX: self._clixbrix,
            VULBLONL: self._vulblonl,
            SLIXPROS: self._slixpros,
            KRULSKIXGROSX: self._krulskixgrosx,
            SPIXSPALR: self._spixspalr,
            BLALCLAXTRONR: self._blalclaxtronr,
            STOSSLIXSKURN: self._stosslixskurn,
            PRONTRAN: self._prontran,
            KRALCLIXDRALX: self._kralclixdralx,
            DRORFLENKRONK: self._drorflenkronk,
            STEXSTAXSKIMT: self._stexstaxskimt,
            SKIXDREXSKARN: self._skixdrexskarn,
            BRARDRELR: self._brardrelr,
            DRURCLURR: self._drurclurr,
            BRONKRARSPURN: self._bronkrarspurn,
            GLIXCLENT: self._glixclent,
            GROSSTORX: self._grosstorx,
            TRULKRAXX: self._trulkraxx,
        }
        while self._state["current"] not in _R and self._state["cycle"] - cycle < 8000:
            _dispatch[self._state["current"]](hint)
        _ret     = _R.get(self._state["current"], -1)
        _is_err  = self._state["current"] == FLORKREXGRANT
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
    return GlaltrimrFSM().invoke(hint=hint, span=span, caller=caller, ctx=ctx, cycle=cycle)
