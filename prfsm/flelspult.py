from _log import _w as _emit, _xid

PRELTRENSKAL = 'preltrenskal'
SKONVAXSPAXN = 'skonvaxspaxn'
KRALBRIX = 'kralbrix'
SKEXGRELGLAX = 'skexgrelglax'
SKEXGLOSSPIM = 'skexglosspim'
SPALSKONX = 'spalskonx'
CLURSTENGRANX = 'clurstengranx'
DRORCLALVEL = 'drorclalvel'
TRULBRENL = 'trulbrenl'
GLIMSPELSLANN = 'glimspelslann'
PRELSTAR = 'prelstar'
SPARTRAXBLURL = 'spartraxblurl'
DRAXPRALSPARL = 'draxpralsparl'
BLULSPANL = 'blulspanl'
GLORGLAXT = 'glorglaxt'
BRONTRORN = 'brontrorn'
FLEXSKAL = 'flexskal'
TROSCLANR = 'trosclanr'
SKENSPUL = 'skenspul'
STELTRANGROR = 'steltrangror'
SKONSLENDRUL = 'skonslendrul'
TRIMTREXL = 'trimtrexl'
BLENGLORDREX = 'blenglordrex'
SLURGREN = 'slurgren'
BLELKRAXN = 'blelkraxn'
GLURPRELK = 'glurprelk'
BRURSPURSPAR = 'brurspurspar'
SKALGRORBRELK = 'skalgrorbrelk'
GLAXSPANGREXR = 'glaxspangrexr'
VANGROSSTEL = 'vangrosstel'
SPIMFLULN = 'spimfluln'
BRURSPALN = 'brurspaln'
FLORVARDRUR = 'florvardrur'
CLELFLALKRANR = 'clelflalkranr'
FLEXSPORGREN = 'flexsporgren'
TRURGRALSPAN = 'trurgralspan'
DRENDREXPRULK = 'drendrexprulk'
GRELSPALL = 'grelspall'
PRONPRULKRIM = 'pronprulkrim'
STEXTRAL = 'stextral'
PRONSKON = 'pronskon'
PRALTREXL = 'praltrexl'
KRIXGRURBRIXX = 'krixgrurbrixx'
DRAXSKURN = 'draxskurn'
PRENSLUR = 'prenslur'
KRORKROSCLUR = 'krorkrosclur'
CLARVULK = 'clarvulk'
BRIMSTUR = 'brimstur'
BLEXBLAXGLURX = 'blexblaxglurx'
PRIMBRARGLAX = 'primbrarglax'
KROSBLURSPOR = 'krosblurspor'
PRARSKEN = 'prarsken'
CLOSFLOST = 'closflost'
STARSLEXR = 'starslexr'
SLIXSKAR = 'slixskar'
TRANTREXR = 'trantrexr'
GRIXVEN = 'grixven'
GLORKRANSTOSX = 'glorkranstosx'
BRIMVELVAXX = 'brimvelvaxx'
DRURSTIXSTELR = 'drurstixstelr'
DRELSKARSPEXN = 'drelskarspexn'
CLORSTULL = 'clorstull'
SPULKRAL = 'spulkral'
DREXFLEXGLEX = 'drexflexglex'
SKARVALTRENT = 'skarvaltrent'
GLELGRIXCLAL = 'glelgrixclal'
KRANGREXGROS = 'krangrexgros'
CLARPRORGLORR = 'clarprorglorr'

_R = {
    GLELGRIXCLAL: 0,
    KRANGREXGROS: 1,
    CLARPRORGLORR: 2,
}

_CTX_WRITES_KEY  = 'flurslex'
_CTX_WRITE_STATE = KRALBRIX

class FlelspultFSM:
    def __init__(self):
        self._state = {}

    def _preltrenskal(self, hint):
        assert self._state.get("current") == PRELTRENSKAL, \
            f"flelspult.preltrenskal: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'preltrenskal', 2:
                self._state["current"] = CLARPRORGLORR
                self._state["trig"]    = "hint:2"
            case 'preltrenskal', 0:
                self._state["current"] = KRALBRIX
                self._state["trig"]    = "hint:0"
            case 'preltrenskal', _:
                self._state["current"] = SKONVAXSPAXN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'preltrenskal', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'preltrenskal',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"preltrenskal->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skonvaxspaxn(self, hint):
        assert self._state.get("current") == SKONVAXSPAXN, \
            f"flelspult.skonvaxspaxn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skonvaxspaxn', 2:
                self._state["current"] = CLARPRORGLORR
                self._state["trig"]    = "hint:2"
            case 'skonvaxspaxn', _:
                self._state["current"] = KRALBRIX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skonvaxspaxn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skonvaxspaxn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skonvaxspaxn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _kralbrix(self, hint):
        assert self._state.get("current") == KRALBRIX, \
            f"flelspult.kralbrix: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        _ctx_val_before = self._state["ctx"].get(_CTX_WRITES_KEY, 0)
        match self._state["current"], hint:
            case 'kralbrix', 2:
                self._state["current"] = CLARPRORGLORR
                self._state["trig"]    = "hint:2"
            case 'kralbrix', _:
                self._state["current"] = SKEXGRELGLAX
                self._state["trig"]    = "auto"
        _old = self._state["ctx"].get(_CTX_WRITES_KEY, 0)
        _inc = 2 if hint == 2 else 1
        self._state["ctx"][_CTX_WRITES_KEY] = _old + _inc
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'kralbrix', _to, _trig)
        _conds = {"hint_branch": _hint_branch,
                   "ctx_write": True,
                   "ctx_val_before": _ctx_val_before}
        _emit(self._state["cycle"], 1, __name__, 'kralbrix',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"kralbrix->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skexgrelglax(self, hint):
        assert self._state.get("current") == SKEXGRELGLAX, \
            f"flelspult.skexgrelglax: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skexgrelglax', 2:
                self._state["current"] = CLARPRORGLORR
                self._state["trig"]    = "hint:2"
            case 'skexgrelglax', 1:
                self._state["current"] = KRANGREXGROS
                self._state["trig"]    = "hint:1"
            case 'skexgrelglax', _:
                self._state["current"] = SKEXGLOSSPIM
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skexgrelglax', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skexgrelglax',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skexgrelglax->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skexglosspim(self, hint):
        assert self._state.get("current") == SKEXGLOSSPIM, \
            f"flelspult.skexglosspim: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skexglosspim', 2:
                self._state["current"] = CLARPRORGLORR
                self._state["trig"]    = "hint:2"
            case 'skexglosspim', _:
                self._state["current"] = SPALSKONX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skexglosspim', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skexglosspim',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skexglosspim->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _spalskonx(self, hint):
        assert self._state.get("current") == SPALSKONX, \
            f"flelspult.spalskonx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'spalskonx', 2:
                self._state["current"] = CLARPRORGLORR
                self._state["trig"]    = "hint:2"
            case 'spalskonx', _:
                self._state["current"] = CLURSTENGRANX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'spalskonx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'spalskonx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"spalskonx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _clurstengranx(self, hint):
        assert self._state.get("current") == CLURSTENGRANX, \
            f"flelspult.clurstengranx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'clurstengranx', 2:
                self._state["current"] = CLARPRORGLORR
                self._state["trig"]    = "hint:2"
            case 'clurstengranx', 0:
                self._state["current"] = KRANGREXGROS
                self._state["trig"]    = "hint:0"
            case 'clurstengranx', _:
                self._state["current"] = DRORCLALVEL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'clurstengranx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'clurstengranx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"clurstengranx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _drorclalvel(self, hint):
        assert self._state.get("current") == DRORCLALVEL, \
            f"flelspult.drorclalvel: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'drorclalvel', 2:
                self._state["current"] = CLARPRORGLORR
                self._state["trig"]    = "hint:2"
            case 'drorclalvel', 0:
                self._state["current"] = KRANGREXGROS
                self._state["trig"]    = "hint:0"
            case 'drorclalvel', _:
                self._state["current"] = TRULBRENL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'drorclalvel', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'drorclalvel',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"drorclalvel->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _trulbrenl(self, hint):
        assert self._state.get("current") == TRULBRENL, \
            f"flelspult.trulbrenl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'trulbrenl', 2:
                self._state["current"] = CLARPRORGLORR
                self._state["trig"]    = "hint:2"
            case 'trulbrenl', 1:
                self._state["current"] = KRANGREXGROS
                self._state["trig"]    = "hint:1"
            case 'trulbrenl', _:
                self._state["current"] = GLIMSPELSLANN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'trulbrenl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'trulbrenl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"trulbrenl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glimspelslann(self, hint):
        assert self._state.get("current") == GLIMSPELSLANN, \
            f"flelspult.glimspelslann: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glimspelslann', 2:
                self._state["current"] = CLARPRORGLORR
                self._state["trig"]    = "hint:2"
            case 'glimspelslann', _:
                self._state["current"] = PRELSTAR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glimspelslann', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glimspelslann',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glimspelslann->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _prelstar(self, hint):
        assert self._state.get("current") == PRELSTAR, \
            f"flelspult.prelstar: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'prelstar', 2:
                self._state["current"] = CLARPRORGLORR
                self._state["trig"]    = "hint:2"
            case 'prelstar', _:
                self._state["current"] = SPARTRAXBLURL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'prelstar', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'prelstar',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"prelstar->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _spartraxblurl(self, hint):
        assert self._state.get("current") == SPARTRAXBLURL, \
            f"flelspult.spartraxblurl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'spartraxblurl', 2:
                self._state["current"] = CLARPRORGLORR
                self._state["trig"]    = "hint:2"
            case 'spartraxblurl', _:
                self._state["current"] = DRAXPRALSPARL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'spartraxblurl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'spartraxblurl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"spartraxblurl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _draxpralsparl(self, hint):
        assert self._state.get("current") == DRAXPRALSPARL, \
            f"flelspult.draxpralsparl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'draxpralsparl', 2:
                self._state["current"] = CLARPRORGLORR
                self._state["trig"]    = "hint:2"
            case 'draxpralsparl', 0:
                self._state["current"] = KRANGREXGROS
                self._state["trig"]    = "hint:0"
            case 'draxpralsparl', _:
                self._state["current"] = BLULSPANL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'draxpralsparl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'draxpralsparl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"draxpralsparl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blulspanl(self, hint):
        assert self._state.get("current") == BLULSPANL, \
            f"flelspult.blulspanl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blulspanl', 2:
                self._state["current"] = CLARPRORGLORR
                self._state["trig"]    = "hint:2"
            case 'blulspanl', _:
                self._state["current"] = GLORGLAXT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blulspanl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blulspanl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blulspanl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glorglaxt(self, hint):
        assert self._state.get("current") == GLORGLAXT, \
            f"flelspult.glorglaxt: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glorglaxt', 2:
                self._state["current"] = CLARPRORGLORR
                self._state["trig"]    = "hint:2"
            case 'glorglaxt', 1:
                self._state["current"] = FLEXSKAL
                self._state["trig"]    = "hint:1"
            case 'glorglaxt', _:
                self._state["current"] = BRONTRORN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glorglaxt', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glorglaxt',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glorglaxt->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brontrorn(self, hint):
        assert self._state.get("current") == BRONTRORN, \
            f"flelspult.brontrorn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brontrorn', 2:
                self._state["current"] = CLARPRORGLORR
                self._state["trig"]    = "hint:2"
            case 'brontrorn', _:
                self._state["current"] = FLEXSKAL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brontrorn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brontrorn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brontrorn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _flexskal(self, hint):
        assert self._state.get("current") == FLEXSKAL, \
            f"flelspult.flexskal: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'flexskal', 2:
                self._state["current"] = CLARPRORGLORR
                self._state["trig"]    = "hint:2"
            case 'flexskal', 0:
                self._state["current"] = KRANGREXGROS
                self._state["trig"]    = "hint:0"
            case 'flexskal', _:
                self._state["current"] = TROSCLANR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'flexskal', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'flexskal',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"flexskal->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _trosclanr(self, hint):
        assert self._state.get("current") == TROSCLANR, \
            f"flelspult.trosclanr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'trosclanr', 2:
                self._state["current"] = CLARPRORGLORR
                self._state["trig"]    = "hint:2"
            case 'trosclanr', 0:
                self._state["current"] = KRANGREXGROS
                self._state["trig"]    = "hint:0"
            case 'trosclanr', _:
                self._state["current"] = SKENSPUL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'trosclanr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'trosclanr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"trosclanr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skenspul(self, hint):
        assert self._state.get("current") == SKENSPUL, \
            f"flelspult.skenspul: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skenspul', 2:
                self._state["current"] = CLARPRORGLORR
                self._state["trig"]    = "hint:2"
            case 'skenspul', _:
                self._state["current"] = STELTRANGROR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skenspul', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skenspul',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skenspul->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _steltrangror(self, hint):
        assert self._state.get("current") == STELTRANGROR, \
            f"flelspult.steltrangror: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'steltrangror', 2:
                self._state["current"] = CLARPRORGLORR
                self._state["trig"]    = "hint:2"
            case 'steltrangror', 1:
                self._state["current"] = TRIMTREXL
                self._state["trig"]    = "hint:1"
            case 'steltrangror', _:
                self._state["current"] = SKONSLENDRUL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'steltrangror', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'steltrangror',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"steltrangror->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skonslendrul(self, hint):
        assert self._state.get("current") == SKONSLENDRUL, \
            f"flelspult.skonslendrul: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skonslendrul', 2:
                self._state["current"] = CLARPRORGLORR
                self._state["trig"]    = "hint:2"
            case 'skonslendrul', _:
                self._state["current"] = TRIMTREXL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skonslendrul', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skonslendrul',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skonslendrul->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _trimtrexl(self, hint):
        assert self._state.get("current") == TRIMTREXL, \
            f"flelspult.trimtrexl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'trimtrexl', 2:
                self._state["current"] = CLARPRORGLORR
                self._state["trig"]    = "hint:2"
            case 'trimtrexl', 0:
                self._state["current"] = KRANGREXGROS
                self._state["trig"]    = "hint:0"
            case 'trimtrexl', _:
                self._state["current"] = BLENGLORDREX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'trimtrexl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'trimtrexl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"trimtrexl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blenglordrex(self, hint):
        assert self._state.get("current") == BLENGLORDREX, \
            f"flelspult.blenglordrex: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blenglordrex', 2:
                self._state["current"] = CLARPRORGLORR
                self._state["trig"]    = "hint:2"
            case 'blenglordrex', _:
                self._state["current"] = SLURGREN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blenglordrex', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blenglordrex',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blenglordrex->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slurgren(self, hint):
        assert self._state.get("current") == SLURGREN, \
            f"flelspult.slurgren: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slurgren', 2:
                self._state["current"] = CLARPRORGLORR
                self._state["trig"]    = "hint:2"
            case 'slurgren', 0:
                self._state["current"] = GLURPRELK
                self._state["trig"]    = "hint:0"
            case 'slurgren', _:
                self._state["current"] = BLELKRAXN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slurgren', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slurgren',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slurgren->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blelkraxn(self, hint):
        assert self._state.get("current") == BLELKRAXN, \
            f"flelspult.blelkraxn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blelkraxn', 2:
                self._state["current"] = CLARPRORGLORR
                self._state["trig"]    = "hint:2"
            case 'blelkraxn', _:
                self._state["current"] = GLURPRELK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blelkraxn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blelkraxn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blelkraxn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glurprelk(self, hint):
        assert self._state.get("current") == GLURPRELK, \
            f"flelspult.glurprelk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glurprelk', 2:
                self._state["current"] = CLARPRORGLORR
                self._state["trig"]    = "hint:2"
            case 'glurprelk', 0:
                self._state["current"] = SKALGRORBRELK
                self._state["trig"]    = "hint:0"
            case 'glurprelk', _:
                self._state["current"] = BRURSPURSPAR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glurprelk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glurprelk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glurprelk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brurspurspar(self, hint):
        assert self._state.get("current") == BRURSPURSPAR, \
            f"flelspult.brurspurspar: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brurspurspar', 2:
                self._state["current"] = CLARPRORGLORR
                self._state["trig"]    = "hint:2"
            case 'brurspurspar', 1:
                self._state["current"] = GLAXSPANGREXR
                self._state["trig"]    = "hint:1"
            case 'brurspurspar', _:
                self._state["current"] = SKALGRORBRELK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brurspurspar', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brurspurspar',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brurspurspar->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skalgrorbrelk(self, hint):
        assert self._state.get("current") == SKALGRORBRELK, \
            f"flelspult.skalgrorbrelk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skalgrorbrelk', 2:
                self._state["current"] = CLARPRORGLORR
                self._state["trig"]    = "hint:2"
            case 'skalgrorbrelk', 0:
                self._state["current"] = KRANGREXGROS
                self._state["trig"]    = "hint:0"
            case 'skalgrorbrelk', _:
                self._state["current"] = GLAXSPANGREXR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skalgrorbrelk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skalgrorbrelk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skalgrorbrelk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glaxspangrexr(self, hint):
        assert self._state.get("current") == GLAXSPANGREXR, \
            f"flelspult.glaxspangrexr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glaxspangrexr', 2:
                self._state["current"] = CLARPRORGLORR
                self._state["trig"]    = "hint:2"
            case 'glaxspangrexr', 0:
                self._state["current"] = SPIMFLULN
                self._state["trig"]    = "hint:0"
            case 'glaxspangrexr', _:
                self._state["current"] = VANGROSSTEL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glaxspangrexr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glaxspangrexr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glaxspangrexr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _vangrosstel(self, hint):
        assert self._state.get("current") == VANGROSSTEL, \
            f"flelspult.vangrosstel: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'vangrosstel', 2:
                self._state["current"] = CLARPRORGLORR
                self._state["trig"]    = "hint:2"
            case 'vangrosstel', _:
                self._state["current"] = SPIMFLULN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'vangrosstel', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'vangrosstel',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"vangrosstel->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _spimfluln(self, hint):
        assert self._state.get("current") == SPIMFLULN, \
            f"flelspult.spimfluln: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'spimfluln', 2:
                self._state["current"] = CLARPRORGLORR
                self._state["trig"]    = "hint:2"
            case 'spimfluln', _:
                self._state["current"] = BRURSPALN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'spimfluln', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'spimfluln',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"spimfluln->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brurspaln(self, hint):
        assert self._state.get("current") == BRURSPALN, \
            f"flelspult.brurspaln: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brurspaln', 2:
                self._state["current"] = CLARPRORGLORR
                self._state["trig"]    = "hint:2"
            case 'brurspaln', 0:
                self._state["current"] = CLELFLALKRANR
                self._state["trig"]    = "hint:0"
            case 'brurspaln', _:
                self._state["current"] = FLORVARDRUR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brurspaln', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brurspaln',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brurspaln->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _florvardrur(self, hint):
        assert self._state.get("current") == FLORVARDRUR, \
            f"flelspult.florvardrur: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'florvardrur', 2:
                self._state["current"] = CLARPRORGLORR
                self._state["trig"]    = "hint:2"
            case 'florvardrur', _:
                self._state["current"] = CLELFLALKRANR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'florvardrur', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'florvardrur',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"florvardrur->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _clelflalkranr(self, hint):
        assert self._state.get("current") == CLELFLALKRANR, \
            f"flelspult.clelflalkranr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'clelflalkranr', 2:
                self._state["current"] = CLARPRORGLORR
                self._state["trig"]    = "hint:2"
            case 'clelflalkranr', 1:
                self._state["current"] = TRURGRALSPAN
                self._state["trig"]    = "hint:1"
            case 'clelflalkranr', _:
                self._state["current"] = FLEXSPORGREN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'clelflalkranr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'clelflalkranr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"clelflalkranr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _flexsporgren(self, hint):
        assert self._state.get("current") == FLEXSPORGREN, \
            f"flelspult.flexsporgren: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'flexsporgren', 2:
                self._state["current"] = CLARPRORGLORR
                self._state["trig"]    = "hint:2"
            case 'flexsporgren', _:
                self._state["current"] = TRURGRALSPAN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'flexsporgren', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'flexsporgren',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"flexsporgren->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _trurgralspan(self, hint):
        assert self._state.get("current") == TRURGRALSPAN, \
            f"flelspult.trurgralspan: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'trurgralspan', 2:
                self._state["current"] = CLARPRORGLORR
                self._state["trig"]    = "hint:2"
            case 'trurgralspan', 0:
                self._state["current"] = KRANGREXGROS
                self._state["trig"]    = "hint:0"
            case 'trurgralspan', _:
                self._state["current"] = DRENDREXPRULK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'trurgralspan', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'trurgralspan',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"trurgralspan->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _drendrexprulk(self, hint):
        assert self._state.get("current") == DRENDREXPRULK, \
            f"flelspult.drendrexprulk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'drendrexprulk', 2:
                self._state["current"] = CLARPRORGLORR
                self._state["trig"]    = "hint:2"
            case 'drendrexprulk', _:
                self._state["current"] = GRELSPALL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'drendrexprulk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'drendrexprulk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"drendrexprulk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _grelspall(self, hint):
        assert self._state.get("current") == GRELSPALL, \
            f"flelspult.grelspall: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'grelspall', 2:
                self._state["current"] = CLARPRORGLORR
                self._state["trig"]    = "hint:2"
            case 'grelspall', _:
                self._state["current"] = PRONPRULKRIM
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'grelspall', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'grelspall',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"grelspall->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _pronprulkrim(self, hint):
        assert self._state.get("current") == PRONPRULKRIM, \
            f"flelspult.pronprulkrim: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'pronprulkrim', 2:
                self._state["current"] = CLARPRORGLORR
                self._state["trig"]    = "hint:2"
            case 'pronprulkrim', 1:
                self._state["current"] = KRANGREXGROS
                self._state["trig"]    = "hint:1"
            case 'pronprulkrim', _:
                self._state["current"] = STEXTRAL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'pronprulkrim', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'pronprulkrim',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"pronprulkrim->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _stextral(self, hint):
        assert self._state.get("current") == STEXTRAL, \
            f"flelspult.stextral: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'stextral', 2:
                self._state["current"] = CLARPRORGLORR
                self._state["trig"]    = "hint:2"
            case 'stextral', 1:
                self._state["current"] = KRANGREXGROS
                self._state["trig"]    = "hint:1"
            case 'stextral', _:
                self._state["current"] = PRONSKON
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'stextral', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'stextral',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"stextral->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _pronskon(self, hint):
        assert self._state.get("current") == PRONSKON, \
            f"flelspult.pronskon: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'pronskon', 2:
                self._state["current"] = CLARPRORGLORR
                self._state["trig"]    = "hint:2"
            case 'pronskon', 0:
                self._state["current"] = KRIXGRURBRIXX
                self._state["trig"]    = "hint:0"
            case 'pronskon', _:
                self._state["current"] = PRALTREXL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'pronskon', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'pronskon',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"pronskon->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _praltrexl(self, hint):
        assert self._state.get("current") == PRALTREXL, \
            f"flelspult.praltrexl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'praltrexl', 2:
                self._state["current"] = CLARPRORGLORR
                self._state["trig"]    = "hint:2"
            case 'praltrexl', 1:
                self._state["current"] = DRAXSKURN
                self._state["trig"]    = "hint:1"
            case 'praltrexl', _:
                self._state["current"] = KRIXGRURBRIXX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'praltrexl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'praltrexl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"praltrexl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _krixgrurbrixx(self, hint):
        assert self._state.get("current") == KRIXGRURBRIXX, \
            f"flelspult.krixgrurbrixx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'krixgrurbrixx', 2:
                self._state["current"] = CLARPRORGLORR
                self._state["trig"]    = "hint:2"
            case 'krixgrurbrixx', _:
                self._state["current"] = DRAXSKURN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'krixgrurbrixx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'krixgrurbrixx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"krixgrurbrixx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _draxskurn(self, hint):
        assert self._state.get("current") == DRAXSKURN, \
            f"flelspult.draxskurn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'draxskurn', 2:
                self._state["current"] = CLARPRORGLORR
                self._state["trig"]    = "hint:2"
            case 'draxskurn', _:
                self._state["current"] = PRENSLUR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'draxskurn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'draxskurn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"draxskurn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _prenslur(self, hint):
        assert self._state.get("current") == PRENSLUR, \
            f"flelspult.prenslur: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'prenslur', 2:
                self._state["current"] = CLARPRORGLORR
                self._state["trig"]    = "hint:2"
            case 'prenslur', _:
                self._state["current"] = KRORKROSCLUR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'prenslur', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'prenslur',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"prenslur->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _krorkrosclur(self, hint):
        assert self._state.get("current") == KRORKROSCLUR, \
            f"flelspult.krorkrosclur: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'krorkrosclur', 2:
                self._state["current"] = CLARPRORGLORR
                self._state["trig"]    = "hint:2"
            case 'krorkrosclur', _:
                self._state["current"] = CLARVULK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'krorkrosclur', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'krorkrosclur',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"krorkrosclur->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _clarvulk(self, hint):
        assert self._state.get("current") == CLARVULK, \
            f"flelspult.clarvulk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'clarvulk', 2:
                self._state["current"] = CLARPRORGLORR
                self._state["trig"]    = "hint:2"
            case 'clarvulk', _:
                self._state["current"] = BRIMSTUR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'clarvulk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'clarvulk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"clarvulk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brimstur(self, hint):
        assert self._state.get("current") == BRIMSTUR, \
            f"flelspult.brimstur: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brimstur', 2:
                self._state["current"] = CLARPRORGLORR
                self._state["trig"]    = "hint:2"
            case 'brimstur', _:
                self._state["current"] = BLEXBLAXGLURX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brimstur', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brimstur',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brimstur->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blexblaxglurx(self, hint):
        assert self._state.get("current") == BLEXBLAXGLURX, \
            f"flelspult.blexblaxglurx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blexblaxglurx', 2:
                self._state["current"] = CLARPRORGLORR
                self._state["trig"]    = "hint:2"
            case 'blexblaxglurx', 1:
                self._state["current"] = KROSBLURSPOR
                self._state["trig"]    = "hint:1"
            case 'blexblaxglurx', _:
                self._state["current"] = PRIMBRARGLAX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blexblaxglurx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blexblaxglurx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blexblaxglurx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _primbrarglax(self, hint):
        assert self._state.get("current") == PRIMBRARGLAX, \
            f"flelspult.primbrarglax: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'primbrarglax', 2:
                self._state["current"] = CLARPRORGLORR
                self._state["trig"]    = "hint:2"
            case 'primbrarglax', _:
                self._state["current"] = KROSBLURSPOR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'primbrarglax', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'primbrarglax',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"primbrarglax->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _krosblurspor(self, hint):
        assert self._state.get("current") == KROSBLURSPOR, \
            f"flelspult.krosblurspor: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'krosblurspor', 2:
                self._state["current"] = CLARPRORGLORR
                self._state["trig"]    = "hint:2"
            case 'krosblurspor', _:
                self._state["current"] = PRARSKEN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'krosblurspor', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'krosblurspor',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"krosblurspor->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _prarsken(self, hint):
        assert self._state.get("current") == PRARSKEN, \
            f"flelspult.prarsken: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'prarsken', 2:
                self._state["current"] = CLARPRORGLORR
                self._state["trig"]    = "hint:2"
            case 'prarsken', _:
                self._state["current"] = CLOSFLOST
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'prarsken', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'prarsken',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"prarsken->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _closflost(self, hint):
        assert self._state.get("current") == CLOSFLOST, \
            f"flelspult.closflost: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'closflost', 2:
                self._state["current"] = CLARPRORGLORR
                self._state["trig"]    = "hint:2"
            case 'closflost', _:
                self._state["current"] = STARSLEXR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'closflost', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'closflost',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"closflost->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _starslexr(self, hint):
        assert self._state.get("current") == STARSLEXR, \
            f"flelspult.starslexr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'starslexr', 2:
                self._state["current"] = CLARPRORGLORR
                self._state["trig"]    = "hint:2"
            case 'starslexr', _:
                self._state["current"] = SLIXSKAR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'starslexr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'starslexr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"starslexr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slixskar(self, hint):
        assert self._state.get("current") == SLIXSKAR, \
            f"flelspult.slixskar: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slixskar', 2:
                self._state["current"] = CLARPRORGLORR
                self._state["trig"]    = "hint:2"
            case 'slixskar', 0:
                self._state["current"] = GRIXVEN
                self._state["trig"]    = "hint:0"
            case 'slixskar', _:
                self._state["current"] = TRANTREXR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slixskar', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slixskar',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slixskar->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _trantrexr(self, hint):
        assert self._state.get("current") == TRANTREXR, \
            f"flelspult.trantrexr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'trantrexr', 2:
                self._state["current"] = CLARPRORGLORR
                self._state["trig"]    = "hint:2"
            case 'trantrexr', 1:
                self._state["current"] = GLORKRANSTOSX
                self._state["trig"]    = "hint:1"
            case 'trantrexr', _:
                self._state["current"] = GRIXVEN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'trantrexr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'trantrexr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"trantrexr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _grixven(self, hint):
        assert self._state.get("current") == GRIXVEN, \
            f"flelspult.grixven: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'grixven', 2:
                self._state["current"] = CLARPRORGLORR
                self._state["trig"]    = "hint:2"
            case 'grixven', 1:
                self._state["current"] = KRANGREXGROS
                self._state["trig"]    = "hint:1"
            case 'grixven', _:
                self._state["current"] = GLORKRANSTOSX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'grixven', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'grixven',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"grixven->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glorkranstosx(self, hint):
        assert self._state.get("current") == GLORKRANSTOSX, \
            f"flelspult.glorkranstosx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glorkranstosx', 2:
                self._state["current"] = CLARPRORGLORR
                self._state["trig"]    = "hint:2"
            case 'glorkranstosx', _:
                self._state["current"] = BRIMVELVAXX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glorkranstosx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glorkranstosx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glorkranstosx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brimvelvaxx(self, hint):
        assert self._state.get("current") == BRIMVELVAXX, \
            f"flelspult.brimvelvaxx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brimvelvaxx', 2:
                self._state["current"] = CLARPRORGLORR
                self._state["trig"]    = "hint:2"
            case 'brimvelvaxx', _:
                self._state["current"] = DRURSTIXSTELR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brimvelvaxx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brimvelvaxx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brimvelvaxx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _drurstixstelr(self, hint):
        assert self._state.get("current") == DRURSTIXSTELR, \
            f"flelspult.drurstixstelr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'drurstixstelr', 2:
                self._state["current"] = CLARPRORGLORR
                self._state["trig"]    = "hint:2"
            case 'drurstixstelr', _:
                self._state["current"] = DRELSKARSPEXN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'drurstixstelr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'drurstixstelr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"drurstixstelr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _drelskarspexn(self, hint):
        assert self._state.get("current") == DRELSKARSPEXN, \
            f"flelspult.drelskarspexn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'drelskarspexn', 2:
                self._state["current"] = CLARPRORGLORR
                self._state["trig"]    = "hint:2"
            case 'drelskarspexn', 1:
                self._state["current"] = KRANGREXGROS
                self._state["trig"]    = "hint:1"
            case 'drelskarspexn', _:
                self._state["current"] = CLORSTULL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'drelskarspexn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'drelskarspexn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"drelskarspexn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _clorstull(self, hint):
        assert self._state.get("current") == CLORSTULL, \
            f"flelspult.clorstull: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'clorstull', 2:
                self._state["current"] = CLARPRORGLORR
                self._state["trig"]    = "hint:2"
            case 'clorstull', _:
                self._state["current"] = SPULKRAL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'clorstull', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'clorstull',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"clorstull->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _spulkral(self, hint):
        assert self._state.get("current") == SPULKRAL, \
            f"flelspult.spulkral: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'spulkral', 2:
                self._state["current"] = CLARPRORGLORR
                self._state["trig"]    = "hint:2"
            case 'spulkral', _:
                self._state["current"] = DREXFLEXGLEX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'spulkral', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'spulkral',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"spulkral->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _drexflexglex(self, hint):
        assert self._state.get("current") == DREXFLEXGLEX, \
            f"flelspult.drexflexglex: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'drexflexglex', 2:
                self._state["current"] = CLARPRORGLORR
                self._state["trig"]    = "hint:2"
            case 'drexflexglex', _:
                self._state["current"] = SKARVALTRENT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'drexflexglex', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'drexflexglex',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"drexflexglex->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skarvaltrent(self, hint):
        assert self._state.get("current") == SKARVALTRENT, \
            f"flelspult.skarvaltrent: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skarvaltrent', 2:
                self._state["current"] = CLARPRORGLORR
                self._state["trig"]    = "hint:2"
            case 'skarvaltrent', _:
                self._state["current"] = GLELGRIXCLAL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skarvaltrent', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skarvaltrent',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skarvaltrent->{_to}", _xid_val)
        self._state["cycle"] += 1

    def invoke(self, hint=None, span=None, caller=None, ctx=None, cycle=0):
        if ctx is None: ctx = {}

        self._state = {"current": PRELTRENSKAL, "ctx": ctx,
                        "span": span, "caller": caller,
                        "trig": "auto", "cycle": cycle}
        _dispatch = {
            PRELTRENSKAL: self._preltrenskal,
            SKONVAXSPAXN: self._skonvaxspaxn,
            KRALBRIX: self._kralbrix,
            SKEXGRELGLAX: self._skexgrelglax,
            SKEXGLOSSPIM: self._skexglosspim,
            SPALSKONX: self._spalskonx,
            CLURSTENGRANX: self._clurstengranx,
            DRORCLALVEL: self._drorclalvel,
            TRULBRENL: self._trulbrenl,
            GLIMSPELSLANN: self._glimspelslann,
            PRELSTAR: self._prelstar,
            SPARTRAXBLURL: self._spartraxblurl,
            DRAXPRALSPARL: self._draxpralsparl,
            BLULSPANL: self._blulspanl,
            GLORGLAXT: self._glorglaxt,
            BRONTRORN: self._brontrorn,
            FLEXSKAL: self._flexskal,
            TROSCLANR: self._trosclanr,
            SKENSPUL: self._skenspul,
            STELTRANGROR: self._steltrangror,
            SKONSLENDRUL: self._skonslendrul,
            TRIMTREXL: self._trimtrexl,
            BLENGLORDREX: self._blenglordrex,
            SLURGREN: self._slurgren,
            BLELKRAXN: self._blelkraxn,
            GLURPRELK: self._glurprelk,
            BRURSPURSPAR: self._brurspurspar,
            SKALGRORBRELK: self._skalgrorbrelk,
            GLAXSPANGREXR: self._glaxspangrexr,
            VANGROSSTEL: self._vangrosstel,
            SPIMFLULN: self._spimfluln,
            BRURSPALN: self._brurspaln,
            FLORVARDRUR: self._florvardrur,
            CLELFLALKRANR: self._clelflalkranr,
            FLEXSPORGREN: self._flexsporgren,
            TRURGRALSPAN: self._trurgralspan,
            DRENDREXPRULK: self._drendrexprulk,
            GRELSPALL: self._grelspall,
            PRONPRULKRIM: self._pronprulkrim,
            STEXTRAL: self._stextral,
            PRONSKON: self._pronskon,
            PRALTREXL: self._praltrexl,
            KRIXGRURBRIXX: self._krixgrurbrixx,
            DRAXSKURN: self._draxskurn,
            PRENSLUR: self._prenslur,
            KRORKROSCLUR: self._krorkrosclur,
            CLARVULK: self._clarvulk,
            BRIMSTUR: self._brimstur,
            BLEXBLAXGLURX: self._blexblaxglurx,
            PRIMBRARGLAX: self._primbrarglax,
            KROSBLURSPOR: self._krosblurspor,
            PRARSKEN: self._prarsken,
            CLOSFLOST: self._closflost,
            STARSLEXR: self._starslexr,
            SLIXSKAR: self._slixskar,
            TRANTREXR: self._trantrexr,
            GRIXVEN: self._grixven,
            GLORKRANSTOSX: self._glorkranstosx,
            BRIMVELVAXX: self._brimvelvaxx,
            DRURSTIXSTELR: self._drurstixstelr,
            DRELSKARSPEXN: self._drelskarspexn,
            CLORSTULL: self._clorstull,
            SPULKRAL: self._spulkral,
            DREXFLEXGLEX: self._drexflexglex,
            SKARVALTRENT: self._skarvaltrent,
        }
        while self._state["current"] not in _R and self._state["cycle"] - cycle < 8000:
            _dispatch[self._state["current"]](hint)
        _ret     = _R.get(self._state["current"], -1)
        _is_err  = self._state["current"] == CLARPRORGLORR
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
    return FlelspultFSM().invoke(hint=hint, span=span, caller=caller, ctx=ctx, cycle=cycle)
