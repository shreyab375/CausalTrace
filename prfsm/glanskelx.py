from _log import _w as _emit, _xid

DRORPRIMGRARK = 'drorprimgrark'
SLANTRIMSTAN = 'slantrimstan'
VANBLENTRORX = 'vanblentrorx'
FLARPRALBLUR = 'flarpralblur'
SLONSKIMKRIX = 'slonskimkrix'
STORDRANT = 'stordrant'
FLENDREN = 'flendren'
PRIXBLAXL = 'prixblaxl'
SLIXGLENR = 'slixglenr'
SKULVAR = 'skulvar'
TRANBRARX = 'tranbrarx'
SPOSDRELKREX = 'sposdrelkrex'
KRURBLEL = 'krurblel'
CLENTRIXBLEL = 'clentrixblel'
BRAXFLELBRANR = 'braxflelbranr'
SKELGRENSTOSK = 'skelgrenstosk'
BLONDRALPRURR = 'blondralprurr'
STONPRENX = 'stonprenx'
SPANKREXK = 'spankrexk'
GLANVIMGLIX = 'glanvimglix'
GRIMTROSKRULN = 'grimtroskruln'
CLURGLALT = 'clurglalt'
VARBLAXL = 'varblaxl'
SPENVURVENR = 'spenvurvenr'
CLOSKRULR = 'closkrulr'
KRELVEN = 'krelven'
TRELDRARR = 'treldrarr'
KROSSPURPRANR = 'krosspurpranr'
KRENPREXGRIM = 'krenprexgrim'
BRARCLOS = 'brarclos'
KRIXFLOR = 'krixflor'
BLALDRONR = 'blaldronr'
SLIMDRIXBLAXK = 'slimdrixblaxk'
GRONBRALSPEXL = 'gronbralspexl'
GRULGRALK = 'grulgralk'
CLURTRALX = 'clurtralx'
VORPRAN = 'vorpran'
KRULGRAN = 'krulgran'
SKENBLALSKOS = 'skenblalskos'
BRIXBRIMSTEXK = 'brixbrimstexk'
PRURFLENGRORR = 'prurflengrorr'
PRELPROSGRURT = 'prelprosgrurt'
TRALVEXKRELR = 'tralvexkrelr'
DREXCLAXL = 'drexclaxl'
BRULFLELSKEXN = 'brulflelskexn'
KROSPRIX = 'krosprix'
CLONGREX = 'clongrex'
SPOSFLEXN = 'sposflexn'
FLIXCLEXKRENK = 'flixclexkrenk'
PRALSKIMK = 'pralskimk'
FLIMTROST = 'flimtrost'
STULSLEXTRARX = 'stulslextrarx'
VELSTONFLALK = 'velstonflalk'
VURTRORX = 'vurtrorx'
TRURKRALN = 'trurkraln'
BLOSGRELL = 'blosgrell'
SLULDRON = 'sluldron'
BLARKRALL = 'blarkrall'
PRELFLAXK = 'prelflaxk'
BLALBRAXSKELN = 'blalbraxskeln'
KRELSLURSLONL = 'krelslurslonl'
TROSSLAXR = 'trosslaxr'
SPORSLONCLOS = 'sporslonclos'
BLEXDRELCLIM = 'blexdrelclim'
BLOSSKALBROS = 'blosskalbros'
TRANPRELSKURK = 'tranprelskurk'
SLAXPREXGRUL = 'slaxprexgrul'
GRELVELCLURN = 'grelvelclurn'

_R = {
    TRANPRELSKURK: 0,
    SLAXPREXGRUL: 1,
    GRELVELCLURN: 2,
}

_CTX_READS_KEY = 'flurslex'
_CTX_THRESHOLD = 16

class GlanskelxFSM:
    def __init__(self):
        self._state = {}

    def _drorprimgrark(self, hint):
        assert self._state.get("current") == DRORPRIMGRARK, \
            f"glanskelx.drorprimgrark: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'drorprimgrark', 2:
                self._state["current"] = GRELVELCLURN
                self._state["trig"]    = "hint:2"
            case 'drorprimgrark', 1:
                self._state["current"] = SLAXPREXGRUL
                self._state["trig"]    = "hint:1"
            case 'drorprimgrark', _:
                self._state["current"] = SLANTRIMSTAN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'drorprimgrark', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'drorprimgrark',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"drorprimgrark->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slantrimstan(self, hint):
        assert self._state.get("current") == SLANTRIMSTAN, \
            f"glanskelx.slantrimstan: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slantrimstan', 2:
                self._state["current"] = GRELVELCLURN
                self._state["trig"]    = "hint:2"
            case 'slantrimstan', 1:
                self._state["current"] = SLAXPREXGRUL
                self._state["trig"]    = "hint:1"
            case 'slantrimstan', _:
                self._state["current"] = VANBLENTRORX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slantrimstan', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slantrimstan',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slantrimstan->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _vanblentrorx(self, hint):
        assert self._state.get("current") == VANBLENTRORX, \
            f"glanskelx.vanblentrorx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'vanblentrorx', 2:
                self._state["current"] = GRELVELCLURN
                self._state["trig"]    = "hint:2"
            case 'vanblentrorx', _:
                self._state["current"] = FLARPRALBLUR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'vanblentrorx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'vanblentrorx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"vanblentrorx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _flarpralblur(self, hint):
        assert self._state.get("current") == FLARPRALBLUR, \
            f"glanskelx.flarpralblur: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'flarpralblur', 2:
                self._state["current"] = GRELVELCLURN
                self._state["trig"]    = "hint:2"
            case 'flarpralblur', _:
                self._state["current"] = SLONSKIMKRIX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'flarpralblur', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'flarpralblur',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"flarpralblur->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slonskimkrix(self, hint):
        assert self._state.get("current") == SLONSKIMKRIX, \
            f"glanskelx.slonskimkrix: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slonskimkrix', 2:
                self._state["current"] = GRELVELCLURN
                self._state["trig"]    = "hint:2"
            case 'slonskimkrix', _:
                self._state["current"] = STORDRANT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slonskimkrix', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slonskimkrix',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slonskimkrix->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _stordrant(self, hint):
        assert self._state.get("current") == STORDRANT, \
            f"glanskelx.stordrant: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'stordrant', 2:
                self._state["current"] = GRELVELCLURN
                self._state["trig"]    = "hint:2"
            case 'stordrant', 0:
                self._state["current"] = PRIXBLAXL
                self._state["trig"]    = "hint:0"
            case 'stordrant', _:
                self._state["current"] = FLENDREN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'stordrant', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'stordrant',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"stordrant->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _flendren(self, hint):
        assert self._state.get("current") == FLENDREN, \
            f"glanskelx.flendren: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'flendren', 2:
                self._state["current"] = GRELVELCLURN
                self._state["trig"]    = "hint:2"
            case 'flendren', _:
                self._state["current"] = PRIXBLAXL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'flendren', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'flendren',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"flendren->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _prixblaxl(self, hint):
        assert self._state.get("current") == PRIXBLAXL, \
            f"glanskelx.prixblaxl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'prixblaxl', 2:
                self._state["current"] = GRELVELCLURN
                self._state["trig"]    = "hint:2"
            case 'prixblaxl', 0:
                self._state["current"] = SLAXPREXGRUL
                self._state["trig"]    = "hint:0"
            case 'prixblaxl', _:
                self._state["current"] = SLIXGLENR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'prixblaxl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'prixblaxl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"prixblaxl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slixglenr(self, hint):
        assert self._state.get("current") == SLIXGLENR, \
            f"glanskelx.slixglenr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slixglenr', 2:
                self._state["current"] = GRELVELCLURN
                self._state["trig"]    = "hint:2"
            case 'slixglenr', _:
                self._state["current"] = SKULVAR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slixglenr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slixglenr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slixglenr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skulvar(self, hint):
        assert self._state.get("current") == SKULVAR, \
            f"glanskelx.skulvar: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skulvar', 2:
                self._state["current"] = GRELVELCLURN
                self._state["trig"]    = "hint:2"
            case 'skulvar', _:
                self._state["current"] = TRANBRARX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skulvar', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skulvar',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skulvar->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _tranbrarx(self, hint):
        assert self._state.get("current") == TRANBRARX, \
            f"glanskelx.tranbrarx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'tranbrarx', 2:
                self._state["current"] = GRELVELCLURN
                self._state["trig"]    = "hint:2"
            case 'tranbrarx', _:
                self._state["current"] = SPOSDRELKREX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'tranbrarx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'tranbrarx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"tranbrarx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _sposdrelkrex(self, hint):
        assert self._state.get("current") == SPOSDRELKREX, \
            f"glanskelx.sposdrelkrex: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'sposdrelkrex', 2:
                self._state["current"] = GRELVELCLURN
                self._state["trig"]    = "hint:2"
            case 'sposdrelkrex', _:
                self._state["current"] = KRURBLEL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'sposdrelkrex', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'sposdrelkrex',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"sposdrelkrex->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _krurblel(self, hint):
        assert self._state.get("current") == KRURBLEL, \
            f"glanskelx.krurblel: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'krurblel', 2:
                self._state["current"] = GRELVELCLURN
                self._state["trig"]    = "hint:2"
            case 'krurblel', _:
                self._state["current"] = CLENTRIXBLEL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'krurblel', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'krurblel',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"krurblel->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _clentrixblel(self, hint):
        assert self._state.get("current") == CLENTRIXBLEL, \
            f"glanskelx.clentrixblel: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'clentrixblel', 2:
                self._state["current"] = GRELVELCLURN
                self._state["trig"]    = "hint:2"
            case 'clentrixblel', 1:
                self._state["current"] = SLAXPREXGRUL
                self._state["trig"]    = "hint:1"
            case 'clentrixblel', _:
                self._state["current"] = BRAXFLELBRANR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'clentrixblel', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'clentrixblel',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"clentrixblel->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _braxflelbranr(self, hint):
        assert self._state.get("current") == BRAXFLELBRANR, \
            f"glanskelx.braxflelbranr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'braxflelbranr', 2:
                self._state["current"] = GRELVELCLURN
                self._state["trig"]    = "hint:2"
            case 'braxflelbranr', _:
                self._state["current"] = SKELGRENSTOSK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'braxflelbranr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'braxflelbranr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"braxflelbranr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skelgrenstosk(self, hint):
        assert self._state.get("current") == SKELGRENSTOSK, \
            f"glanskelx.skelgrenstosk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skelgrenstosk', 2:
                self._state["current"] = GRELVELCLURN
                self._state["trig"]    = "hint:2"
            case 'skelgrenstosk', _:
                self._state["current"] = BLONDRALPRURR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skelgrenstosk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skelgrenstosk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skelgrenstosk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blondralprurr(self, hint):
        assert self._state.get("current") == BLONDRALPRURR, \
            f"glanskelx.blondralprurr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blondralprurr', 2:
                self._state["current"] = GRELVELCLURN
                self._state["trig"]    = "hint:2"
            case 'blondralprurr', _:
                self._state["current"] = STONPRENX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blondralprurr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blondralprurr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blondralprurr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _stonprenx(self, hint):
        assert self._state.get("current") == STONPRENX, \
            f"glanskelx.stonprenx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'stonprenx', 2:
                self._state["current"] = GRELVELCLURN
                self._state["trig"]    = "hint:2"
            case 'stonprenx', _:
                self._state["current"] = SPANKREXK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'stonprenx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'stonprenx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"stonprenx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _spankrexk(self, hint):
        assert self._state.get("current") == SPANKREXK, \
            f"glanskelx.spankrexk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'spankrexk', 2:
                self._state["current"] = GRELVELCLURN
                self._state["trig"]    = "hint:2"
            case 'spankrexk', _:
                self._state["current"] = GLANVIMGLIX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'spankrexk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'spankrexk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"spankrexk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glanvimglix(self, hint):
        assert self._state.get("current") == GLANVIMGLIX, \
            f"glanskelx.glanvimglix: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glanvimglix', 2:
                self._state["current"] = GRELVELCLURN
                self._state["trig"]    = "hint:2"
            case 'glanvimglix', _:
                self._state["current"] = GRIMTROSKRULN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glanvimglix', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glanvimglix',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glanvimglix->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _grimtroskruln(self, hint):
        assert self._state.get("current") == GRIMTROSKRULN, \
            f"glanskelx.grimtroskruln: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'grimtroskruln', 2:
                self._state["current"] = GRELVELCLURN
                self._state["trig"]    = "hint:2"
            case 'grimtroskruln', _:
                self._state["current"] = CLURGLALT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'grimtroskruln', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'grimtroskruln',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"grimtroskruln->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _clurglalt(self, hint):
        assert self._state.get("current") == CLURGLALT, \
            f"glanskelx.clurglalt: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'clurglalt', 2:
                self._state["current"] = GRELVELCLURN
                self._state["trig"]    = "hint:2"
            case 'clurglalt', 0:
                self._state["current"] = SPENVURVENR
                self._state["trig"]    = "hint:0"
            case 'clurglalt', _:
                self._state["current"] = VARBLAXL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'clurglalt', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'clurglalt',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"clurglalt->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _varblaxl(self, hint):
        assert self._state.get("current") == VARBLAXL, \
            f"glanskelx.varblaxl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'varblaxl', 2:
                self._state["current"] = GRELVELCLURN
                self._state["trig"]    = "hint:2"
            case 'varblaxl', _:
                self._state["current"] = SPENVURVENR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'varblaxl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'varblaxl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"varblaxl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _spenvurvenr(self, hint):
        assert self._state.get("current") == SPENVURVENR, \
            f"glanskelx.spenvurvenr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'spenvurvenr', 2:
                self._state["current"] = GRELVELCLURN
                self._state["trig"]    = "hint:2"
            case 'spenvurvenr', 1:
                self._state["current"] = SLAXPREXGRUL
                self._state["trig"]    = "hint:1"
            case 'spenvurvenr', _:
                self._state["current"] = CLOSKRULR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'spenvurvenr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'spenvurvenr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"spenvurvenr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _closkrulr(self, hint):
        assert self._state.get("current") == CLOSKRULR, \
            f"glanskelx.closkrulr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'closkrulr', 2:
                self._state["current"] = GRELVELCLURN
                self._state["trig"]    = "hint:2"
            case 'closkrulr', _:
                self._state["current"] = KRELVEN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'closkrulr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'closkrulr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"closkrulr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _krelven(self, hint):
        assert self._state.get("current") == KRELVEN, \
            f"glanskelx.krelven: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'krelven', 2:
                self._state["current"] = GRELVELCLURN
                self._state["trig"]    = "hint:2"
            case 'krelven', _:
                self._state["current"] = TRELDRARR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'krelven', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'krelven',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"krelven->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _treldrarr(self, hint):
        assert self._state.get("current") == TRELDRARR, \
            f"glanskelx.treldrarr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'treldrarr', 2:
                self._state["current"] = GRELVELCLURN
                self._state["trig"]    = "hint:2"
            case 'treldrarr', _:
                self._state["current"] = KROSSPURPRANR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'treldrarr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'treldrarr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"treldrarr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _krosspurpranr(self, hint):
        assert self._state.get("current") == KROSSPURPRANR, \
            f"glanskelx.krosspurpranr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'krosspurpranr', 2:
                self._state["current"] = GRELVELCLURN
                self._state["trig"]    = "hint:2"
            case 'krosspurpranr', 1:
                self._state["current"] = SLAXPREXGRUL
                self._state["trig"]    = "hint:1"
            case 'krosspurpranr', _:
                self._state["current"] = KRENPREXGRIM
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'krosspurpranr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'krosspurpranr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"krosspurpranr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _krenprexgrim(self, hint):
        assert self._state.get("current") == KRENPREXGRIM, \
            f"glanskelx.krenprexgrim: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'krenprexgrim', 2:
                self._state["current"] = GRELVELCLURN
                self._state["trig"]    = "hint:2"
            case 'krenprexgrim', _:
                self._state["current"] = BRARCLOS
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'krenprexgrim', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'krenprexgrim',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"krenprexgrim->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brarclos(self, hint):
        assert self._state.get("current") == BRARCLOS, \
            f"glanskelx.brarclos: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brarclos', 2:
                self._state["current"] = GRELVELCLURN
                self._state["trig"]    = "hint:2"
            case 'brarclos', 1:
                self._state["current"] = BLALDRONR
                self._state["trig"]    = "hint:1"
            case 'brarclos', _:
                self._state["current"] = KRIXFLOR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brarclos', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brarclos',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brarclos->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _krixflor(self, hint):
        assert self._state.get("current") == KRIXFLOR, \
            f"glanskelx.krixflor: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'krixflor', 2:
                self._state["current"] = GRELVELCLURN
                self._state["trig"]    = "hint:2"
            case 'krixflor', 1:
                self._state["current"] = SLIMDRIXBLAXK
                self._state["trig"]    = "hint:1"
            case 'krixflor', _:
                self._state["current"] = BLALDRONR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'krixflor', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'krixflor',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"krixflor->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blaldronr(self, hint):
        assert self._state.get("current") == BLALDRONR, \
            f"glanskelx.blaldronr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blaldronr', 2:
                self._state["current"] = GRELVELCLURN
                self._state["trig"]    = "hint:2"
            case 'blaldronr', 1:
                self._state["current"] = SLAXPREXGRUL
                self._state["trig"]    = "hint:1"
            case 'blaldronr', _:
                self._state["current"] = SLIMDRIXBLAXK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blaldronr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blaldronr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blaldronr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slimdrixblaxk(self, hint):
        assert self._state.get("current") == SLIMDRIXBLAXK, \
            f"glanskelx.slimdrixblaxk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slimdrixblaxk', 2:
                self._state["current"] = GRELVELCLURN
                self._state["trig"]    = "hint:2"
            case 'slimdrixblaxk', _:
                self._state["current"] = GRONBRALSPEXL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slimdrixblaxk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slimdrixblaxk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slimdrixblaxk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _gronbralspexl(self, hint):
        assert self._state.get("current") == GRONBRALSPEXL, \
            f"glanskelx.gronbralspexl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'gronbralspexl', 2:
                self._state["current"] = GRELVELCLURN
                self._state["trig"]    = "hint:2"
            case 'gronbralspexl', _:
                self._state["current"] = GRULGRALK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'gronbralspexl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'gronbralspexl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"gronbralspexl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _grulgralk(self, hint):
        assert self._state.get("current") == GRULGRALK, \
            f"glanskelx.grulgralk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'grulgralk', 2:
                self._state["current"] = GRELVELCLURN
                self._state["trig"]    = "hint:2"
            case 'grulgralk', 1:
                self._state["current"] = VORPRAN
                self._state["trig"]    = "hint:1"
            case 'grulgralk', _:
                self._state["current"] = CLURTRALX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'grulgralk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'grulgralk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"grulgralk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _clurtralx(self, hint):
        assert self._state.get("current") == CLURTRALX, \
            f"glanskelx.clurtralx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'clurtralx', 2:
                self._state["current"] = GRELVELCLURN
                self._state["trig"]    = "hint:2"
            case 'clurtralx', 0:
                self._state["current"] = SLAXPREXGRUL
                self._state["trig"]    = "hint:0"
            case 'clurtralx', _:
                self._state["current"] = VORPRAN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'clurtralx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'clurtralx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"clurtralx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _vorpran(self, hint):
        assert self._state.get("current") == VORPRAN, \
            f"glanskelx.vorpran: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'vorpran', 2:
                self._state["current"] = GRELVELCLURN
                self._state["trig"]    = "hint:2"
            case 'vorpran', _:
                self._state["current"] = KRULGRAN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'vorpran', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'vorpran',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"vorpran->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _krulgran(self, hint):
        assert self._state.get("current") == KRULGRAN, \
            f"glanskelx.krulgran: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'krulgran', 2:
                self._state["current"] = GRELVELCLURN
                self._state["trig"]    = "hint:2"
            case 'krulgran', 0:
                self._state["current"] = SLAXPREXGRUL
                self._state["trig"]    = "hint:0"
            case 'krulgran', _:
                self._state["current"] = SKENBLALSKOS
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'krulgran', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'krulgran',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"krulgran->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skenblalskos(self, hint):
        assert self._state.get("current") == SKENBLALSKOS, \
            f"glanskelx.skenblalskos: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skenblalskos', 2:
                self._state["current"] = GRELVELCLURN
                self._state["trig"]    = "hint:2"
            case 'skenblalskos', 1:
                self._state["current"] = PRURFLENGRORR
                self._state["trig"]    = "hint:1"
            case 'skenblalskos', _:
                self._state["current"] = BRIXBRIMSTEXK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skenblalskos', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skenblalskos',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skenblalskos->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brixbrimstexk(self, hint):
        assert self._state.get("current") == BRIXBRIMSTEXK, \
            f"glanskelx.brixbrimstexk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brixbrimstexk', 2:
                self._state["current"] = GRELVELCLURN
                self._state["trig"]    = "hint:2"
            case 'brixbrimstexk', _:
                self._state["current"] = PRURFLENGRORR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brixbrimstexk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brixbrimstexk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brixbrimstexk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _prurflengrorr(self, hint):
        assert self._state.get("current") == PRURFLENGRORR, \
            f"glanskelx.prurflengrorr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'prurflengrorr', 2:
                self._state["current"] = GRELVELCLURN
                self._state["trig"]    = "hint:2"
            case 'prurflengrorr', 1:
                self._state["current"] = SLAXPREXGRUL
                self._state["trig"]    = "hint:1"
            case 'prurflengrorr', _:
                self._state["current"] = PRELPROSGRURT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'prurflengrorr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'prurflengrorr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"prurflengrorr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _prelprosgrurt(self, hint):
        assert self._state.get("current") == PRELPROSGRURT, \
            f"glanskelx.prelprosgrurt: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'prelprosgrurt', 2:
                self._state["current"] = GRELVELCLURN
                self._state["trig"]    = "hint:2"
            case 'prelprosgrurt', 1:
                self._state["current"] = SLAXPREXGRUL
                self._state["trig"]    = "hint:1"
            case 'prelprosgrurt', _:
                self._state["current"] = TRALVEXKRELR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'prelprosgrurt', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'prelprosgrurt',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"prelprosgrurt->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _tralvexkrelr(self, hint):
        assert self._state.get("current") == TRALVEXKRELR, \
            f"glanskelx.tralvexkrelr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'tralvexkrelr', 2:
                self._state["current"] = GRELVELCLURN
                self._state["trig"]    = "hint:2"
            case 'tralvexkrelr', _:
                self._state["current"] = DREXCLAXL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'tralvexkrelr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'tralvexkrelr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"tralvexkrelr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _drexclaxl(self, hint):
        assert self._state.get("current") == DREXCLAXL, \
            f"glanskelx.drexclaxl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'drexclaxl', 2:
                self._state["current"] = GRELVELCLURN
                self._state["trig"]    = "hint:2"
            case 'drexclaxl', _:
                self._state["current"] = BRULFLELSKEXN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'drexclaxl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'drexclaxl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"drexclaxl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brulflelskexn(self, hint):
        assert self._state.get("current") == BRULFLELSKEXN, \
            f"glanskelx.brulflelskexn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brulflelskexn', 2:
                self._state["current"] = GRELVELCLURN
                self._state["trig"]    = "hint:2"
            case 'brulflelskexn', 0:
                self._state["current"] = CLONGREX
                self._state["trig"]    = "hint:0"
            case 'brulflelskexn', _:
                self._state["current"] = KROSPRIX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brulflelskexn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brulflelskexn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brulflelskexn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _krosprix(self, hint):
        assert self._state.get("current") == KROSPRIX, \
            f"glanskelx.krosprix: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'krosprix', 2:
                self._state["current"] = GRELVELCLURN
                self._state["trig"]    = "hint:2"
            case 'krosprix', _:
                self._state["current"] = CLONGREX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'krosprix', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'krosprix',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"krosprix->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _clongrex(self, hint):
        assert self._state.get("current") == CLONGREX, \
            f"glanskelx.clongrex: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'clongrex', 2:
                self._state["current"] = GRELVELCLURN
                self._state["trig"]    = "hint:2"
            case 'clongrex', _:
                self._state["current"] = SPOSFLEXN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'clongrex', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'clongrex',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"clongrex->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _sposflexn(self, hint):
        assert self._state.get("current") == SPOSFLEXN, \
            f"glanskelx.sposflexn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'sposflexn', 2:
                self._state["current"] = GRELVELCLURN
                self._state["trig"]    = "hint:2"
            case 'sposflexn', _:
                self._state["current"] = FLIXCLEXKRENK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'sposflexn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'sposflexn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"sposflexn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _flixclexkrenk(self, hint):
        assert self._state.get("current") == FLIXCLEXKRENK, \
            f"glanskelx.flixclexkrenk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'flixclexkrenk', 2:
                self._state["current"] = GRELVELCLURN
                self._state["trig"]    = "hint:2"
            case 'flixclexkrenk', _:
                self._state["current"] = PRALSKIMK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'flixclexkrenk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'flixclexkrenk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"flixclexkrenk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _pralskimk(self, hint):
        assert self._state.get("current") == PRALSKIMK, \
            f"glanskelx.pralskimk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'pralskimk', 2:
                self._state["current"] = GRELVELCLURN
                self._state["trig"]    = "hint:2"
            case 'pralskimk', _:
                self._state["current"] = FLIMTROST
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'pralskimk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'pralskimk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"pralskimk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _flimtrost(self, hint):
        assert self._state.get("current") == FLIMTROST, \
            f"glanskelx.flimtrost: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'flimtrost', 2:
                self._state["current"] = GRELVELCLURN
                self._state["trig"]    = "hint:2"
            case 'flimtrost', _:
                self._state["current"] = STULSLEXTRARX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'flimtrost', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'flimtrost',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"flimtrost->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _stulslextrarx(self, hint):
        assert self._state.get("current") == STULSLEXTRARX, \
            f"glanskelx.stulslextrarx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'stulslextrarx', 2:
                self._state["current"] = GRELVELCLURN
                self._state["trig"]    = "hint:2"
            case 'stulslextrarx', 0:
                self._state["current"] = VURTRORX
                self._state["trig"]    = "hint:0"
            case 'stulslextrarx', _:
                self._state["current"] = VELSTONFLALK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'stulslextrarx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'stulslextrarx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"stulslextrarx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _velstonflalk(self, hint):
        assert self._state.get("current") == VELSTONFLALK, \
            f"glanskelx.velstonflalk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'velstonflalk', 2:
                self._state["current"] = GRELVELCLURN
                self._state["trig"]    = "hint:2"
            case 'velstonflalk', 1:
                self._state["current"] = SLAXPREXGRUL
                self._state["trig"]    = "hint:1"
            case 'velstonflalk', _:
                self._state["current"] = VURTRORX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'velstonflalk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'velstonflalk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"velstonflalk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _vurtrorx(self, hint):
        assert self._state.get("current") == VURTRORX, \
            f"glanskelx.vurtrorx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'vurtrorx', 2:
                self._state["current"] = GRELVELCLURN
                self._state["trig"]    = "hint:2"
            case 'vurtrorx', 1:
                self._state["current"] = SLAXPREXGRUL
                self._state["trig"]    = "hint:1"
            case 'vurtrorx', _:
                self._state["current"] = TRURKRALN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'vurtrorx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'vurtrorx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"vurtrorx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _trurkraln(self, hint):
        assert self._state.get("current") == TRURKRALN, \
            f"glanskelx.trurkraln: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'trurkraln', 2:
                self._state["current"] = GRELVELCLURN
                self._state["trig"]    = "hint:2"
            case 'trurkraln', 1:
                self._state["current"] = SLULDRON
                self._state["trig"]    = "hint:1"
            case 'trurkraln', _:
                self._state["current"] = BLOSGRELL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'trurkraln', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'trurkraln',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"trurkraln->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blosgrell(self, hint):
        assert self._state.get("current") == BLOSGRELL, \
            f"glanskelx.blosgrell: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blosgrell', 2:
                self._state["current"] = GRELVELCLURN
                self._state["trig"]    = "hint:2"
            case 'blosgrell', _:
                self._state["current"] = SLULDRON
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blosgrell', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blosgrell',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blosgrell->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _sluldron(self, hint):
        assert self._state.get("current") == SLULDRON, \
            f"glanskelx.sluldron: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'sluldron', 2:
                self._state["current"] = GRELVELCLURN
                self._state["trig"]    = "hint:2"
            case 'sluldron', _:
                self._state["current"] = BLARKRALL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'sluldron', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'sluldron',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"sluldron->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blarkrall(self, hint):
        assert self._state.get("current") == BLARKRALL, \
            f"glanskelx.blarkrall: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blarkrall', 2:
                self._state["current"] = GRELVELCLURN
                self._state["trig"]    = "hint:2"
            case 'blarkrall', _:
                self._state["current"] = PRELFLAXK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blarkrall', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blarkrall',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blarkrall->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _prelflaxk(self, hint):
        assert self._state.get("current") == PRELFLAXK, \
            f"glanskelx.prelflaxk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'prelflaxk', 2:
                self._state["current"] = GRELVELCLURN
                self._state["trig"]    = "hint:2"
            case 'prelflaxk', _:
                self._state["current"] = BLALBRAXSKELN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'prelflaxk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'prelflaxk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"prelflaxk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blalbraxskeln(self, hint):
        assert self._state.get("current") == BLALBRAXSKELN, \
            f"glanskelx.blalbraxskeln: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blalbraxskeln', 2:
                self._state["current"] = GRELVELCLURN
                self._state["trig"]    = "hint:2"
            case 'blalbraxskeln', _:
                self._state["current"] = KRELSLURSLONL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blalbraxskeln', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blalbraxskeln',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blalbraxskeln->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _krelslurslonl(self, hint):
        assert self._state.get("current") == KRELSLURSLONL, \
            f"glanskelx.krelslurslonl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'krelslurslonl', 2:
                self._state["current"] = GRELVELCLURN
                self._state["trig"]    = "hint:2"
            case 'krelslurslonl', _:
                self._state["current"] = TROSSLAXR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'krelslurslonl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'krelslurslonl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"krelslurslonl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _trosslaxr(self, hint):
        assert self._state.get("current") == TROSSLAXR, \
            f"glanskelx.trosslaxr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'trosslaxr', 2:
                self._state["current"] = GRELVELCLURN
                self._state["trig"]    = "hint:2"
            case 'trosslaxr', 0:
                self._state["current"] = SLAXPREXGRUL
                self._state["trig"]    = "hint:0"
            case 'trosslaxr', _:
                self._state["current"] = SPORSLONCLOS
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'trosslaxr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'trosslaxr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"trosslaxr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _sporslonclos(self, hint):
        assert self._state.get("current") == SPORSLONCLOS, \
            f"glanskelx.sporslonclos: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'sporslonclos', 2:
                self._state["current"] = GRELVELCLURN
                self._state["trig"]    = "hint:2"
            case 'sporslonclos', _:
                self._state["current"] = BLEXDRELCLIM
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'sporslonclos', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'sporslonclos',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"sporslonclos->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blexdrelclim(self, hint):
        assert self._state.get("current") == BLEXDRELCLIM, \
            f"glanskelx.blexdrelclim: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blexdrelclim', 2:
                self._state["current"] = GRELVELCLURN
                self._state["trig"]    = "hint:2"
            case 'blexdrelclim', 0:
                self._state["current"] = SLAXPREXGRUL
                self._state["trig"]    = "hint:0"
            case 'blexdrelclim', _:
                self._state["current"] = BLOSSKALBROS
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blexdrelclim', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blexdrelclim',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blexdrelclim->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blosskalbros(self, hint):
        assert self._state.get("current") == BLOSSKALBROS, \
            f"glanskelx.blosskalbros: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blosskalbros', 2:
                self._state["current"] = GRELVELCLURN
                self._state["trig"]    = "hint:2"
            case 'blosskalbros', _:
                self._state["current"] = TRANPRELSKURK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blosskalbros', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blosskalbros',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blosskalbros->{_to}", _xid_val)
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
            _xid_val = _xid(__name__, 'drorprimgrark', "error", "assert_fail")
            _emit(cycle, 1, __name__, 'drorprimgrark',
                   {"hint": hint, "span": span, "caller": caller},
                   dict(ctx), _conds,
                   "entry_blocked->error", _xid_val, assertion=_asrt)
            return 2, cycle + 1

        self._state = {"current": DRORPRIMGRARK, "ctx": ctx,
                        "span": span, "caller": caller,
                        "trig": "auto", "cycle": cycle}
        _dispatch = {
            DRORPRIMGRARK: self._drorprimgrark,
            SLANTRIMSTAN: self._slantrimstan,
            VANBLENTRORX: self._vanblentrorx,
            FLARPRALBLUR: self._flarpralblur,
            SLONSKIMKRIX: self._slonskimkrix,
            STORDRANT: self._stordrant,
            FLENDREN: self._flendren,
            PRIXBLAXL: self._prixblaxl,
            SLIXGLENR: self._slixglenr,
            SKULVAR: self._skulvar,
            TRANBRARX: self._tranbrarx,
            SPOSDRELKREX: self._sposdrelkrex,
            KRURBLEL: self._krurblel,
            CLENTRIXBLEL: self._clentrixblel,
            BRAXFLELBRANR: self._braxflelbranr,
            SKELGRENSTOSK: self._skelgrenstosk,
            BLONDRALPRURR: self._blondralprurr,
            STONPRENX: self._stonprenx,
            SPANKREXK: self._spankrexk,
            GLANVIMGLIX: self._glanvimglix,
            GRIMTROSKRULN: self._grimtroskruln,
            CLURGLALT: self._clurglalt,
            VARBLAXL: self._varblaxl,
            SPENVURVENR: self._spenvurvenr,
            CLOSKRULR: self._closkrulr,
            KRELVEN: self._krelven,
            TRELDRARR: self._treldrarr,
            KROSSPURPRANR: self._krosspurpranr,
            KRENPREXGRIM: self._krenprexgrim,
            BRARCLOS: self._brarclos,
            KRIXFLOR: self._krixflor,
            BLALDRONR: self._blaldronr,
            SLIMDRIXBLAXK: self._slimdrixblaxk,
            GRONBRALSPEXL: self._gronbralspexl,
            GRULGRALK: self._grulgralk,
            CLURTRALX: self._clurtralx,
            VORPRAN: self._vorpran,
            KRULGRAN: self._krulgran,
            SKENBLALSKOS: self._skenblalskos,
            BRIXBRIMSTEXK: self._brixbrimstexk,
            PRURFLENGRORR: self._prurflengrorr,
            PRELPROSGRURT: self._prelprosgrurt,
            TRALVEXKRELR: self._tralvexkrelr,
            DREXCLAXL: self._drexclaxl,
            BRULFLELSKEXN: self._brulflelskexn,
            KROSPRIX: self._krosprix,
            CLONGREX: self._clongrex,
            SPOSFLEXN: self._sposflexn,
            FLIXCLEXKRENK: self._flixclexkrenk,
            PRALSKIMK: self._pralskimk,
            FLIMTROST: self._flimtrost,
            STULSLEXTRARX: self._stulslextrarx,
            VELSTONFLALK: self._velstonflalk,
            VURTRORX: self._vurtrorx,
            TRURKRALN: self._trurkraln,
            BLOSGRELL: self._blosgrell,
            SLULDRON: self._sluldron,
            BLARKRALL: self._blarkrall,
            PRELFLAXK: self._prelflaxk,
            BLALBRAXSKELN: self._blalbraxskeln,
            KRELSLURSLONL: self._krelslurslonl,
            TROSSLAXR: self._trosslaxr,
            SPORSLONCLOS: self._sporslonclos,
            BLEXDRELCLIM: self._blexdrelclim,
            BLOSSKALBROS: self._blosskalbros,
        }
        while self._state["current"] not in _R and self._state["cycle"] - cycle < 8000:
            _dispatch[self._state["current"]](hint)
        _ret     = _R.get(self._state["current"], -1)
        _is_err  = self._state["current"] == GRELVELCLURN
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
    return GlanskelxFSM().invoke(hint=hint, span=span, caller=caller, ctx=ctx, cycle=cycle)
