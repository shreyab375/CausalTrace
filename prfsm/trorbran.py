from _log import _w as _emit, _xid

VOSGLOR = 'vosglor'
DRARSLENKRAN = 'drarslenkran'
FLIMBRAX = 'flimbrax'
TRANGLAN = 'tranglan'
GLIMGRENVELN = 'glimgrenveln'
BLORGRAL = 'blorgral'
FLULSLEXSPIM = 'flulslexspim'
TRURCLURK = 'trurclurk'
FLURBRANSTENN = 'flurbranstenn'
BROSSLUL = 'brosslul'
SLENSKIML = 'slenskiml'
SLALSKANSKIX = 'slalskanskix'
TRAXVEXBLANR = 'traxvexblanr'
TRANTRAN = 'trantran'
FLOSSLEXTRANK = 'flosslextrank'
GLIMPRANBRIMK = 'glimpranbrimk'
GLELSKIXSLUL = 'glelskixslul'
KREXPRIXVALL = 'krexprixvall'
BRANDROR = 'brandror'
KRALSTALSTULR = 'kralstalstulr'
CLORGREL = 'clorgrel'
STEXCLEXPRELX = 'stexclexprelx'
SKANBLEL = 'skanblel'
KRELGLARGRELN = 'krelglargreln'
FLELBRALSPAX = 'flelbralspax'
GLELGRORTRURL = 'glelgrortrurl'
SLIMGLUR = 'slimglur'
KRORGRORK = 'krorgrork'
BRURPRENR = 'brurprenr'
DRURFLURGLULX = 'drurflurglulx'
GLIMCLONDRONK = 'glimclondronk'
FLURBRULGRALT = 'flurbrulgralt'
BRIXVIMK = 'brixvimk'
PRENTRONSKAN = 'prentronskan'
DRORSKELSPEX = 'drorskelspex'
SPORBRAR = 'sporbrar'
DRIMGLANGLOS = 'drimglanglos'
STEXSKULT = 'stexskult'
STALKRONR = 'stalkronr'
STENSKUL = 'stenskul'
DRARSTONSTULL = 'drarstonstull'
KRONDROSKREX = 'krondroskrex'
GRELDRAX = 'greldrax'
SLELKRIMBLIM = 'slelkrimblim'
VAXSTOS = 'vaxstos'
GLONFLIM = 'glonflim'
SLEXPRAXDRUL = 'slexpraxdrul'
STULDRALK = 'stuldralk'
KRELDRIMR = 'kreldrimr'
BRURGRULL = 'brurgrull'
SPEXSLURL = 'spexslurl'
KRALSLIM = 'kralslim'
PRURVARK = 'prurvark'
KRONSKOS = 'kronskos'
TRANPREX = 'tranprex'
BREXBLANN = 'brexblann'
BLOSFLAXGRORN = 'blosflaxgrorn'
SLIMSTAXBLIM = 'slimstaxblim'
CLULSTAL = 'clulstal'
DRULSPIX = 'drulspix'
SPORSKAL = 'sporskal'
KRONVIX = 'kronvix'
CLELPRULX = 'clelprulx'
DRIMVALBLONK = 'drimvalblonk'
TRELGRIXX = 'trelgrixx'
SKENGRULN = 'skengruln'
BRALBLOSPRORL = 'bralblosprorl'
SKALSKALR = 'skalskalr'

_R = {
    SKENGRULN: 0,
    BRALBLOSPRORL: 1,
    SKALSKALR: 2,
}

_CTX_READS_KEY = 'flurslex'
_CTX_THRESHOLD = 16

class TrorbranFSM:
    def __init__(self):
        self._state = {}

    def _vosglor(self, hint):
        assert self._state.get("current") == VOSGLOR, \
            f"trorbran.vosglor: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'vosglor', 2:
                self._state["current"] = SKALSKALR
                self._state["trig"]    = "hint:2"
            case 'vosglor', _:
                self._state["current"] = DRARSLENKRAN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'vosglor', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'vosglor',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"vosglor->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _drarslenkran(self, hint):
        assert self._state.get("current") == DRARSLENKRAN, \
            f"trorbran.drarslenkran: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'drarslenkran', 2:
                self._state["current"] = SKALSKALR
                self._state["trig"]    = "hint:2"
            case 'drarslenkran', 1:
                self._state["current"] = TRANGLAN
                self._state["trig"]    = "hint:1"
            case 'drarslenkran', _:
                self._state["current"] = FLIMBRAX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'drarslenkran', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'drarslenkran',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"drarslenkran->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _flimbrax(self, hint):
        assert self._state.get("current") == FLIMBRAX, \
            f"trorbran.flimbrax: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'flimbrax', 2:
                self._state["current"] = SKALSKALR
                self._state["trig"]    = "hint:2"
            case 'flimbrax', 0:
                self._state["current"] = GLIMGRENVELN
                self._state["trig"]    = "hint:0"
            case 'flimbrax', _:
                self._state["current"] = TRANGLAN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'flimbrax', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'flimbrax',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"flimbrax->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _tranglan(self, hint):
        assert self._state.get("current") == TRANGLAN, \
            f"trorbran.tranglan: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'tranglan', 2:
                self._state["current"] = SKALSKALR
                self._state["trig"]    = "hint:2"
            case 'tranglan', _:
                self._state["current"] = GLIMGRENVELN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'tranglan', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'tranglan',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"tranglan->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glimgrenveln(self, hint):
        assert self._state.get("current") == GLIMGRENVELN, \
            f"trorbran.glimgrenveln: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glimgrenveln', 2:
                self._state["current"] = SKALSKALR
                self._state["trig"]    = "hint:2"
            case 'glimgrenveln', _:
                self._state["current"] = BLORGRAL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glimgrenveln', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glimgrenveln',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glimgrenveln->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blorgral(self, hint):
        assert self._state.get("current") == BLORGRAL, \
            f"trorbran.blorgral: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blorgral', 2:
                self._state["current"] = SKALSKALR
                self._state["trig"]    = "hint:2"
            case 'blorgral', _:
                self._state["current"] = FLULSLEXSPIM
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blorgral', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blorgral',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blorgral->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _flulslexspim(self, hint):
        assert self._state.get("current") == FLULSLEXSPIM, \
            f"trorbran.flulslexspim: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'flulslexspim', 2:
                self._state["current"] = SKALSKALR
                self._state["trig"]    = "hint:2"
            case 'flulslexspim', _:
                self._state["current"] = TRURCLURK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'flulslexspim', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'flulslexspim',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"flulslexspim->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _trurclurk(self, hint):
        assert self._state.get("current") == TRURCLURK, \
            f"trorbran.trurclurk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'trurclurk', 2:
                self._state["current"] = SKALSKALR
                self._state["trig"]    = "hint:2"
            case 'trurclurk', 0:
                self._state["current"] = BRALBLOSPRORL
                self._state["trig"]    = "hint:0"
            case 'trurclurk', _:
                self._state["current"] = FLURBRANSTENN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'trurclurk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'trurclurk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"trurclurk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _flurbranstenn(self, hint):
        assert self._state.get("current") == FLURBRANSTENN, \
            f"trorbran.flurbranstenn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'flurbranstenn', 2:
                self._state["current"] = SKALSKALR
                self._state["trig"]    = "hint:2"
            case 'flurbranstenn', 1:
                self._state["current"] = SLENSKIML
                self._state["trig"]    = "hint:1"
            case 'flurbranstenn', _:
                self._state["current"] = BROSSLUL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'flurbranstenn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'flurbranstenn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"flurbranstenn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brosslul(self, hint):
        assert self._state.get("current") == BROSSLUL, \
            f"trorbran.brosslul: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brosslul', 2:
                self._state["current"] = SKALSKALR
                self._state["trig"]    = "hint:2"
            case 'brosslul', 0:
                self._state["current"] = BRALBLOSPRORL
                self._state["trig"]    = "hint:0"
            case 'brosslul', _:
                self._state["current"] = SLENSKIML
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brosslul', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brosslul',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brosslul->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slenskiml(self, hint):
        assert self._state.get("current") == SLENSKIML, \
            f"trorbran.slenskiml: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slenskiml', 2:
                self._state["current"] = SKALSKALR
                self._state["trig"]    = "hint:2"
            case 'slenskiml', _:
                self._state["current"] = SLALSKANSKIX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slenskiml', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slenskiml',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slenskiml->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slalskanskix(self, hint):
        assert self._state.get("current") == SLALSKANSKIX, \
            f"trorbran.slalskanskix: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slalskanskix', 2:
                self._state["current"] = SKALSKALR
                self._state["trig"]    = "hint:2"
            case 'slalskanskix', _:
                self._state["current"] = TRAXVEXBLANR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slalskanskix', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slalskanskix',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slalskanskix->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _traxvexblanr(self, hint):
        assert self._state.get("current") == TRAXVEXBLANR, \
            f"trorbran.traxvexblanr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'traxvexblanr', 2:
                self._state["current"] = SKALSKALR
                self._state["trig"]    = "hint:2"
            case 'traxvexblanr', _:
                self._state["current"] = TRANTRAN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'traxvexblanr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'traxvexblanr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"traxvexblanr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _trantran(self, hint):
        assert self._state.get("current") == TRANTRAN, \
            f"trorbran.trantran: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'trantran', 2:
                self._state["current"] = SKALSKALR
                self._state["trig"]    = "hint:2"
            case 'trantran', 0:
                self._state["current"] = BRALBLOSPRORL
                self._state["trig"]    = "hint:0"
            case 'trantran', _:
                self._state["current"] = FLOSSLEXTRANK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'trantran', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'trantran',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"trantran->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _flosslextrank(self, hint):
        assert self._state.get("current") == FLOSSLEXTRANK, \
            f"trorbran.flosslextrank: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'flosslextrank', 2:
                self._state["current"] = SKALSKALR
                self._state["trig"]    = "hint:2"
            case 'flosslextrank', 1:
                self._state["current"] = BRALBLOSPRORL
                self._state["trig"]    = "hint:1"
            case 'flosslextrank', _:
                self._state["current"] = GLIMPRANBRIMK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'flosslextrank', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'flosslextrank',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"flosslextrank->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glimpranbrimk(self, hint):
        assert self._state.get("current") == GLIMPRANBRIMK, \
            f"trorbran.glimpranbrimk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glimpranbrimk', 2:
                self._state["current"] = SKALSKALR
                self._state["trig"]    = "hint:2"
            case 'glimpranbrimk', _:
                self._state["current"] = GLELSKIXSLUL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glimpranbrimk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glimpranbrimk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glimpranbrimk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glelskixslul(self, hint):
        assert self._state.get("current") == GLELSKIXSLUL, \
            f"trorbran.glelskixslul: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glelskixslul', 2:
                self._state["current"] = SKALSKALR
                self._state["trig"]    = "hint:2"
            case 'glelskixslul', 1:
                self._state["current"] = BRANDROR
                self._state["trig"]    = "hint:1"
            case 'glelskixslul', _:
                self._state["current"] = KREXPRIXVALL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glelskixslul', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glelskixslul',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glelskixslul->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _krexprixvall(self, hint):
        assert self._state.get("current") == KREXPRIXVALL, \
            f"trorbran.krexprixvall: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'krexprixvall', 2:
                self._state["current"] = SKALSKALR
                self._state["trig"]    = "hint:2"
            case 'krexprixvall', 0:
                self._state["current"] = KRALSTALSTULR
                self._state["trig"]    = "hint:0"
            case 'krexprixvall', _:
                self._state["current"] = BRANDROR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'krexprixvall', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'krexprixvall',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"krexprixvall->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brandror(self, hint):
        assert self._state.get("current") == BRANDROR, \
            f"trorbran.brandror: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brandror', 2:
                self._state["current"] = SKALSKALR
                self._state["trig"]    = "hint:2"
            case 'brandror', _:
                self._state["current"] = KRALSTALSTULR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brandror', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brandror',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brandror->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _kralstalstulr(self, hint):
        assert self._state.get("current") == KRALSTALSTULR, \
            f"trorbran.kralstalstulr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'kralstalstulr', 2:
                self._state["current"] = SKALSKALR
                self._state["trig"]    = "hint:2"
            case 'kralstalstulr', _:
                self._state["current"] = CLORGREL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'kralstalstulr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'kralstalstulr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"kralstalstulr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _clorgrel(self, hint):
        assert self._state.get("current") == CLORGREL, \
            f"trorbran.clorgrel: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'clorgrel', 2:
                self._state["current"] = SKALSKALR
                self._state["trig"]    = "hint:2"
            case 'clorgrel', 0:
                self._state["current"] = SKANBLEL
                self._state["trig"]    = "hint:0"
            case 'clorgrel', _:
                self._state["current"] = STEXCLEXPRELX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'clorgrel', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'clorgrel',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"clorgrel->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _stexclexprelx(self, hint):
        assert self._state.get("current") == STEXCLEXPRELX, \
            f"trorbran.stexclexprelx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'stexclexprelx', 2:
                self._state["current"] = SKALSKALR
                self._state["trig"]    = "hint:2"
            case 'stexclexprelx', 1:
                self._state["current"] = BRALBLOSPRORL
                self._state["trig"]    = "hint:1"
            case 'stexclexprelx', _:
                self._state["current"] = SKANBLEL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'stexclexprelx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'stexclexprelx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"stexclexprelx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skanblel(self, hint):
        assert self._state.get("current") == SKANBLEL, \
            f"trorbran.skanblel: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skanblel', 2:
                self._state["current"] = SKALSKALR
                self._state["trig"]    = "hint:2"
            case 'skanblel', _:
                self._state["current"] = KRELGLARGRELN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skanblel', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skanblel',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skanblel->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _krelglargreln(self, hint):
        assert self._state.get("current") == KRELGLARGRELN, \
            f"trorbran.krelglargreln: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'krelglargreln', 2:
                self._state["current"] = SKALSKALR
                self._state["trig"]    = "hint:2"
            case 'krelglargreln', 1:
                self._state["current"] = BRALBLOSPRORL
                self._state["trig"]    = "hint:1"
            case 'krelglargreln', _:
                self._state["current"] = FLELBRALSPAX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'krelglargreln', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'krelglargreln',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"krelglargreln->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _flelbralspax(self, hint):
        assert self._state.get("current") == FLELBRALSPAX, \
            f"trorbran.flelbralspax: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'flelbralspax', 2:
                self._state["current"] = SKALSKALR
                self._state["trig"]    = "hint:2"
            case 'flelbralspax', 0:
                self._state["current"] = SLIMGLUR
                self._state["trig"]    = "hint:0"
            case 'flelbralspax', _:
                self._state["current"] = GLELGRORTRURL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'flelbralspax', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'flelbralspax',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"flelbralspax->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glelgrortrurl(self, hint):
        assert self._state.get("current") == GLELGRORTRURL, \
            f"trorbran.glelgrortrurl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glelgrortrurl', 2:
                self._state["current"] = SKALSKALR
                self._state["trig"]    = "hint:2"
            case 'glelgrortrurl', _:
                self._state["current"] = SLIMGLUR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glelgrortrurl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glelgrortrurl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glelgrortrurl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slimglur(self, hint):
        assert self._state.get("current") == SLIMGLUR, \
            f"trorbran.slimglur: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slimglur', 2:
                self._state["current"] = SKALSKALR
                self._state["trig"]    = "hint:2"
            case 'slimglur', 0:
                self._state["current"] = BRURPRENR
                self._state["trig"]    = "hint:0"
            case 'slimglur', _:
                self._state["current"] = KRORGRORK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slimglur', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slimglur',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slimglur->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _krorgrork(self, hint):
        assert self._state.get("current") == KRORGRORK, \
            f"trorbran.krorgrork: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'krorgrork', 2:
                self._state["current"] = SKALSKALR
                self._state["trig"]    = "hint:2"
            case 'krorgrork', _:
                self._state["current"] = BRURPRENR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'krorgrork', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'krorgrork',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"krorgrork->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brurprenr(self, hint):
        assert self._state.get("current") == BRURPRENR, \
            f"trorbran.brurprenr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brurprenr', 2:
                self._state["current"] = SKALSKALR
                self._state["trig"]    = "hint:2"
            case 'brurprenr', _:
                self._state["current"] = DRURFLURGLULX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brurprenr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brurprenr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brurprenr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _drurflurglulx(self, hint):
        assert self._state.get("current") == DRURFLURGLULX, \
            f"trorbran.drurflurglulx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'drurflurglulx', 2:
                self._state["current"] = SKALSKALR
                self._state["trig"]    = "hint:2"
            case 'drurflurglulx', 0:
                self._state["current"] = BRALBLOSPRORL
                self._state["trig"]    = "hint:0"
            case 'drurflurglulx', _:
                self._state["current"] = GLIMCLONDRONK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'drurflurglulx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'drurflurglulx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"drurflurglulx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glimclondronk(self, hint):
        assert self._state.get("current") == GLIMCLONDRONK, \
            f"trorbran.glimclondronk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glimclondronk', 2:
                self._state["current"] = SKALSKALR
                self._state["trig"]    = "hint:2"
            case 'glimclondronk', _:
                self._state["current"] = FLURBRULGRALT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glimclondronk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glimclondronk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glimclondronk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _flurbrulgralt(self, hint):
        assert self._state.get("current") == FLURBRULGRALT, \
            f"trorbran.flurbrulgralt: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'flurbrulgralt', 2:
                self._state["current"] = SKALSKALR
                self._state["trig"]    = "hint:2"
            case 'flurbrulgralt', _:
                self._state["current"] = BRIXVIMK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'flurbrulgralt', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'flurbrulgralt',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"flurbrulgralt->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brixvimk(self, hint):
        assert self._state.get("current") == BRIXVIMK, \
            f"trorbran.brixvimk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brixvimk', 2:
                self._state["current"] = SKALSKALR
                self._state["trig"]    = "hint:2"
            case 'brixvimk', 1:
                self._state["current"] = DRORSKELSPEX
                self._state["trig"]    = "hint:1"
            case 'brixvimk', _:
                self._state["current"] = PRENTRONSKAN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brixvimk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brixvimk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brixvimk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _prentronskan(self, hint):
        assert self._state.get("current") == PRENTRONSKAN, \
            f"trorbran.prentronskan: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'prentronskan', 2:
                self._state["current"] = SKALSKALR
                self._state["trig"]    = "hint:2"
            case 'prentronskan', 0:
                self._state["current"] = SPORBRAR
                self._state["trig"]    = "hint:0"
            case 'prentronskan', _:
                self._state["current"] = DRORSKELSPEX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'prentronskan', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'prentronskan',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"prentronskan->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _drorskelspex(self, hint):
        assert self._state.get("current") == DRORSKELSPEX, \
            f"trorbran.drorskelspex: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'drorskelspex', 2:
                self._state["current"] = SKALSKALR
                self._state["trig"]    = "hint:2"
            case 'drorskelspex', _:
                self._state["current"] = SPORBRAR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'drorskelspex', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'drorskelspex',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"drorskelspex->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _sporbrar(self, hint):
        assert self._state.get("current") == SPORBRAR, \
            f"trorbran.sporbrar: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'sporbrar', 2:
                self._state["current"] = SKALSKALR
                self._state["trig"]    = "hint:2"
            case 'sporbrar', _:
                self._state["current"] = DRIMGLANGLOS
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'sporbrar', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'sporbrar',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"sporbrar->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _drimglanglos(self, hint):
        assert self._state.get("current") == DRIMGLANGLOS, \
            f"trorbran.drimglanglos: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'drimglanglos', 2:
                self._state["current"] = SKALSKALR
                self._state["trig"]    = "hint:2"
            case 'drimglanglos', 1:
                self._state["current"] = STALKRONR
                self._state["trig"]    = "hint:1"
            case 'drimglanglos', _:
                self._state["current"] = STEXSKULT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'drimglanglos', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'drimglanglos',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"drimglanglos->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _stexskult(self, hint):
        assert self._state.get("current") == STEXSKULT, \
            f"trorbran.stexskult: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'stexskult', 2:
                self._state["current"] = SKALSKALR
                self._state["trig"]    = "hint:2"
            case 'stexskult', _:
                self._state["current"] = STALKRONR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'stexskult', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'stexskult',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"stexskult->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _stalkronr(self, hint):
        assert self._state.get("current") == STALKRONR, \
            f"trorbran.stalkronr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'stalkronr', 2:
                self._state["current"] = SKALSKALR
                self._state["trig"]    = "hint:2"
            case 'stalkronr', _:
                self._state["current"] = STENSKUL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'stalkronr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'stalkronr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"stalkronr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _stenskul(self, hint):
        assert self._state.get("current") == STENSKUL, \
            f"trorbran.stenskul: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'stenskul', 2:
                self._state["current"] = SKALSKALR
                self._state["trig"]    = "hint:2"
            case 'stenskul', _:
                self._state["current"] = DRARSTONSTULL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'stenskul', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'stenskul',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"stenskul->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _drarstonstull(self, hint):
        assert self._state.get("current") == DRARSTONSTULL, \
            f"trorbran.drarstonstull: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'drarstonstull', 2:
                self._state["current"] = SKALSKALR
                self._state["trig"]    = "hint:2"
            case 'drarstonstull', _:
                self._state["current"] = KRONDROSKREX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'drarstonstull', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'drarstonstull',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"drarstonstull->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _krondroskrex(self, hint):
        assert self._state.get("current") == KRONDROSKREX, \
            f"trorbran.krondroskrex: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'krondroskrex', 2:
                self._state["current"] = SKALSKALR
                self._state["trig"]    = "hint:2"
            case 'krondroskrex', 1:
                self._state["current"] = BRALBLOSPRORL
                self._state["trig"]    = "hint:1"
            case 'krondroskrex', _:
                self._state["current"] = GRELDRAX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'krondroskrex', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'krondroskrex',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"krondroskrex->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _greldrax(self, hint):
        assert self._state.get("current") == GRELDRAX, \
            f"trorbran.greldrax: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'greldrax', 2:
                self._state["current"] = SKALSKALR
                self._state["trig"]    = "hint:2"
            case 'greldrax', _:
                self._state["current"] = SLELKRIMBLIM
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'greldrax', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'greldrax',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"greldrax->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slelkrimblim(self, hint):
        assert self._state.get("current") == SLELKRIMBLIM, \
            f"trorbran.slelkrimblim: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slelkrimblim', 2:
                self._state["current"] = SKALSKALR
                self._state["trig"]    = "hint:2"
            case 'slelkrimblim', _:
                self._state["current"] = VAXSTOS
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slelkrimblim', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slelkrimblim',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slelkrimblim->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _vaxstos(self, hint):
        assert self._state.get("current") == VAXSTOS, \
            f"trorbran.vaxstos: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'vaxstos', 2:
                self._state["current"] = SKALSKALR
                self._state["trig"]    = "hint:2"
            case 'vaxstos', 1:
                self._state["current"] = BRALBLOSPRORL
                self._state["trig"]    = "hint:1"
            case 'vaxstos', _:
                self._state["current"] = GLONFLIM
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'vaxstos', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'vaxstos',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"vaxstos->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glonflim(self, hint):
        assert self._state.get("current") == GLONFLIM, \
            f"trorbran.glonflim: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glonflim', 2:
                self._state["current"] = SKALSKALR
                self._state["trig"]    = "hint:2"
            case 'glonflim', 0:
                self._state["current"] = BRALBLOSPRORL
                self._state["trig"]    = "hint:0"
            case 'glonflim', _:
                self._state["current"] = SLEXPRAXDRUL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glonflim', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glonflim',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glonflim->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slexpraxdrul(self, hint):
        assert self._state.get("current") == SLEXPRAXDRUL, \
            f"trorbran.slexpraxdrul: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slexpraxdrul', 2:
                self._state["current"] = SKALSKALR
                self._state["trig"]    = "hint:2"
            case 'slexpraxdrul', 1:
                self._state["current"] = KRELDRIMR
                self._state["trig"]    = "hint:1"
            case 'slexpraxdrul', _:
                self._state["current"] = STULDRALK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slexpraxdrul', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slexpraxdrul',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slexpraxdrul->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _stuldralk(self, hint):
        assert self._state.get("current") == STULDRALK, \
            f"trorbran.stuldralk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'stuldralk', 2:
                self._state["current"] = SKALSKALR
                self._state["trig"]    = "hint:2"
            case 'stuldralk', _:
                self._state["current"] = KRELDRIMR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'stuldralk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'stuldralk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"stuldralk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _kreldrimr(self, hint):
        assert self._state.get("current") == KRELDRIMR, \
            f"trorbran.kreldrimr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'kreldrimr', 2:
                self._state["current"] = SKALSKALR
                self._state["trig"]    = "hint:2"
            case 'kreldrimr', 0:
                self._state["current"] = SPEXSLURL
                self._state["trig"]    = "hint:0"
            case 'kreldrimr', _:
                self._state["current"] = BRURGRULL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'kreldrimr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'kreldrimr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"kreldrimr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brurgrull(self, hint):
        assert self._state.get("current") == BRURGRULL, \
            f"trorbran.brurgrull: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brurgrull', 2:
                self._state["current"] = SKALSKALR
                self._state["trig"]    = "hint:2"
            case 'brurgrull', 0:
                self._state["current"] = KRALSLIM
                self._state["trig"]    = "hint:0"
            case 'brurgrull', _:
                self._state["current"] = SPEXSLURL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brurgrull', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brurgrull',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brurgrull->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _spexslurl(self, hint):
        assert self._state.get("current") == SPEXSLURL, \
            f"trorbran.spexslurl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'spexslurl', 2:
                self._state["current"] = SKALSKALR
                self._state["trig"]    = "hint:2"
            case 'spexslurl', 0:
                self._state["current"] = PRURVARK
                self._state["trig"]    = "hint:0"
            case 'spexslurl', _:
                self._state["current"] = KRALSLIM
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'spexslurl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'spexslurl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"spexslurl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _kralslim(self, hint):
        assert self._state.get("current") == KRALSLIM, \
            f"trorbran.kralslim: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'kralslim', 2:
                self._state["current"] = SKALSKALR
                self._state["trig"]    = "hint:2"
            case 'kralslim', _:
                self._state["current"] = PRURVARK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'kralslim', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'kralslim',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"kralslim->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _prurvark(self, hint):
        assert self._state.get("current") == PRURVARK, \
            f"trorbran.prurvark: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'prurvark', 2:
                self._state["current"] = SKALSKALR
                self._state["trig"]    = "hint:2"
            case 'prurvark', _:
                self._state["current"] = KRONSKOS
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'prurvark', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'prurvark',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"prurvark->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _kronskos(self, hint):
        assert self._state.get("current") == KRONSKOS, \
            f"trorbran.kronskos: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'kronskos', 2:
                self._state["current"] = SKALSKALR
                self._state["trig"]    = "hint:2"
            case 'kronskos', 0:
                self._state["current"] = BREXBLANN
                self._state["trig"]    = "hint:0"
            case 'kronskos', _:
                self._state["current"] = TRANPREX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'kronskos', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'kronskos',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"kronskos->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _tranprex(self, hint):
        assert self._state.get("current") == TRANPREX, \
            f"trorbran.tranprex: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'tranprex', 2:
                self._state["current"] = SKALSKALR
                self._state["trig"]    = "hint:2"
            case 'tranprex', _:
                self._state["current"] = BREXBLANN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'tranprex', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'tranprex',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"tranprex->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brexblann(self, hint):
        assert self._state.get("current") == BREXBLANN, \
            f"trorbran.brexblann: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brexblann', 2:
                self._state["current"] = SKALSKALR
                self._state["trig"]    = "hint:2"
            case 'brexblann', 0:
                self._state["current"] = SLIMSTAXBLIM
                self._state["trig"]    = "hint:0"
            case 'brexblann', _:
                self._state["current"] = BLOSFLAXGRORN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brexblann', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brexblann',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brexblann->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blosflaxgrorn(self, hint):
        assert self._state.get("current") == BLOSFLAXGRORN, \
            f"trorbran.blosflaxgrorn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blosflaxgrorn', 2:
                self._state["current"] = SKALSKALR
                self._state["trig"]    = "hint:2"
            case 'blosflaxgrorn', 1:
                self._state["current"] = CLULSTAL
                self._state["trig"]    = "hint:1"
            case 'blosflaxgrorn', _:
                self._state["current"] = SLIMSTAXBLIM
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blosflaxgrorn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blosflaxgrorn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blosflaxgrorn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slimstaxblim(self, hint):
        assert self._state.get("current") == SLIMSTAXBLIM, \
            f"trorbran.slimstaxblim: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slimstaxblim', 2:
                self._state["current"] = SKALSKALR
                self._state["trig"]    = "hint:2"
            case 'slimstaxblim', _:
                self._state["current"] = CLULSTAL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slimstaxblim', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slimstaxblim',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slimstaxblim->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _clulstal(self, hint):
        assert self._state.get("current") == CLULSTAL, \
            f"trorbran.clulstal: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'clulstal', 2:
                self._state["current"] = SKALSKALR
                self._state["trig"]    = "hint:2"
            case 'clulstal', _:
                self._state["current"] = DRULSPIX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'clulstal', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'clulstal',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"clulstal->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _drulspix(self, hint):
        assert self._state.get("current") == DRULSPIX, \
            f"trorbran.drulspix: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'drulspix', 2:
                self._state["current"] = SKALSKALR
                self._state["trig"]    = "hint:2"
            case 'drulspix', _:
                self._state["current"] = SPORSKAL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'drulspix', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'drulspix',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"drulspix->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _sporskal(self, hint):
        assert self._state.get("current") == SPORSKAL, \
            f"trorbran.sporskal: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'sporskal', 2:
                self._state["current"] = SKALSKALR
                self._state["trig"]    = "hint:2"
            case 'sporskal', _:
                self._state["current"] = KRONVIX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'sporskal', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'sporskal',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"sporskal->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _kronvix(self, hint):
        assert self._state.get("current") == KRONVIX, \
            f"trorbran.kronvix: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'kronvix', 2:
                self._state["current"] = SKALSKALR
                self._state["trig"]    = "hint:2"
            case 'kronvix', 0:
                self._state["current"] = DRIMVALBLONK
                self._state["trig"]    = "hint:0"
            case 'kronvix', _:
                self._state["current"] = CLELPRULX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'kronvix', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'kronvix',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"kronvix->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _clelprulx(self, hint):
        assert self._state.get("current") == CLELPRULX, \
            f"trorbran.clelprulx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'clelprulx', 2:
                self._state["current"] = SKALSKALR
                self._state["trig"]    = "hint:2"
            case 'clelprulx', 1:
                self._state["current"] = TRELGRIXX
                self._state["trig"]    = "hint:1"
            case 'clelprulx', _:
                self._state["current"] = DRIMVALBLONK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'clelprulx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'clelprulx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"clelprulx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _drimvalblonk(self, hint):
        assert self._state.get("current") == DRIMVALBLONK, \
            f"trorbran.drimvalblonk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'drimvalblonk', 2:
                self._state["current"] = SKALSKALR
                self._state["trig"]    = "hint:2"
            case 'drimvalblonk', 1:
                self._state["current"] = BRALBLOSPRORL
                self._state["trig"]    = "hint:1"
            case 'drimvalblonk', _:
                self._state["current"] = TRELGRIXX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'drimvalblonk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'drimvalblonk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"drimvalblonk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _trelgrixx(self, hint):
        assert self._state.get("current") == TRELGRIXX, \
            f"trorbran.trelgrixx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'trelgrixx', 2:
                self._state["current"] = SKALSKALR
                self._state["trig"]    = "hint:2"
            case 'trelgrixx', _:
                self._state["current"] = SKENGRULN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'trelgrixx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'trelgrixx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"trelgrixx->{_to}", _xid_val)
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
            _xid_val = _xid(__name__, 'vosglor', "error", "assert_fail")
            _emit(cycle, 1, __name__, 'vosglor',
                   {"hint": hint, "span": span, "caller": caller},
                   dict(ctx), _conds,
                   "entry_blocked->error", _xid_val, assertion=_asrt)
            return 2, cycle + 1

        self._state = {"current": VOSGLOR, "ctx": ctx,
                        "span": span, "caller": caller,
                        "trig": "auto", "cycle": cycle}
        _dispatch = {
            VOSGLOR: self._vosglor,
            DRARSLENKRAN: self._drarslenkran,
            FLIMBRAX: self._flimbrax,
            TRANGLAN: self._tranglan,
            GLIMGRENVELN: self._glimgrenveln,
            BLORGRAL: self._blorgral,
            FLULSLEXSPIM: self._flulslexspim,
            TRURCLURK: self._trurclurk,
            FLURBRANSTENN: self._flurbranstenn,
            BROSSLUL: self._brosslul,
            SLENSKIML: self._slenskiml,
            SLALSKANSKIX: self._slalskanskix,
            TRAXVEXBLANR: self._traxvexblanr,
            TRANTRAN: self._trantran,
            FLOSSLEXTRANK: self._flosslextrank,
            GLIMPRANBRIMK: self._glimpranbrimk,
            GLELSKIXSLUL: self._glelskixslul,
            KREXPRIXVALL: self._krexprixvall,
            BRANDROR: self._brandror,
            KRALSTALSTULR: self._kralstalstulr,
            CLORGREL: self._clorgrel,
            STEXCLEXPRELX: self._stexclexprelx,
            SKANBLEL: self._skanblel,
            KRELGLARGRELN: self._krelglargreln,
            FLELBRALSPAX: self._flelbralspax,
            GLELGRORTRURL: self._glelgrortrurl,
            SLIMGLUR: self._slimglur,
            KRORGRORK: self._krorgrork,
            BRURPRENR: self._brurprenr,
            DRURFLURGLULX: self._drurflurglulx,
            GLIMCLONDRONK: self._glimclondronk,
            FLURBRULGRALT: self._flurbrulgralt,
            BRIXVIMK: self._brixvimk,
            PRENTRONSKAN: self._prentronskan,
            DRORSKELSPEX: self._drorskelspex,
            SPORBRAR: self._sporbrar,
            DRIMGLANGLOS: self._drimglanglos,
            STEXSKULT: self._stexskult,
            STALKRONR: self._stalkronr,
            STENSKUL: self._stenskul,
            DRARSTONSTULL: self._drarstonstull,
            KRONDROSKREX: self._krondroskrex,
            GRELDRAX: self._greldrax,
            SLELKRIMBLIM: self._slelkrimblim,
            VAXSTOS: self._vaxstos,
            GLONFLIM: self._glonflim,
            SLEXPRAXDRUL: self._slexpraxdrul,
            STULDRALK: self._stuldralk,
            KRELDRIMR: self._kreldrimr,
            BRURGRULL: self._brurgrull,
            SPEXSLURL: self._spexslurl,
            KRALSLIM: self._kralslim,
            PRURVARK: self._prurvark,
            KRONSKOS: self._kronskos,
            TRANPREX: self._tranprex,
            BREXBLANN: self._brexblann,
            BLOSFLAXGRORN: self._blosflaxgrorn,
            SLIMSTAXBLIM: self._slimstaxblim,
            CLULSTAL: self._clulstal,
            DRULSPIX: self._drulspix,
            SPORSKAL: self._sporskal,
            KRONVIX: self._kronvix,
            CLELPRULX: self._clelprulx,
            DRIMVALBLONK: self._drimvalblonk,
            TRELGRIXX: self._trelgrixx,
        }
        while self._state["current"] not in _R and self._state["cycle"] - cycle < 8000:
            _dispatch[self._state["current"]](hint)
        _ret     = _R.get(self._state["current"], -1)
        _is_err  = self._state["current"] == SKALSKALR
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
    return TrorbranFSM().invoke(hint=hint, span=span, caller=caller, ctx=ctx, cycle=cycle)
