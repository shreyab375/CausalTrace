from _log import _w as _emit, _xid

DROSKRARR = 'droskrarr'
CLORSLALL = 'clorslall'
PRENSTELK = 'prenstelk'
VULPRAX = 'vulprax'
TRALDRONX = 'traldronx'
DRORSPIXFLALT = 'drorspixflalt'
SKELSKULCLORX = 'skelskulclorx'
DRONGLELDRENL = 'drongleldrenl'
TRURSKUR = 'trurskur'
DREXSPAN = 'drexspan'
BRENCLIX = 'brenclix'
SLULSPALX = 'slulspalx'
SLELKRURK = 'slelkrurk'
GRULGRURKRIXT = 'grulgrurkrixt'
FLIMSPON = 'flimspon'
SKOSPRAXN = 'skospraxn'
CLULSTALX = 'clulstalx'
TRELBLARPRIMT = 'trelblarprimt'
SLENKRULSKOS = 'slenkrulskos'
FLALKRURBRURN = 'flalkrurbrurn'
VAXBLAN = 'vaxblan'
FLAXPRONFLURK = 'flaxpronflurk'
DRALFLEXSPORL = 'dralflexsporl'
FLIXGLORR = 'flixglorr'
STONTRON = 'stontron'
VIXDRULN = 'vixdruln'
STALCLAL = 'stalclal'
VONKRONR = 'vonkronr'
FLEXGLOSCLAXX = 'flexglosclaxx'
CLELGLANGRURN = 'clelglangrurn'
STONSPALR = 'stonspalr'
VARSKIMKRENT = 'varskimkrent'
BLONFLANT = 'blonflant'
VARGRUL = 'vargrul'
SLOSVEX = 'slosvex'
BLENBLULSLONT = 'blenblulslont'
DREXPRANKRIX = 'drexprankrix'
TRELSLAR = 'trelslar'
GRELFLARVENN = 'grelflarvenn'
CLIMBLARGRIM = 'climblargrim'
CLEXGLURT = 'clexglurt'
VIXFLENPROS = 'vixflenpros'
GRANGLALK = 'granglalk'
DRIXFLIXTRAR = 'drixflixtrar'
CLAXDRAN = 'claxdran'
CLENBRONDRIMX = 'clenbrondrimx'
DRIMSPANTRAL = 'drimspantral'
STAXSKEN = 'staxsken'
CLOSCLENGRART = 'closclengrart'
KRURGLIMT = 'krurglimt'
BRARGRULL = 'brargrull'
BRAXBRAX = 'braxbrax'
KRURPRAX = 'krurprax'
BLOSSKENK = 'blosskenk'
GRULFLAN = 'grulflan'
SKORVULSKAR = 'skorvulskar'
DRARDRUR = 'drardrur'
VANSKUR = 'vanskur'
BLOSTREN = 'blostren'
SPIMSTOST = 'spimstost'
SLALBRURL = 'slalbrurl'
VARVOR = 'varvor'
SKONTRARVUL = 'skontrarvul'
GRIXSLORR = 'grixslorr'
VIMSPIML = 'vimspiml'
TREXBRANDRAXR = 'trexbrandraxr'
PRURFLIX = 'prurflix'
TRURCLENR = 'trurclenr'

_R = {
    TREXBRANDRAXR: 0,
    PRURFLIX: 1,
    TRURCLENR: 2,
}

_CTX_WRITES_KEY  = 'flurslex'
_CTX_WRITE_STATE = DRORSPIXFLALT

class SpaxglosxFSM:
    def __init__(self):
        self._state = {}

    def _droskrarr(self, hint):
        assert self._state.get("current") == DROSKRARR, \
            f"spaxglosx.droskrarr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'droskrarr', 2:
                self._state["current"] = TRURCLENR
                self._state["trig"]    = "hint:2"
            case 'droskrarr', 1:
                self._state["current"] = PRURFLIX
                self._state["trig"]    = "hint:1"
            case 'droskrarr', _:
                self._state["current"] = CLORSLALL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'droskrarr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'droskrarr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"droskrarr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _clorslall(self, hint):
        assert self._state.get("current") == CLORSLALL, \
            f"spaxglosx.clorslall: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'clorslall', 2:
                self._state["current"] = TRURCLENR
                self._state["trig"]    = "hint:2"
            case 'clorslall', 0:
                self._state["current"] = PRURFLIX
                self._state["trig"]    = "hint:0"
            case 'clorslall', _:
                self._state["current"] = PRENSTELK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'clorslall', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'clorslall',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"clorslall->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _prenstelk(self, hint):
        assert self._state.get("current") == PRENSTELK, \
            f"spaxglosx.prenstelk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'prenstelk', 2:
                self._state["current"] = TRURCLENR
                self._state["trig"]    = "hint:2"
            case 'prenstelk', _:
                self._state["current"] = VULPRAX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'prenstelk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'prenstelk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"prenstelk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _vulprax(self, hint):
        assert self._state.get("current") == VULPRAX, \
            f"spaxglosx.vulprax: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'vulprax', 2:
                self._state["current"] = TRURCLENR
                self._state["trig"]    = "hint:2"
            case 'vulprax', 1:
                self._state["current"] = DRORSPIXFLALT
                self._state["trig"]    = "hint:1"
            case 'vulprax', _:
                self._state["current"] = TRALDRONX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'vulprax', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'vulprax',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"vulprax->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _traldronx(self, hint):
        assert self._state.get("current") == TRALDRONX, \
            f"spaxglosx.traldronx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'traldronx', 2:
                self._state["current"] = TRURCLENR
                self._state["trig"]    = "hint:2"
            case 'traldronx', _:
                self._state["current"] = DRORSPIXFLALT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'traldronx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'traldronx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"traldronx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _drorspixflalt(self, hint):
        assert self._state.get("current") == DRORSPIXFLALT, \
            f"spaxglosx.drorspixflalt: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        _ctx_val_before = self._state["ctx"].get(_CTX_WRITES_KEY, 0)
        match self._state["current"], hint:
            case 'drorspixflalt', 2:
                self._state["current"] = TRURCLENR
                self._state["trig"]    = "hint:2"
            case 'drorspixflalt', 1:
                self._state["current"] = DRONGLELDRENL
                self._state["trig"]    = "hint:1"
            case 'drorspixflalt', _:
                self._state["current"] = SKELSKULCLORX
                self._state["trig"]    = "auto"
        _old = self._state["ctx"].get(_CTX_WRITES_KEY, 0)
        _inc = 2 if hint == 2 else 1
        self._state["ctx"][_CTX_WRITES_KEY] = _old + _inc
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'drorspixflalt', _to, _trig)
        _conds = {"hint_branch": _hint_branch,
                   "ctx_write": True,
                   "ctx_val_before": _ctx_val_before}
        _emit(self._state["cycle"], 1, __name__, 'drorspixflalt',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"drorspixflalt->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skelskulclorx(self, hint):
        assert self._state.get("current") == SKELSKULCLORX, \
            f"spaxglosx.skelskulclorx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skelskulclorx', 2:
                self._state["current"] = TRURCLENR
                self._state["trig"]    = "hint:2"
            case 'skelskulclorx', _:
                self._state["current"] = DRONGLELDRENL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skelskulclorx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skelskulclorx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skelskulclorx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _drongleldrenl(self, hint):
        assert self._state.get("current") == DRONGLELDRENL, \
            f"spaxglosx.drongleldrenl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'drongleldrenl', 2:
                self._state["current"] = TRURCLENR
                self._state["trig"]    = "hint:2"
            case 'drongleldrenl', 0:
                self._state["current"] = PRURFLIX
                self._state["trig"]    = "hint:0"
            case 'drongleldrenl', _:
                self._state["current"] = TRURSKUR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'drongleldrenl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'drongleldrenl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"drongleldrenl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _trurskur(self, hint):
        assert self._state.get("current") == TRURSKUR, \
            f"spaxglosx.trurskur: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'trurskur', 2:
                self._state["current"] = TRURCLENR
                self._state["trig"]    = "hint:2"
            case 'trurskur', _:
                self._state["current"] = DREXSPAN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'trurskur', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'trurskur',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"trurskur->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _drexspan(self, hint):
        assert self._state.get("current") == DREXSPAN, \
            f"spaxglosx.drexspan: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'drexspan', 2:
                self._state["current"] = TRURCLENR
                self._state["trig"]    = "hint:2"
            case 'drexspan', _:
                self._state["current"] = BRENCLIX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'drexspan', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'drexspan',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"drexspan->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brenclix(self, hint):
        assert self._state.get("current") == BRENCLIX, \
            f"spaxglosx.brenclix: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brenclix', 2:
                self._state["current"] = TRURCLENR
                self._state["trig"]    = "hint:2"
            case 'brenclix', _:
                self._state["current"] = SLULSPALX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brenclix', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brenclix',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brenclix->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slulspalx(self, hint):
        assert self._state.get("current") == SLULSPALX, \
            f"spaxglosx.slulspalx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slulspalx', 2:
                self._state["current"] = TRURCLENR
                self._state["trig"]    = "hint:2"
            case 'slulspalx', _:
                self._state["current"] = SLELKRURK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slulspalx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slulspalx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slulspalx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slelkrurk(self, hint):
        assert self._state.get("current") == SLELKRURK, \
            f"spaxglosx.slelkrurk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slelkrurk', 2:
                self._state["current"] = TRURCLENR
                self._state["trig"]    = "hint:2"
            case 'slelkrurk', _:
                self._state["current"] = GRULGRURKRIXT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slelkrurk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slelkrurk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slelkrurk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _grulgrurkrixt(self, hint):
        assert self._state.get("current") == GRULGRURKRIXT, \
            f"spaxglosx.grulgrurkrixt: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'grulgrurkrixt', 2:
                self._state["current"] = TRURCLENR
                self._state["trig"]    = "hint:2"
            case 'grulgrurkrixt', _:
                self._state["current"] = FLIMSPON
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'grulgrurkrixt', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'grulgrurkrixt',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"grulgrurkrixt->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _flimspon(self, hint):
        assert self._state.get("current") == FLIMSPON, \
            f"spaxglosx.flimspon: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'flimspon', 2:
                self._state["current"] = TRURCLENR
                self._state["trig"]    = "hint:2"
            case 'flimspon', _:
                self._state["current"] = SKOSPRAXN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'flimspon', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'flimspon',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"flimspon->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skospraxn(self, hint):
        assert self._state.get("current") == SKOSPRAXN, \
            f"spaxglosx.skospraxn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skospraxn', 2:
                self._state["current"] = TRURCLENR
                self._state["trig"]    = "hint:2"
            case 'skospraxn', 0:
                self._state["current"] = TRELBLARPRIMT
                self._state["trig"]    = "hint:0"
            case 'skospraxn', _:
                self._state["current"] = CLULSTALX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skospraxn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skospraxn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skospraxn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _clulstalx(self, hint):
        assert self._state.get("current") == CLULSTALX, \
            f"spaxglosx.clulstalx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'clulstalx', 2:
                self._state["current"] = TRURCLENR
                self._state["trig"]    = "hint:2"
            case 'clulstalx', 1:
                self._state["current"] = PRURFLIX
                self._state["trig"]    = "hint:1"
            case 'clulstalx', _:
                self._state["current"] = TRELBLARPRIMT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'clulstalx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'clulstalx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"clulstalx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _trelblarprimt(self, hint):
        assert self._state.get("current") == TRELBLARPRIMT, \
            f"spaxglosx.trelblarprimt: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'trelblarprimt', 2:
                self._state["current"] = TRURCLENR
                self._state["trig"]    = "hint:2"
            case 'trelblarprimt', _:
                self._state["current"] = SLENKRULSKOS
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'trelblarprimt', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'trelblarprimt',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"trelblarprimt->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slenkrulskos(self, hint):
        assert self._state.get("current") == SLENKRULSKOS, \
            f"spaxglosx.slenkrulskos: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slenkrulskos', 2:
                self._state["current"] = TRURCLENR
                self._state["trig"]    = "hint:2"
            case 'slenkrulskos', 1:
                self._state["current"] = VAXBLAN
                self._state["trig"]    = "hint:1"
            case 'slenkrulskos', _:
                self._state["current"] = FLALKRURBRURN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slenkrulskos', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slenkrulskos',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slenkrulskos->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _flalkrurbrurn(self, hint):
        assert self._state.get("current") == FLALKRURBRURN, \
            f"spaxglosx.flalkrurbrurn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'flalkrurbrurn', 2:
                self._state["current"] = TRURCLENR
                self._state["trig"]    = "hint:2"
            case 'flalkrurbrurn', _:
                self._state["current"] = VAXBLAN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'flalkrurbrurn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'flalkrurbrurn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"flalkrurbrurn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _vaxblan(self, hint):
        assert self._state.get("current") == VAXBLAN, \
            f"spaxglosx.vaxblan: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'vaxblan', 2:
                self._state["current"] = TRURCLENR
                self._state["trig"]    = "hint:2"
            case 'vaxblan', 1:
                self._state["current"] = PRURFLIX
                self._state["trig"]    = "hint:1"
            case 'vaxblan', _:
                self._state["current"] = FLAXPRONFLURK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'vaxblan', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'vaxblan',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"vaxblan->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _flaxpronflurk(self, hint):
        assert self._state.get("current") == FLAXPRONFLURK, \
            f"spaxglosx.flaxpronflurk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'flaxpronflurk', 2:
                self._state["current"] = TRURCLENR
                self._state["trig"]    = "hint:2"
            case 'flaxpronflurk', 0:
                self._state["current"] = FLIXGLORR
                self._state["trig"]    = "hint:0"
            case 'flaxpronflurk', _:
                self._state["current"] = DRALFLEXSPORL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'flaxpronflurk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'flaxpronflurk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"flaxpronflurk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _dralflexsporl(self, hint):
        assert self._state.get("current") == DRALFLEXSPORL, \
            f"spaxglosx.dralflexsporl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'dralflexsporl', 2:
                self._state["current"] = TRURCLENR
                self._state["trig"]    = "hint:2"
            case 'dralflexsporl', 0:
                self._state["current"] = STONTRON
                self._state["trig"]    = "hint:0"
            case 'dralflexsporl', _:
                self._state["current"] = FLIXGLORR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'dralflexsporl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'dralflexsporl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"dralflexsporl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _flixglorr(self, hint):
        assert self._state.get("current") == FLIXGLORR, \
            f"spaxglosx.flixglorr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'flixglorr', 2:
                self._state["current"] = TRURCLENR
                self._state["trig"]    = "hint:2"
            case 'flixglorr', _:
                self._state["current"] = STONTRON
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'flixglorr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'flixglorr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"flixglorr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _stontron(self, hint):
        assert self._state.get("current") == STONTRON, \
            f"spaxglosx.stontron: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'stontron', 2:
                self._state["current"] = TRURCLENR
                self._state["trig"]    = "hint:2"
            case 'stontron', 0:
                self._state["current"] = STALCLAL
                self._state["trig"]    = "hint:0"
            case 'stontron', _:
                self._state["current"] = VIXDRULN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'stontron', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'stontron',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"stontron->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _vixdruln(self, hint):
        assert self._state.get("current") == VIXDRULN, \
            f"spaxglosx.vixdruln: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'vixdruln', 2:
                self._state["current"] = TRURCLENR
                self._state["trig"]    = "hint:2"
            case 'vixdruln', 0:
                self._state["current"] = PRURFLIX
                self._state["trig"]    = "hint:0"
            case 'vixdruln', _:
                self._state["current"] = STALCLAL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'vixdruln', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'vixdruln',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"vixdruln->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _stalclal(self, hint):
        assert self._state.get("current") == STALCLAL, \
            f"spaxglosx.stalclal: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'stalclal', 2:
                self._state["current"] = TRURCLENR
                self._state["trig"]    = "hint:2"
            case 'stalclal', 0:
                self._state["current"] = FLEXGLOSCLAXX
                self._state["trig"]    = "hint:0"
            case 'stalclal', _:
                self._state["current"] = VONKRONR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'stalclal', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'stalclal',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"stalclal->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _vonkronr(self, hint):
        assert self._state.get("current") == VONKRONR, \
            f"spaxglosx.vonkronr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'vonkronr', 2:
                self._state["current"] = TRURCLENR
                self._state["trig"]    = "hint:2"
            case 'vonkronr', _:
                self._state["current"] = FLEXGLOSCLAXX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'vonkronr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'vonkronr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"vonkronr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _flexglosclaxx(self, hint):
        assert self._state.get("current") == FLEXGLOSCLAXX, \
            f"spaxglosx.flexglosclaxx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'flexglosclaxx', 2:
                self._state["current"] = TRURCLENR
                self._state["trig"]    = "hint:2"
            case 'flexglosclaxx', _:
                self._state["current"] = CLELGLANGRURN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'flexglosclaxx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'flexglosclaxx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"flexglosclaxx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _clelglangrurn(self, hint):
        assert self._state.get("current") == CLELGLANGRURN, \
            f"spaxglosx.clelglangrurn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'clelglangrurn', 2:
                self._state["current"] = TRURCLENR
                self._state["trig"]    = "hint:2"
            case 'clelglangrurn', _:
                self._state["current"] = STONSPALR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'clelglangrurn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'clelglangrurn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"clelglangrurn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _stonspalr(self, hint):
        assert self._state.get("current") == STONSPALR, \
            f"spaxglosx.stonspalr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'stonspalr', 2:
                self._state["current"] = TRURCLENR
                self._state["trig"]    = "hint:2"
            case 'stonspalr', _:
                self._state["current"] = VARSKIMKRENT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'stonspalr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'stonspalr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"stonspalr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _varskimkrent(self, hint):
        assert self._state.get("current") == VARSKIMKRENT, \
            f"spaxglosx.varskimkrent: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'varskimkrent', 2:
                self._state["current"] = TRURCLENR
                self._state["trig"]    = "hint:2"
            case 'varskimkrent', 1:
                self._state["current"] = VARGRUL
                self._state["trig"]    = "hint:1"
            case 'varskimkrent', _:
                self._state["current"] = BLONFLANT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'varskimkrent', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'varskimkrent',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"varskimkrent->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blonflant(self, hint):
        assert self._state.get("current") == BLONFLANT, \
            f"spaxglosx.blonflant: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blonflant', 2:
                self._state["current"] = TRURCLENR
                self._state["trig"]    = "hint:2"
            case 'blonflant', 1:
                self._state["current"] = SLOSVEX
                self._state["trig"]    = "hint:1"
            case 'blonflant', _:
                self._state["current"] = VARGRUL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blonflant', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blonflant',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blonflant->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _vargrul(self, hint):
        assert self._state.get("current") == VARGRUL, \
            f"spaxglosx.vargrul: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'vargrul', 2:
                self._state["current"] = TRURCLENR
                self._state["trig"]    = "hint:2"
            case 'vargrul', _:
                self._state["current"] = SLOSVEX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'vargrul', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'vargrul',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"vargrul->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slosvex(self, hint):
        assert self._state.get("current") == SLOSVEX, \
            f"spaxglosx.slosvex: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slosvex', 2:
                self._state["current"] = TRURCLENR
                self._state["trig"]    = "hint:2"
            case 'slosvex', _:
                self._state["current"] = BLENBLULSLONT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slosvex', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slosvex',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slosvex->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blenblulslont(self, hint):
        assert self._state.get("current") == BLENBLULSLONT, \
            f"spaxglosx.blenblulslont: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blenblulslont', 2:
                self._state["current"] = TRURCLENR
                self._state["trig"]    = "hint:2"
            case 'blenblulslont', 1:
                self._state["current"] = PRURFLIX
                self._state["trig"]    = "hint:1"
            case 'blenblulslont', _:
                self._state["current"] = DREXPRANKRIX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blenblulslont', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blenblulslont',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blenblulslont->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _drexprankrix(self, hint):
        assert self._state.get("current") == DREXPRANKRIX, \
            f"spaxglosx.drexprankrix: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'drexprankrix', 2:
                self._state["current"] = TRURCLENR
                self._state["trig"]    = "hint:2"
            case 'drexprankrix', 1:
                self._state["current"] = GRELFLARVENN
                self._state["trig"]    = "hint:1"
            case 'drexprankrix', _:
                self._state["current"] = TRELSLAR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'drexprankrix', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'drexprankrix',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"drexprankrix->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _trelslar(self, hint):
        assert self._state.get("current") == TRELSLAR, \
            f"spaxglosx.trelslar: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'trelslar', 2:
                self._state["current"] = TRURCLENR
                self._state["trig"]    = "hint:2"
            case 'trelslar', _:
                self._state["current"] = GRELFLARVENN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'trelslar', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'trelslar',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"trelslar->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _grelflarvenn(self, hint):
        assert self._state.get("current") == GRELFLARVENN, \
            f"spaxglosx.grelflarvenn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'grelflarvenn', 2:
                self._state["current"] = TRURCLENR
                self._state["trig"]    = "hint:2"
            case 'grelflarvenn', _:
                self._state["current"] = CLIMBLARGRIM
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'grelflarvenn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'grelflarvenn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"grelflarvenn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _climblargrim(self, hint):
        assert self._state.get("current") == CLIMBLARGRIM, \
            f"spaxglosx.climblargrim: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'climblargrim', 2:
                self._state["current"] = TRURCLENR
                self._state["trig"]    = "hint:2"
            case 'climblargrim', 1:
                self._state["current"] = VIXFLENPROS
                self._state["trig"]    = "hint:1"
            case 'climblargrim', _:
                self._state["current"] = CLEXGLURT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'climblargrim', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'climblargrim',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"climblargrim->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _clexglurt(self, hint):
        assert self._state.get("current") == CLEXGLURT, \
            f"spaxglosx.clexglurt: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'clexglurt', 2:
                self._state["current"] = TRURCLENR
                self._state["trig"]    = "hint:2"
            case 'clexglurt', 0:
                self._state["current"] = PRURFLIX
                self._state["trig"]    = "hint:0"
            case 'clexglurt', _:
                self._state["current"] = VIXFLENPROS
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'clexglurt', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'clexglurt',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"clexglurt->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _vixflenpros(self, hint):
        assert self._state.get("current") == VIXFLENPROS, \
            f"spaxglosx.vixflenpros: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'vixflenpros', 2:
                self._state["current"] = TRURCLENR
                self._state["trig"]    = "hint:2"
            case 'vixflenpros', _:
                self._state["current"] = GRANGLALK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'vixflenpros', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'vixflenpros',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"vixflenpros->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _granglalk(self, hint):
        assert self._state.get("current") == GRANGLALK, \
            f"spaxglosx.granglalk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'granglalk', 2:
                self._state["current"] = TRURCLENR
                self._state["trig"]    = "hint:2"
            case 'granglalk', _:
                self._state["current"] = DRIXFLIXTRAR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'granglalk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'granglalk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"granglalk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _drixflixtrar(self, hint):
        assert self._state.get("current") == DRIXFLIXTRAR, \
            f"spaxglosx.drixflixtrar: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'drixflixtrar', 2:
                self._state["current"] = TRURCLENR
                self._state["trig"]    = "hint:2"
            case 'drixflixtrar', _:
                self._state["current"] = CLAXDRAN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'drixflixtrar', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'drixflixtrar',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"drixflixtrar->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _claxdran(self, hint):
        assert self._state.get("current") == CLAXDRAN, \
            f"spaxglosx.claxdran: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'claxdran', 2:
                self._state["current"] = TRURCLENR
                self._state["trig"]    = "hint:2"
            case 'claxdran', 1:
                self._state["current"] = DRIMSPANTRAL
                self._state["trig"]    = "hint:1"
            case 'claxdran', _:
                self._state["current"] = CLENBRONDRIMX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'claxdran', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'claxdran',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"claxdran->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _clenbrondrimx(self, hint):
        assert self._state.get("current") == CLENBRONDRIMX, \
            f"spaxglosx.clenbrondrimx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'clenbrondrimx', 2:
                self._state["current"] = TRURCLENR
                self._state["trig"]    = "hint:2"
            case 'clenbrondrimx', _:
                self._state["current"] = DRIMSPANTRAL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'clenbrondrimx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'clenbrondrimx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"clenbrondrimx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _drimspantral(self, hint):
        assert self._state.get("current") == DRIMSPANTRAL, \
            f"spaxglosx.drimspantral: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'drimspantral', 2:
                self._state["current"] = TRURCLENR
                self._state["trig"]    = "hint:2"
            case 'drimspantral', 1:
                self._state["current"] = CLOSCLENGRART
                self._state["trig"]    = "hint:1"
            case 'drimspantral', _:
                self._state["current"] = STAXSKEN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'drimspantral', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'drimspantral',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"drimspantral->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _staxsken(self, hint):
        assert self._state.get("current") == STAXSKEN, \
            f"spaxglosx.staxsken: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'staxsken', 2:
                self._state["current"] = TRURCLENR
                self._state["trig"]    = "hint:2"
            case 'staxsken', 0:
                self._state["current"] = KRURGLIMT
                self._state["trig"]    = "hint:0"
            case 'staxsken', _:
                self._state["current"] = CLOSCLENGRART
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'staxsken', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'staxsken',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"staxsken->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _closclengrart(self, hint):
        assert self._state.get("current") == CLOSCLENGRART, \
            f"spaxglosx.closclengrart: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'closclengrart', 2:
                self._state["current"] = TRURCLENR
                self._state["trig"]    = "hint:2"
            case 'closclengrart', 1:
                self._state["current"] = BRARGRULL
                self._state["trig"]    = "hint:1"
            case 'closclengrart', _:
                self._state["current"] = KRURGLIMT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'closclengrart', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'closclengrart',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"closclengrart->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _krurglimt(self, hint):
        assert self._state.get("current") == KRURGLIMT, \
            f"spaxglosx.krurglimt: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'krurglimt', 2:
                self._state["current"] = TRURCLENR
                self._state["trig"]    = "hint:2"
            case 'krurglimt', _:
                self._state["current"] = BRARGRULL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'krurglimt', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'krurglimt',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"krurglimt->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brargrull(self, hint):
        assert self._state.get("current") == BRARGRULL, \
            f"spaxglosx.brargrull: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brargrull', 2:
                self._state["current"] = TRURCLENR
                self._state["trig"]    = "hint:2"
            case 'brargrull', _:
                self._state["current"] = BRAXBRAX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brargrull', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brargrull',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brargrull->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _braxbrax(self, hint):
        assert self._state.get("current") == BRAXBRAX, \
            f"spaxglosx.braxbrax: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'braxbrax', 2:
                self._state["current"] = TRURCLENR
                self._state["trig"]    = "hint:2"
            case 'braxbrax', _:
                self._state["current"] = KRURPRAX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'braxbrax', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'braxbrax',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"braxbrax->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _krurprax(self, hint):
        assert self._state.get("current") == KRURPRAX, \
            f"spaxglosx.krurprax: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'krurprax', 2:
                self._state["current"] = TRURCLENR
                self._state["trig"]    = "hint:2"
            case 'krurprax', _:
                self._state["current"] = BLOSSKENK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'krurprax', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'krurprax',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"krurprax->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blosskenk(self, hint):
        assert self._state.get("current") == BLOSSKENK, \
            f"spaxglosx.blosskenk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blosskenk', 2:
                self._state["current"] = TRURCLENR
                self._state["trig"]    = "hint:2"
            case 'blosskenk', _:
                self._state["current"] = GRULFLAN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blosskenk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blosskenk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blosskenk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _grulflan(self, hint):
        assert self._state.get("current") == GRULFLAN, \
            f"spaxglosx.grulflan: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'grulflan', 2:
                self._state["current"] = TRURCLENR
                self._state["trig"]    = "hint:2"
            case 'grulflan', 0:
                self._state["current"] = PRURFLIX
                self._state["trig"]    = "hint:0"
            case 'grulflan', _:
                self._state["current"] = SKORVULSKAR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'grulflan', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'grulflan',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"grulflan->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skorvulskar(self, hint):
        assert self._state.get("current") == SKORVULSKAR, \
            f"spaxglosx.skorvulskar: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skorvulskar', 2:
                self._state["current"] = TRURCLENR
                self._state["trig"]    = "hint:2"
            case 'skorvulskar', 0:
                self._state["current"] = PRURFLIX
                self._state["trig"]    = "hint:0"
            case 'skorvulskar', _:
                self._state["current"] = DRARDRUR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skorvulskar', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skorvulskar',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skorvulskar->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _drardrur(self, hint):
        assert self._state.get("current") == DRARDRUR, \
            f"spaxglosx.drardrur: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'drardrur', 2:
                self._state["current"] = TRURCLENR
                self._state["trig"]    = "hint:2"
            case 'drardrur', 0:
                self._state["current"] = BLOSTREN
                self._state["trig"]    = "hint:0"
            case 'drardrur', _:
                self._state["current"] = VANSKUR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'drardrur', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'drardrur',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"drardrur->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _vanskur(self, hint):
        assert self._state.get("current") == VANSKUR, \
            f"spaxglosx.vanskur: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'vanskur', 2:
                self._state["current"] = TRURCLENR
                self._state["trig"]    = "hint:2"
            case 'vanskur', 1:
                self._state["current"] = PRURFLIX
                self._state["trig"]    = "hint:1"
            case 'vanskur', _:
                self._state["current"] = BLOSTREN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'vanskur', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'vanskur',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"vanskur->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blostren(self, hint):
        assert self._state.get("current") == BLOSTREN, \
            f"spaxglosx.blostren: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blostren', 2:
                self._state["current"] = TRURCLENR
                self._state["trig"]    = "hint:2"
            case 'blostren', _:
                self._state["current"] = SPIMSTOST
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blostren', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blostren',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blostren->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _spimstost(self, hint):
        assert self._state.get("current") == SPIMSTOST, \
            f"spaxglosx.spimstost: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'spimstost', 2:
                self._state["current"] = TRURCLENR
                self._state["trig"]    = "hint:2"
            case 'spimstost', _:
                self._state["current"] = SLALBRURL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'spimstost', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'spimstost',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"spimstost->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slalbrurl(self, hint):
        assert self._state.get("current") == SLALBRURL, \
            f"spaxglosx.slalbrurl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slalbrurl', 2:
                self._state["current"] = TRURCLENR
                self._state["trig"]    = "hint:2"
            case 'slalbrurl', 1:
                self._state["current"] = PRURFLIX
                self._state["trig"]    = "hint:1"
            case 'slalbrurl', _:
                self._state["current"] = VARVOR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slalbrurl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slalbrurl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slalbrurl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _varvor(self, hint):
        assert self._state.get("current") == VARVOR, \
            f"spaxglosx.varvor: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'varvor', 2:
                self._state["current"] = TRURCLENR
                self._state["trig"]    = "hint:2"
            case 'varvor', _:
                self._state["current"] = SKONTRARVUL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'varvor', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'varvor',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"varvor->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skontrarvul(self, hint):
        assert self._state.get("current") == SKONTRARVUL, \
            f"spaxglosx.skontrarvul: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skontrarvul', 2:
                self._state["current"] = TRURCLENR
                self._state["trig"]    = "hint:2"
            case 'skontrarvul', 1:
                self._state["current"] = VIMSPIML
                self._state["trig"]    = "hint:1"
            case 'skontrarvul', _:
                self._state["current"] = GRIXSLORR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skontrarvul', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skontrarvul',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skontrarvul->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _grixslorr(self, hint):
        assert self._state.get("current") == GRIXSLORR, \
            f"spaxglosx.grixslorr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'grixslorr', 2:
                self._state["current"] = TRURCLENR
                self._state["trig"]    = "hint:2"
            case 'grixslorr', 0:
                self._state["current"] = PRURFLIX
                self._state["trig"]    = "hint:0"
            case 'grixslorr', _:
                self._state["current"] = VIMSPIML
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'grixslorr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'grixslorr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"grixslorr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _vimspiml(self, hint):
        assert self._state.get("current") == VIMSPIML, \
            f"spaxglosx.vimspiml: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'vimspiml', 2:
                self._state["current"] = TRURCLENR
                self._state["trig"]    = "hint:2"
            case 'vimspiml', _:
                self._state["current"] = TREXBRANDRAXR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'vimspiml', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'vimspiml',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"vimspiml->{_to}", _xid_val)
        self._state["cycle"] += 1

    def invoke(self, hint=None, span=None, caller=None, ctx=None, cycle=0):
        if ctx is None: ctx = {}

        self._state = {"current": DROSKRARR, "ctx": ctx,
                        "span": span, "caller": caller,
                        "trig": "auto", "cycle": cycle}
        _dispatch = {
            DROSKRARR: self._droskrarr,
            CLORSLALL: self._clorslall,
            PRENSTELK: self._prenstelk,
            VULPRAX: self._vulprax,
            TRALDRONX: self._traldronx,
            DRORSPIXFLALT: self._drorspixflalt,
            SKELSKULCLORX: self._skelskulclorx,
            DRONGLELDRENL: self._drongleldrenl,
            TRURSKUR: self._trurskur,
            DREXSPAN: self._drexspan,
            BRENCLIX: self._brenclix,
            SLULSPALX: self._slulspalx,
            SLELKRURK: self._slelkrurk,
            GRULGRURKRIXT: self._grulgrurkrixt,
            FLIMSPON: self._flimspon,
            SKOSPRAXN: self._skospraxn,
            CLULSTALX: self._clulstalx,
            TRELBLARPRIMT: self._trelblarprimt,
            SLENKRULSKOS: self._slenkrulskos,
            FLALKRURBRURN: self._flalkrurbrurn,
            VAXBLAN: self._vaxblan,
            FLAXPRONFLURK: self._flaxpronflurk,
            DRALFLEXSPORL: self._dralflexsporl,
            FLIXGLORR: self._flixglorr,
            STONTRON: self._stontron,
            VIXDRULN: self._vixdruln,
            STALCLAL: self._stalclal,
            VONKRONR: self._vonkronr,
            FLEXGLOSCLAXX: self._flexglosclaxx,
            CLELGLANGRURN: self._clelglangrurn,
            STONSPALR: self._stonspalr,
            VARSKIMKRENT: self._varskimkrent,
            BLONFLANT: self._blonflant,
            VARGRUL: self._vargrul,
            SLOSVEX: self._slosvex,
            BLENBLULSLONT: self._blenblulslont,
            DREXPRANKRIX: self._drexprankrix,
            TRELSLAR: self._trelslar,
            GRELFLARVENN: self._grelflarvenn,
            CLIMBLARGRIM: self._climblargrim,
            CLEXGLURT: self._clexglurt,
            VIXFLENPROS: self._vixflenpros,
            GRANGLALK: self._granglalk,
            DRIXFLIXTRAR: self._drixflixtrar,
            CLAXDRAN: self._claxdran,
            CLENBRONDRIMX: self._clenbrondrimx,
            DRIMSPANTRAL: self._drimspantral,
            STAXSKEN: self._staxsken,
            CLOSCLENGRART: self._closclengrart,
            KRURGLIMT: self._krurglimt,
            BRARGRULL: self._brargrull,
            BRAXBRAX: self._braxbrax,
            KRURPRAX: self._krurprax,
            BLOSSKENK: self._blosskenk,
            GRULFLAN: self._grulflan,
            SKORVULSKAR: self._skorvulskar,
            DRARDRUR: self._drardrur,
            VANSKUR: self._vanskur,
            BLOSTREN: self._blostren,
            SPIMSTOST: self._spimstost,
            SLALBRURL: self._slalbrurl,
            VARVOR: self._varvor,
            SKONTRARVUL: self._skontrarvul,
            GRIXSLORR: self._grixslorr,
            VIMSPIML: self._vimspiml,
        }
        while self._state["current"] not in _R and self._state["cycle"] - cycle < 8000:
            _dispatch[self._state["current"]](hint)
        _ret     = _R.get(self._state["current"], -1)
        _is_err  = self._state["current"] == TRURCLENR
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
    return SpaxglosxFSM().invoke(hint=hint, span=span, caller=caller, ctx=ctx, cycle=cycle)
