from _log import _w as _emit, _xid

STANGRAX = 'stangrax'
GRORSLULT = 'grorslult'
GRIMSPAR = 'grimspar'
PRORSPULKRANX = 'prorspulkranx'
TRONFLON = 'tronflon'
PRAXSTIXDRANN = 'praxstixdrann'
KRANGRANTRELK = 'krangrantrelk'
BLELVIXKRALT = 'blelvixkralt'
SKELSTURTRARK = 'skelsturtrark'
DRALFLULKREN = 'dralflulkren'
KRARVAXBRARL = 'krarvaxbrarl'
KRURCLALK = 'krurclalk'
GLEXTRURSPIX = 'glextrurspix'
SKEXTREXPROS = 'skextrexpros'
BRAXDRUL = 'braxdrul'
FLIMSLEX = 'flimslex'
DRURBROR = 'drurbror'
BLURBLORT = 'blurblort'
BLOSPRORSKIMK = 'blosprorskimk'
DRULFLUL = 'drulflul'
FLARSLOSVUR = 'flarslosvur'
DRULKRORSPIM = 'drulkrorspim'
SLELSPURL = 'slelspurl'
SLULSTULPRAR = 'slulstulprar'
VORSTULKRIM = 'vorstulkrim'
VULSLENCLIXR = 'vulslenclixr'
SLENVENSKURL = 'slenvenskurl'
SKONPRELSKIXK = 'skonprelskixk'
GLOSGRAXCLUL = 'glosgraxclul'
BLARBLOSR = 'blarblosr'
SKANFLURKRELN = 'skanflurkreln'
KRURSKEXSLIMX = 'krurskexslimx'
SKANBLANL = 'skanblanl'
STENSKARK = 'stenskark'
PRANBLENR = 'pranblenr'
SKARSPEXX = 'skarspexx'
CLOSCLELSTANX = 'closclelstanx'
SKIXPRIX = 'skixprix'
PRULFLANSKUR = 'prulflanskur'
BRORPROR = 'brorpror'
BLAXSPUR = 'blaxspur'
TRULSKENBRAXL = 'trulskenbraxl'
SPELVEXPROS = 'spelvexpros'
STALDRARDREN = 'staldrardren'
SKAXSTALCLALX = 'skaxstalclalx'
SLANGLOS = 'slanglos'
PRENPRORCLAN = 'prenprorclan'
STULTRULCLAN = 'stultrulclan'
GRONCLIX = 'gronclix'
SLALGREXSTOSK = 'slalgrexstosk'
STELBROR = 'stelbror'
PRENPRELX = 'prenprelx'
TRURSLENGRAX = 'trurslengrax'
SKELBRANSKAL = 'skelbranskal'
BRIXFLEL = 'brixflel'
FLAXTRANSKOSX = 'flaxtranskosx'
TRIMSLARKREN = 'trimslarkren'
GLELBREN = 'glelbren'
GRALVANX = 'gralvanx'
SPURKRAR = 'spurkrar'
KRIMTRALR = 'krimtralr'
TRANVEXBLONT = 'tranvexblont'
GLOSFLIXVALK = 'glosflixvalk'
BLONSLENT = 'blonslent'
FLIMSTORDROSL = 'flimstordrosl'
CLEXSPEXGRUL = 'clexspexgrul'
GRARGRURR = 'grargrurr'
BLIXCLORT = 'blixclort'

_R = {
    CLEXSPEXGRUL: 0,
    GRARGRURR: 1,
    BLIXCLORT: 2,
}

_CTX_WRITES_KEY  = 'flurslex'
_CTX_WRITE_STATE = KRANGRANTRELK

class ClulgraxlFSM:
    def __init__(self):
        self._state = {}

    def _stangrax(self, hint):
        assert self._state.get("current") == STANGRAX, \
            f"clulgraxl.stangrax: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'stangrax', 2:
                self._state["current"] = BLIXCLORT
                self._state["trig"]    = "hint:2"
            case 'stangrax', _:
                self._state["current"] = GRORSLULT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'stangrax', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'stangrax',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"stangrax->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _grorslult(self, hint):
        assert self._state.get("current") == GRORSLULT, \
            f"clulgraxl.grorslult: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'grorslult', 2:
                self._state["current"] = BLIXCLORT
                self._state["trig"]    = "hint:2"
            case 'grorslult', 1:
                self._state["current"] = PRORSPULKRANX
                self._state["trig"]    = "hint:1"
            case 'grorslult', _:
                self._state["current"] = GRIMSPAR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'grorslult', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'grorslult',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"grorslult->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _grimspar(self, hint):
        assert self._state.get("current") == GRIMSPAR, \
            f"clulgraxl.grimspar: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'grimspar', 2:
                self._state["current"] = BLIXCLORT
                self._state["trig"]    = "hint:2"
            case 'grimspar', 1:
                self._state["current"] = TRONFLON
                self._state["trig"]    = "hint:1"
            case 'grimspar', _:
                self._state["current"] = PRORSPULKRANX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'grimspar', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'grimspar',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"grimspar->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _prorspulkranx(self, hint):
        assert self._state.get("current") == PRORSPULKRANX, \
            f"clulgraxl.prorspulkranx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'prorspulkranx', 2:
                self._state["current"] = BLIXCLORT
                self._state["trig"]    = "hint:2"
            case 'prorspulkranx', _:
                self._state["current"] = TRONFLON
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'prorspulkranx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'prorspulkranx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"prorspulkranx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _tronflon(self, hint):
        assert self._state.get("current") == TRONFLON, \
            f"clulgraxl.tronflon: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'tronflon', 2:
                self._state["current"] = BLIXCLORT
                self._state["trig"]    = "hint:2"
            case 'tronflon', 0:
                self._state["current"] = KRANGRANTRELK
                self._state["trig"]    = "hint:0"
            case 'tronflon', _:
                self._state["current"] = PRAXSTIXDRANN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'tronflon', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'tronflon',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"tronflon->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _praxstixdrann(self, hint):
        assert self._state.get("current") == PRAXSTIXDRANN, \
            f"clulgraxl.praxstixdrann: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'praxstixdrann', 2:
                self._state["current"] = BLIXCLORT
                self._state["trig"]    = "hint:2"
            case 'praxstixdrann', 0:
                self._state["current"] = GRARGRURR
                self._state["trig"]    = "hint:0"
            case 'praxstixdrann', _:
                self._state["current"] = KRANGRANTRELK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'praxstixdrann', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'praxstixdrann',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"praxstixdrann->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _krangrantrelk(self, hint):
        assert self._state.get("current") == KRANGRANTRELK, \
            f"clulgraxl.krangrantrelk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        _ctx_val_before = self._state["ctx"].get(_CTX_WRITES_KEY, 0)
        match self._state["current"], hint:
            case 'krangrantrelk', 2:
                self._state["current"] = BLIXCLORT
                self._state["trig"]    = "hint:2"
            case 'krangrantrelk', 0:
                self._state["current"] = GRARGRURR
                self._state["trig"]    = "hint:0"
            case 'krangrantrelk', _:
                self._state["current"] = BLELVIXKRALT
                self._state["trig"]    = "auto"
        _old = self._state["ctx"].get(_CTX_WRITES_KEY, 0)
        _inc = 2 if hint == 2 else 1
        self._state["ctx"][_CTX_WRITES_KEY] = _old + _inc
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'krangrantrelk', _to, _trig)
        _conds = {"hint_branch": _hint_branch,
                   "ctx_write": True,
                   "ctx_val_before": _ctx_val_before}
        _emit(self._state["cycle"], 1, __name__, 'krangrantrelk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"krangrantrelk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blelvixkralt(self, hint):
        assert self._state.get("current") == BLELVIXKRALT, \
            f"clulgraxl.blelvixkralt: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blelvixkralt', 2:
                self._state["current"] = BLIXCLORT
                self._state["trig"]    = "hint:2"
            case 'blelvixkralt', 0:
                self._state["current"] = DRALFLULKREN
                self._state["trig"]    = "hint:0"
            case 'blelvixkralt', _:
                self._state["current"] = SKELSTURTRARK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blelvixkralt', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blelvixkralt',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blelvixkralt->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skelsturtrark(self, hint):
        assert self._state.get("current") == SKELSTURTRARK, \
            f"clulgraxl.skelsturtrark: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skelsturtrark', 2:
                self._state["current"] = BLIXCLORT
                self._state["trig"]    = "hint:2"
            case 'skelsturtrark', _:
                self._state["current"] = DRALFLULKREN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skelsturtrark', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skelsturtrark',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skelsturtrark->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _dralflulkren(self, hint):
        assert self._state.get("current") == DRALFLULKREN, \
            f"clulgraxl.dralflulkren: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'dralflulkren', 2:
                self._state["current"] = BLIXCLORT
                self._state["trig"]    = "hint:2"
            case 'dralflulkren', _:
                self._state["current"] = KRARVAXBRARL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'dralflulkren', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'dralflulkren',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"dralflulkren->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _krarvaxbrarl(self, hint):
        assert self._state.get("current") == KRARVAXBRARL, \
            f"clulgraxl.krarvaxbrarl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'krarvaxbrarl', 2:
                self._state["current"] = BLIXCLORT
                self._state["trig"]    = "hint:2"
            case 'krarvaxbrarl', 0:
                self._state["current"] = GRARGRURR
                self._state["trig"]    = "hint:0"
            case 'krarvaxbrarl', _:
                self._state["current"] = KRURCLALK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'krarvaxbrarl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'krarvaxbrarl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"krarvaxbrarl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _krurclalk(self, hint):
        assert self._state.get("current") == KRURCLALK, \
            f"clulgraxl.krurclalk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'krurclalk', 2:
                self._state["current"] = BLIXCLORT
                self._state["trig"]    = "hint:2"
            case 'krurclalk', _:
                self._state["current"] = GLEXTRURSPIX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'krurclalk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'krurclalk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"krurclalk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glextrurspix(self, hint):
        assert self._state.get("current") == GLEXTRURSPIX, \
            f"clulgraxl.glextrurspix: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glextrurspix', 2:
                self._state["current"] = BLIXCLORT
                self._state["trig"]    = "hint:2"
            case 'glextrurspix', _:
                self._state["current"] = SKEXTREXPROS
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glextrurspix', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glextrurspix',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glextrurspix->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skextrexpros(self, hint):
        assert self._state.get("current") == SKEXTREXPROS, \
            f"clulgraxl.skextrexpros: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skextrexpros', 2:
                self._state["current"] = BLIXCLORT
                self._state["trig"]    = "hint:2"
            case 'skextrexpros', 0:
                self._state["current"] = FLIMSLEX
                self._state["trig"]    = "hint:0"
            case 'skextrexpros', _:
                self._state["current"] = BRAXDRUL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skextrexpros', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skextrexpros',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skextrexpros->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _braxdrul(self, hint):
        assert self._state.get("current") == BRAXDRUL, \
            f"clulgraxl.braxdrul: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'braxdrul', 2:
                self._state["current"] = BLIXCLORT
                self._state["trig"]    = "hint:2"
            case 'braxdrul', 0:
                self._state["current"] = GRARGRURR
                self._state["trig"]    = "hint:0"
            case 'braxdrul', _:
                self._state["current"] = FLIMSLEX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'braxdrul', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'braxdrul',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"braxdrul->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _flimslex(self, hint):
        assert self._state.get("current") == FLIMSLEX, \
            f"clulgraxl.flimslex: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'flimslex', 2:
                self._state["current"] = BLIXCLORT
                self._state["trig"]    = "hint:2"
            case 'flimslex', 0:
                self._state["current"] = GRARGRURR
                self._state["trig"]    = "hint:0"
            case 'flimslex', _:
                self._state["current"] = DRURBROR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'flimslex', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'flimslex',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"flimslex->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _drurbror(self, hint):
        assert self._state.get("current") == DRURBROR, \
            f"clulgraxl.drurbror: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'drurbror', 2:
                self._state["current"] = BLIXCLORT
                self._state["trig"]    = "hint:2"
            case 'drurbror', _:
                self._state["current"] = BLURBLORT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'drurbror', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'drurbror',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"drurbror->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blurblort(self, hint):
        assert self._state.get("current") == BLURBLORT, \
            f"clulgraxl.blurblort: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blurblort', 2:
                self._state["current"] = BLIXCLORT
                self._state["trig"]    = "hint:2"
            case 'blurblort', _:
                self._state["current"] = BLOSPRORSKIMK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blurblort', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blurblort',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blurblort->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blosprorskimk(self, hint):
        assert self._state.get("current") == BLOSPRORSKIMK, \
            f"clulgraxl.blosprorskimk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blosprorskimk', 2:
                self._state["current"] = BLIXCLORT
                self._state["trig"]    = "hint:2"
            case 'blosprorskimk', 1:
                self._state["current"] = GRARGRURR
                self._state["trig"]    = "hint:1"
            case 'blosprorskimk', _:
                self._state["current"] = DRULFLUL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blosprorskimk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blosprorskimk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blosprorskimk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _drulflul(self, hint):
        assert self._state.get("current") == DRULFLUL, \
            f"clulgraxl.drulflul: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'drulflul', 2:
                self._state["current"] = BLIXCLORT
                self._state["trig"]    = "hint:2"
            case 'drulflul', 1:
                self._state["current"] = DRULKRORSPIM
                self._state["trig"]    = "hint:1"
            case 'drulflul', _:
                self._state["current"] = FLARSLOSVUR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'drulflul', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'drulflul',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"drulflul->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _flarslosvur(self, hint):
        assert self._state.get("current") == FLARSLOSVUR, \
            f"clulgraxl.flarslosvur: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'flarslosvur', 2:
                self._state["current"] = BLIXCLORT
                self._state["trig"]    = "hint:2"
            case 'flarslosvur', _:
                self._state["current"] = DRULKRORSPIM
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'flarslosvur', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'flarslosvur',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"flarslosvur->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _drulkrorspim(self, hint):
        assert self._state.get("current") == DRULKRORSPIM, \
            f"clulgraxl.drulkrorspim: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'drulkrorspim', 2:
                self._state["current"] = BLIXCLORT
                self._state["trig"]    = "hint:2"
            case 'drulkrorspim', 0:
                self._state["current"] = SLULSTULPRAR
                self._state["trig"]    = "hint:0"
            case 'drulkrorspim', _:
                self._state["current"] = SLELSPURL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'drulkrorspim', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'drulkrorspim',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"drulkrorspim->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slelspurl(self, hint):
        assert self._state.get("current") == SLELSPURL, \
            f"clulgraxl.slelspurl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slelspurl', 2:
                self._state["current"] = BLIXCLORT
                self._state["trig"]    = "hint:2"
            case 'slelspurl', 0:
                self._state["current"] = VORSTULKRIM
                self._state["trig"]    = "hint:0"
            case 'slelspurl', _:
                self._state["current"] = SLULSTULPRAR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slelspurl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slelspurl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slelspurl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slulstulprar(self, hint):
        assert self._state.get("current") == SLULSTULPRAR, \
            f"clulgraxl.slulstulprar: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slulstulprar', 2:
                self._state["current"] = BLIXCLORT
                self._state["trig"]    = "hint:2"
            case 'slulstulprar', _:
                self._state["current"] = VORSTULKRIM
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slulstulprar', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slulstulprar',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slulstulprar->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _vorstulkrim(self, hint):
        assert self._state.get("current") == VORSTULKRIM, \
            f"clulgraxl.vorstulkrim: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'vorstulkrim', 2:
                self._state["current"] = BLIXCLORT
                self._state["trig"]    = "hint:2"
            case 'vorstulkrim', _:
                self._state["current"] = VULSLENCLIXR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'vorstulkrim', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'vorstulkrim',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"vorstulkrim->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _vulslenclixr(self, hint):
        assert self._state.get("current") == VULSLENCLIXR, \
            f"clulgraxl.vulslenclixr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'vulslenclixr', 2:
                self._state["current"] = BLIXCLORT
                self._state["trig"]    = "hint:2"
            case 'vulslenclixr', 0:
                self._state["current"] = SKONPRELSKIXK
                self._state["trig"]    = "hint:0"
            case 'vulslenclixr', _:
                self._state["current"] = SLENVENSKURL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'vulslenclixr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'vulslenclixr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"vulslenclixr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slenvenskurl(self, hint):
        assert self._state.get("current") == SLENVENSKURL, \
            f"clulgraxl.slenvenskurl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slenvenskurl', 2:
                self._state["current"] = BLIXCLORT
                self._state["trig"]    = "hint:2"
            case 'slenvenskurl', _:
                self._state["current"] = SKONPRELSKIXK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slenvenskurl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slenvenskurl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slenvenskurl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skonprelskixk(self, hint):
        assert self._state.get("current") == SKONPRELSKIXK, \
            f"clulgraxl.skonprelskixk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skonprelskixk', 2:
                self._state["current"] = BLIXCLORT
                self._state["trig"]    = "hint:2"
            case 'skonprelskixk', 1:
                self._state["current"] = BLARBLOSR
                self._state["trig"]    = "hint:1"
            case 'skonprelskixk', _:
                self._state["current"] = GLOSGRAXCLUL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skonprelskixk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skonprelskixk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skonprelskixk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glosgraxclul(self, hint):
        assert self._state.get("current") == GLOSGRAXCLUL, \
            f"clulgraxl.glosgraxclul: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glosgraxclul', 2:
                self._state["current"] = BLIXCLORT
                self._state["trig"]    = "hint:2"
            case 'glosgraxclul', 1:
                self._state["current"] = GRARGRURR
                self._state["trig"]    = "hint:1"
            case 'glosgraxclul', _:
                self._state["current"] = BLARBLOSR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glosgraxclul', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glosgraxclul',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glosgraxclul->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blarblosr(self, hint):
        assert self._state.get("current") == BLARBLOSR, \
            f"clulgraxl.blarblosr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blarblosr', 2:
                self._state["current"] = BLIXCLORT
                self._state["trig"]    = "hint:2"
            case 'blarblosr', 0:
                self._state["current"] = KRURSKEXSLIMX
                self._state["trig"]    = "hint:0"
            case 'blarblosr', _:
                self._state["current"] = SKANFLURKRELN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blarblosr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blarblosr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blarblosr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skanflurkreln(self, hint):
        assert self._state.get("current") == SKANFLURKRELN, \
            f"clulgraxl.skanflurkreln: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skanflurkreln', 2:
                self._state["current"] = BLIXCLORT
                self._state["trig"]    = "hint:2"
            case 'skanflurkreln', _:
                self._state["current"] = KRURSKEXSLIMX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skanflurkreln', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skanflurkreln',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skanflurkreln->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _krurskexslimx(self, hint):
        assert self._state.get("current") == KRURSKEXSLIMX, \
            f"clulgraxl.krurskexslimx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'krurskexslimx', 2:
                self._state["current"] = BLIXCLORT
                self._state["trig"]    = "hint:2"
            case 'krurskexslimx', _:
                self._state["current"] = SKANBLANL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'krurskexslimx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'krurskexslimx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"krurskexslimx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skanblanl(self, hint):
        assert self._state.get("current") == SKANBLANL, \
            f"clulgraxl.skanblanl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skanblanl', 2:
                self._state["current"] = BLIXCLORT
                self._state["trig"]    = "hint:2"
            case 'skanblanl', 1:
                self._state["current"] = GRARGRURR
                self._state["trig"]    = "hint:1"
            case 'skanblanl', _:
                self._state["current"] = STENSKARK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skanblanl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skanblanl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skanblanl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _stenskark(self, hint):
        assert self._state.get("current") == STENSKARK, \
            f"clulgraxl.stenskark: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'stenskark', 2:
                self._state["current"] = BLIXCLORT
                self._state["trig"]    = "hint:2"
            case 'stenskark', _:
                self._state["current"] = PRANBLENR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'stenskark', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'stenskark',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"stenskark->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _pranblenr(self, hint):
        assert self._state.get("current") == PRANBLENR, \
            f"clulgraxl.pranblenr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'pranblenr', 2:
                self._state["current"] = BLIXCLORT
                self._state["trig"]    = "hint:2"
            case 'pranblenr', 0:
                self._state["current"] = CLOSCLELSTANX
                self._state["trig"]    = "hint:0"
            case 'pranblenr', _:
                self._state["current"] = SKARSPEXX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'pranblenr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'pranblenr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"pranblenr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skarspexx(self, hint):
        assert self._state.get("current") == SKARSPEXX, \
            f"clulgraxl.skarspexx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skarspexx', 2:
                self._state["current"] = BLIXCLORT
                self._state["trig"]    = "hint:2"
            case 'skarspexx', _:
                self._state["current"] = CLOSCLELSTANX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skarspexx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skarspexx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skarspexx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _closclelstanx(self, hint):
        assert self._state.get("current") == CLOSCLELSTANX, \
            f"clulgraxl.closclelstanx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'closclelstanx', 2:
                self._state["current"] = BLIXCLORT
                self._state["trig"]    = "hint:2"
            case 'closclelstanx', _:
                self._state["current"] = SKIXPRIX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'closclelstanx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'closclelstanx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"closclelstanx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skixprix(self, hint):
        assert self._state.get("current") == SKIXPRIX, \
            f"clulgraxl.skixprix: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skixprix', 2:
                self._state["current"] = BLIXCLORT
                self._state["trig"]    = "hint:2"
            case 'skixprix', 1:
                self._state["current"] = GRARGRURR
                self._state["trig"]    = "hint:1"
            case 'skixprix', _:
                self._state["current"] = PRULFLANSKUR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skixprix', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skixprix',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skixprix->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _prulflanskur(self, hint):
        assert self._state.get("current") == PRULFLANSKUR, \
            f"clulgraxl.prulflanskur: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'prulflanskur', 2:
                self._state["current"] = BLIXCLORT
                self._state["trig"]    = "hint:2"
            case 'prulflanskur', _:
                self._state["current"] = BRORPROR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'prulflanskur', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'prulflanskur',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"prulflanskur->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brorpror(self, hint):
        assert self._state.get("current") == BRORPROR, \
            f"clulgraxl.brorpror: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brorpror', 2:
                self._state["current"] = BLIXCLORT
                self._state["trig"]    = "hint:2"
            case 'brorpror', 0:
                self._state["current"] = GRARGRURR
                self._state["trig"]    = "hint:0"
            case 'brorpror', _:
                self._state["current"] = BLAXSPUR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brorpror', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brorpror',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brorpror->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blaxspur(self, hint):
        assert self._state.get("current") == BLAXSPUR, \
            f"clulgraxl.blaxspur: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blaxspur', 2:
                self._state["current"] = BLIXCLORT
                self._state["trig"]    = "hint:2"
            case 'blaxspur', _:
                self._state["current"] = TRULSKENBRAXL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blaxspur', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blaxspur',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blaxspur->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _trulskenbraxl(self, hint):
        assert self._state.get("current") == TRULSKENBRAXL, \
            f"clulgraxl.trulskenbraxl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'trulskenbraxl', 2:
                self._state["current"] = BLIXCLORT
                self._state["trig"]    = "hint:2"
            case 'trulskenbraxl', 1:
                self._state["current"] = GRARGRURR
                self._state["trig"]    = "hint:1"
            case 'trulskenbraxl', _:
                self._state["current"] = SPELVEXPROS
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'trulskenbraxl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'trulskenbraxl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"trulskenbraxl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _spelvexpros(self, hint):
        assert self._state.get("current") == SPELVEXPROS, \
            f"clulgraxl.spelvexpros: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'spelvexpros', 2:
                self._state["current"] = BLIXCLORT
                self._state["trig"]    = "hint:2"
            case 'spelvexpros', _:
                self._state["current"] = STALDRARDREN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'spelvexpros', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'spelvexpros',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"spelvexpros->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _staldrardren(self, hint):
        assert self._state.get("current") == STALDRARDREN, \
            f"clulgraxl.staldrardren: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'staldrardren', 2:
                self._state["current"] = BLIXCLORT
                self._state["trig"]    = "hint:2"
            case 'staldrardren', 1:
                self._state["current"] = GRARGRURR
                self._state["trig"]    = "hint:1"
            case 'staldrardren', _:
                self._state["current"] = SKAXSTALCLALX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'staldrardren', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'staldrardren',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"staldrardren->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skaxstalclalx(self, hint):
        assert self._state.get("current") == SKAXSTALCLALX, \
            f"clulgraxl.skaxstalclalx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skaxstalclalx', 2:
                self._state["current"] = BLIXCLORT
                self._state["trig"]    = "hint:2"
            case 'skaxstalclalx', _:
                self._state["current"] = SLANGLOS
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skaxstalclalx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skaxstalclalx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skaxstalclalx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slanglos(self, hint):
        assert self._state.get("current") == SLANGLOS, \
            f"clulgraxl.slanglos: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slanglos', 2:
                self._state["current"] = BLIXCLORT
                self._state["trig"]    = "hint:2"
            case 'slanglos', _:
                self._state["current"] = PRENPRORCLAN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slanglos', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slanglos',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slanglos->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _prenprorclan(self, hint):
        assert self._state.get("current") == PRENPRORCLAN, \
            f"clulgraxl.prenprorclan: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'prenprorclan', 2:
                self._state["current"] = BLIXCLORT
                self._state["trig"]    = "hint:2"
            case 'prenprorclan', _:
                self._state["current"] = STULTRULCLAN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'prenprorclan', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'prenprorclan',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"prenprorclan->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _stultrulclan(self, hint):
        assert self._state.get("current") == STULTRULCLAN, \
            f"clulgraxl.stultrulclan: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'stultrulclan', 2:
                self._state["current"] = BLIXCLORT
                self._state["trig"]    = "hint:2"
            case 'stultrulclan', 0:
                self._state["current"] = SLALGREXSTOSK
                self._state["trig"]    = "hint:0"
            case 'stultrulclan', _:
                self._state["current"] = GRONCLIX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'stultrulclan', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'stultrulclan',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"stultrulclan->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _gronclix(self, hint):
        assert self._state.get("current") == GRONCLIX, \
            f"clulgraxl.gronclix: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'gronclix', 2:
                self._state["current"] = BLIXCLORT
                self._state["trig"]    = "hint:2"
            case 'gronclix', 1:
                self._state["current"] = GRARGRURR
                self._state["trig"]    = "hint:1"
            case 'gronclix', _:
                self._state["current"] = SLALGREXSTOSK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'gronclix', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'gronclix',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"gronclix->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slalgrexstosk(self, hint):
        assert self._state.get("current") == SLALGREXSTOSK, \
            f"clulgraxl.slalgrexstosk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slalgrexstosk', 2:
                self._state["current"] = BLIXCLORT
                self._state["trig"]    = "hint:2"
            case 'slalgrexstosk', 1:
                self._state["current"] = GRARGRURR
                self._state["trig"]    = "hint:1"
            case 'slalgrexstosk', _:
                self._state["current"] = STELBROR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slalgrexstosk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slalgrexstosk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slalgrexstosk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _stelbror(self, hint):
        assert self._state.get("current") == STELBROR, \
            f"clulgraxl.stelbror: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'stelbror', 2:
                self._state["current"] = BLIXCLORT
                self._state["trig"]    = "hint:2"
            case 'stelbror', _:
                self._state["current"] = PRENPRELX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'stelbror', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'stelbror',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"stelbror->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _prenprelx(self, hint):
        assert self._state.get("current") == PRENPRELX, \
            f"clulgraxl.prenprelx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'prenprelx', 2:
                self._state["current"] = BLIXCLORT
                self._state["trig"]    = "hint:2"
            case 'prenprelx', _:
                self._state["current"] = TRURSLENGRAX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'prenprelx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'prenprelx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"prenprelx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _trurslengrax(self, hint):
        assert self._state.get("current") == TRURSLENGRAX, \
            f"clulgraxl.trurslengrax: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'trurslengrax', 2:
                self._state["current"] = BLIXCLORT
                self._state["trig"]    = "hint:2"
            case 'trurslengrax', _:
                self._state["current"] = SKELBRANSKAL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'trurslengrax', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'trurslengrax',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"trurslengrax->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skelbranskal(self, hint):
        assert self._state.get("current") == SKELBRANSKAL, \
            f"clulgraxl.skelbranskal: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skelbranskal', 2:
                self._state["current"] = BLIXCLORT
                self._state["trig"]    = "hint:2"
            case 'skelbranskal', _:
                self._state["current"] = BRIXFLEL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skelbranskal', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skelbranskal',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skelbranskal->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brixflel(self, hint):
        assert self._state.get("current") == BRIXFLEL, \
            f"clulgraxl.brixflel: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brixflel', 2:
                self._state["current"] = BLIXCLORT
                self._state["trig"]    = "hint:2"
            case 'brixflel', _:
                self._state["current"] = FLAXTRANSKOSX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brixflel', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brixflel',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brixflel->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _flaxtranskosx(self, hint):
        assert self._state.get("current") == FLAXTRANSKOSX, \
            f"clulgraxl.flaxtranskosx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'flaxtranskosx', 2:
                self._state["current"] = BLIXCLORT
                self._state["trig"]    = "hint:2"
            case 'flaxtranskosx', 1:
                self._state["current"] = GLELBREN
                self._state["trig"]    = "hint:1"
            case 'flaxtranskosx', _:
                self._state["current"] = TRIMSLARKREN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'flaxtranskosx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'flaxtranskosx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"flaxtranskosx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _trimslarkren(self, hint):
        assert self._state.get("current") == TRIMSLARKREN, \
            f"clulgraxl.trimslarkren: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'trimslarkren', 2:
                self._state["current"] = BLIXCLORT
                self._state["trig"]    = "hint:2"
            case 'trimslarkren', _:
                self._state["current"] = GLELBREN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'trimslarkren', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'trimslarkren',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"trimslarkren->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glelbren(self, hint):
        assert self._state.get("current") == GLELBREN, \
            f"clulgraxl.glelbren: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glelbren', 2:
                self._state["current"] = BLIXCLORT
                self._state["trig"]    = "hint:2"
            case 'glelbren', 0:
                self._state["current"] = GRARGRURR
                self._state["trig"]    = "hint:0"
            case 'glelbren', _:
                self._state["current"] = GRALVANX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glelbren', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glelbren',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glelbren->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _gralvanx(self, hint):
        assert self._state.get("current") == GRALVANX, \
            f"clulgraxl.gralvanx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'gralvanx', 2:
                self._state["current"] = BLIXCLORT
                self._state["trig"]    = "hint:2"
            case 'gralvanx', _:
                self._state["current"] = SPURKRAR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'gralvanx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'gralvanx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"gralvanx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _spurkrar(self, hint):
        assert self._state.get("current") == SPURKRAR, \
            f"clulgraxl.spurkrar: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'spurkrar', 2:
                self._state["current"] = BLIXCLORT
                self._state["trig"]    = "hint:2"
            case 'spurkrar', 0:
                self._state["current"] = GRARGRURR
                self._state["trig"]    = "hint:0"
            case 'spurkrar', _:
                self._state["current"] = KRIMTRALR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'spurkrar', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'spurkrar',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"spurkrar->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _krimtralr(self, hint):
        assert self._state.get("current") == KRIMTRALR, \
            f"clulgraxl.krimtralr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'krimtralr', 2:
                self._state["current"] = BLIXCLORT
                self._state["trig"]    = "hint:2"
            case 'krimtralr', _:
                self._state["current"] = TRANVEXBLONT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'krimtralr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'krimtralr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"krimtralr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _tranvexblont(self, hint):
        assert self._state.get("current") == TRANVEXBLONT, \
            f"clulgraxl.tranvexblont: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'tranvexblont', 2:
                self._state["current"] = BLIXCLORT
                self._state["trig"]    = "hint:2"
            case 'tranvexblont', _:
                self._state["current"] = GLOSFLIXVALK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'tranvexblont', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'tranvexblont',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"tranvexblont->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glosflixvalk(self, hint):
        assert self._state.get("current") == GLOSFLIXVALK, \
            f"clulgraxl.glosflixvalk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glosflixvalk', 2:
                self._state["current"] = BLIXCLORT
                self._state["trig"]    = "hint:2"
            case 'glosflixvalk', _:
                self._state["current"] = BLONSLENT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glosflixvalk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glosflixvalk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glosflixvalk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blonslent(self, hint):
        assert self._state.get("current") == BLONSLENT, \
            f"clulgraxl.blonslent: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blonslent', 2:
                self._state["current"] = BLIXCLORT
                self._state["trig"]    = "hint:2"
            case 'blonslent', 0:
                self._state["current"] = GRARGRURR
                self._state["trig"]    = "hint:0"
            case 'blonslent', _:
                self._state["current"] = FLIMSTORDROSL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blonslent', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blonslent',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blonslent->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _flimstordrosl(self, hint):
        assert self._state.get("current") == FLIMSTORDROSL, \
            f"clulgraxl.flimstordrosl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'flimstordrosl', 2:
                self._state["current"] = BLIXCLORT
                self._state["trig"]    = "hint:2"
            case 'flimstordrosl', 1:
                self._state["current"] = GRARGRURR
                self._state["trig"]    = "hint:1"
            case 'flimstordrosl', _:
                self._state["current"] = CLEXSPEXGRUL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'flimstordrosl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'flimstordrosl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"flimstordrosl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def invoke(self, hint=None, span=None, caller=None, ctx=None, cycle=0):
        if ctx is None: ctx = {}

        self._state = {"current": STANGRAX, "ctx": ctx,
                        "span": span, "caller": caller,
                        "trig": "auto", "cycle": cycle}
        _dispatch = {
            STANGRAX: self._stangrax,
            GRORSLULT: self._grorslult,
            GRIMSPAR: self._grimspar,
            PRORSPULKRANX: self._prorspulkranx,
            TRONFLON: self._tronflon,
            PRAXSTIXDRANN: self._praxstixdrann,
            KRANGRANTRELK: self._krangrantrelk,
            BLELVIXKRALT: self._blelvixkralt,
            SKELSTURTRARK: self._skelsturtrark,
            DRALFLULKREN: self._dralflulkren,
            KRARVAXBRARL: self._krarvaxbrarl,
            KRURCLALK: self._krurclalk,
            GLEXTRURSPIX: self._glextrurspix,
            SKEXTREXPROS: self._skextrexpros,
            BRAXDRUL: self._braxdrul,
            FLIMSLEX: self._flimslex,
            DRURBROR: self._drurbror,
            BLURBLORT: self._blurblort,
            BLOSPRORSKIMK: self._blosprorskimk,
            DRULFLUL: self._drulflul,
            FLARSLOSVUR: self._flarslosvur,
            DRULKRORSPIM: self._drulkrorspim,
            SLELSPURL: self._slelspurl,
            SLULSTULPRAR: self._slulstulprar,
            VORSTULKRIM: self._vorstulkrim,
            VULSLENCLIXR: self._vulslenclixr,
            SLENVENSKURL: self._slenvenskurl,
            SKONPRELSKIXK: self._skonprelskixk,
            GLOSGRAXCLUL: self._glosgraxclul,
            BLARBLOSR: self._blarblosr,
            SKANFLURKRELN: self._skanflurkreln,
            KRURSKEXSLIMX: self._krurskexslimx,
            SKANBLANL: self._skanblanl,
            STENSKARK: self._stenskark,
            PRANBLENR: self._pranblenr,
            SKARSPEXX: self._skarspexx,
            CLOSCLELSTANX: self._closclelstanx,
            SKIXPRIX: self._skixprix,
            PRULFLANSKUR: self._prulflanskur,
            BRORPROR: self._brorpror,
            BLAXSPUR: self._blaxspur,
            TRULSKENBRAXL: self._trulskenbraxl,
            SPELVEXPROS: self._spelvexpros,
            STALDRARDREN: self._staldrardren,
            SKAXSTALCLALX: self._skaxstalclalx,
            SLANGLOS: self._slanglos,
            PRENPRORCLAN: self._prenprorclan,
            STULTRULCLAN: self._stultrulclan,
            GRONCLIX: self._gronclix,
            SLALGREXSTOSK: self._slalgrexstosk,
            STELBROR: self._stelbror,
            PRENPRELX: self._prenprelx,
            TRURSLENGRAX: self._trurslengrax,
            SKELBRANSKAL: self._skelbranskal,
            BRIXFLEL: self._brixflel,
            FLAXTRANSKOSX: self._flaxtranskosx,
            TRIMSLARKREN: self._trimslarkren,
            GLELBREN: self._glelbren,
            GRALVANX: self._gralvanx,
            SPURKRAR: self._spurkrar,
            KRIMTRALR: self._krimtralr,
            TRANVEXBLONT: self._tranvexblont,
            GLOSFLIXVALK: self._glosflixvalk,
            BLONSLENT: self._blonslent,
            FLIMSTORDROSL: self._flimstordrosl,
        }
        while self._state["current"] not in _R and self._state["cycle"] - cycle < 8000:
            _dispatch[self._state["current"]](hint)
        _ret     = _R.get(self._state["current"], -1)
        _is_err  = self._state["current"] == BLIXCLORT
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
    return ClulgraxlFSM().invoke(hint=hint, span=span, caller=caller, ctx=ctx, cycle=cycle)
