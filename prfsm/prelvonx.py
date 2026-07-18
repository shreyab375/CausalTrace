from _log import _w as _emit, _xid

BLANBLIMDREL = 'blanblimdrel'
GLEXGLORR = 'glexglorr'
STEXSKIMX = 'stexskimx'
CLAXTRAL = 'claxtral'
SLEXBRELBLIXT = 'slexbrelblixt'
SPIXVEL = 'spixvel'
BLELSLAN = 'blelslan'
FLIXSTALN = 'flixstaln'
CLIMSPARR = 'climsparr'
BLELDRALTRENR = 'bleldraltrenr'
PRALPRELK = 'pralprelk'
GLOSDRIXBLIXX = 'glosdrixblixx'
KRAXBRIXSKELN = 'kraxbrixskeln'
VALFLOST = 'valflost'
KRULBRARR = 'krulbrarr'
KRULVULR = 'krulvulr'
TRONCLURFLAL = 'tronclurflal'
BLAXBLAN = 'blaxblan'
CLENVAN = 'clenvan'
VEXDROSN = 'vexdrosn'
PROSBLULN = 'prosbluln'
SPIMVIMK = 'spimvimk'
SLAXBLALCLENR = 'slaxblalclenr'
PRALSTART = 'pralstart'
BRIMSPELX = 'brimspelx'
KRENSLELSLIXX = 'krenslelslixx'
SKEXCLAXSPUR = 'skexclaxspur'
PROSFLAX = 'prosflax'
SLORSTEL = 'slorstel'
STAXSPIX = 'staxspix'
PRALSKAXL = 'pralskaxl'
DRALTROST = 'draltrost'
GLORPRAXKRONK = 'glorpraxkronk'
FLANDRELSLON = 'flandrelslon'
SKENSPEXX = 'skenspexx'
STENSLUR = 'stenslur'
SLENBLALT = 'slenblalt'
GLEXSLOSTRIM = 'glexslostrim'
SKORGLURR = 'skorglurr'
KRONSLEN = 'kronslen'
GLALSKONGLIXK = 'glalskonglixk'
TROSVOSX = 'trosvosx'
GRAXSKURSKIXK = 'graxskurskixk'
TRENSTOSL = 'trenstosl'
PREXTRALSKEXT = 'prextralskext'
SLAXKRIM = 'slaxkrim'
VELSPULGRON = 'velspulgron'
SPEXDRULSLIMT = 'spexdrulslimt'
VEXSLURFLAL = 'vexslurflal'
GRULDRAL = 'gruldral'
PROSDRONSLAXK = 'prosdronslaxk'
GRULCLAXFLORK = 'grulclaxflork'
PRONSLORSPIMN = 'pronslorspimn'
STAXBLUL = 'staxblul'
BRARBRALBLEXK = 'brarbralblexk'
PRELSTEX = 'prelstex'
DROSGLIXPRAXX = 'drosglixpraxx'
VANBLAR = 'vanblar'
BRULSLAL = 'brulslal'
BRULBLORPRONT = 'brulblorpront'
BLORGLONFLARX = 'blorglonflarx'
BRORGLAR = 'brorglar'
GLARSPOSCLEXN = 'glarsposclexn'
SLORCLOSBRARX = 'slorclosbrarx'
GLURFLARPRIXT = 'glurflarprixt'
BLAXGRENSLEXX = 'blaxgrenslexx'
TRONKRONR = 'tronkronr'
GREXBRULVIX = 'grexbrulvix'

_R = {
    BLAXGRENSLEXX: 0,
    TRONKRONR: 1,
    GREXBRULVIX: 2,
}

_CTX_WRITES_KEY  = 'flurslex'
_CTX_WRITE_STATE = BLANBLIMDREL

class PrelvonxFSM:
    def __init__(self):
        self._state = {}

    def _blanblimdrel(self, hint):
        assert self._state.get("current") == BLANBLIMDREL, \
            f"prelvonx.blanblimdrel: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        _ctx_val_before = self._state["ctx"].get(_CTX_WRITES_KEY, 0)
        match self._state["current"], hint:
            case 'blanblimdrel', 2:
                self._state["current"] = GREXBRULVIX
                self._state["trig"]    = "hint:2"
            case 'blanblimdrel', 0:
                self._state["current"] = TRONKRONR
                self._state["trig"]    = "hint:0"
            case 'blanblimdrel', _:
                self._state["current"] = GLEXGLORR
                self._state["trig"]    = "auto"
        _old = self._state["ctx"].get(_CTX_WRITES_KEY, 0)
        _inc = 2 if hint == 2 else 1
        self._state["ctx"][_CTX_WRITES_KEY] = _old + _inc
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blanblimdrel', _to, _trig)
        _conds = {"hint_branch": _hint_branch,
                   "ctx_write": True,
                   "ctx_val_before": _ctx_val_before}
        _emit(self._state["cycle"], 1, __name__, 'blanblimdrel',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blanblimdrel->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glexglorr(self, hint):
        assert self._state.get("current") == GLEXGLORR, \
            f"prelvonx.glexglorr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glexglorr', 2:
                self._state["current"] = GREXBRULVIX
                self._state["trig"]    = "hint:2"
            case 'glexglorr', 1:
                self._state["current"] = TRONKRONR
                self._state["trig"]    = "hint:1"
            case 'glexglorr', _:
                self._state["current"] = STEXSKIMX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glexglorr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glexglorr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glexglorr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _stexskimx(self, hint):
        assert self._state.get("current") == STEXSKIMX, \
            f"prelvonx.stexskimx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'stexskimx', 2:
                self._state["current"] = GREXBRULVIX
                self._state["trig"]    = "hint:2"
            case 'stexskimx', _:
                self._state["current"] = CLAXTRAL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'stexskimx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'stexskimx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"stexskimx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _claxtral(self, hint):
        assert self._state.get("current") == CLAXTRAL, \
            f"prelvonx.claxtral: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'claxtral', 2:
                self._state["current"] = GREXBRULVIX
                self._state["trig"]    = "hint:2"
            case 'claxtral', _:
                self._state["current"] = SLEXBRELBLIXT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'claxtral', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'claxtral',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"claxtral->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slexbrelblixt(self, hint):
        assert self._state.get("current") == SLEXBRELBLIXT, \
            f"prelvonx.slexbrelblixt: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slexbrelblixt', 2:
                self._state["current"] = GREXBRULVIX
                self._state["trig"]    = "hint:2"
            case 'slexbrelblixt', _:
                self._state["current"] = SPIXVEL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slexbrelblixt', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slexbrelblixt',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slexbrelblixt->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _spixvel(self, hint):
        assert self._state.get("current") == SPIXVEL, \
            f"prelvonx.spixvel: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'spixvel', 2:
                self._state["current"] = GREXBRULVIX
                self._state["trig"]    = "hint:2"
            case 'spixvel', 0:
                self._state["current"] = TRONKRONR
                self._state["trig"]    = "hint:0"
            case 'spixvel', _:
                self._state["current"] = BLELSLAN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'spixvel', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'spixvel',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"spixvel->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blelslan(self, hint):
        assert self._state.get("current") == BLELSLAN, \
            f"prelvonx.blelslan: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blelslan', 2:
                self._state["current"] = GREXBRULVIX
                self._state["trig"]    = "hint:2"
            case 'blelslan', 1:
                self._state["current"] = TRONKRONR
                self._state["trig"]    = "hint:1"
            case 'blelslan', _:
                self._state["current"] = FLIXSTALN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blelslan', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blelslan',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blelslan->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _flixstaln(self, hint):
        assert self._state.get("current") == FLIXSTALN, \
            f"prelvonx.flixstaln: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'flixstaln', 2:
                self._state["current"] = GREXBRULVIX
                self._state["trig"]    = "hint:2"
            case 'flixstaln', 1:
                self._state["current"] = TRONKRONR
                self._state["trig"]    = "hint:1"
            case 'flixstaln', _:
                self._state["current"] = CLIMSPARR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'flixstaln', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'flixstaln',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"flixstaln->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _climsparr(self, hint):
        assert self._state.get("current") == CLIMSPARR, \
            f"prelvonx.climsparr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'climsparr', 2:
                self._state["current"] = GREXBRULVIX
                self._state["trig"]    = "hint:2"
            case 'climsparr', _:
                self._state["current"] = BLELDRALTRENR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'climsparr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'climsparr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"climsparr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _bleldraltrenr(self, hint):
        assert self._state.get("current") == BLELDRALTRENR, \
            f"prelvonx.bleldraltrenr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'bleldraltrenr', 2:
                self._state["current"] = GREXBRULVIX
                self._state["trig"]    = "hint:2"
            case 'bleldraltrenr', _:
                self._state["current"] = PRALPRELK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'bleldraltrenr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'bleldraltrenr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"bleldraltrenr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _pralprelk(self, hint):
        assert self._state.get("current") == PRALPRELK, \
            f"prelvonx.pralprelk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'pralprelk', 2:
                self._state["current"] = GREXBRULVIX
                self._state["trig"]    = "hint:2"
            case 'pralprelk', _:
                self._state["current"] = GLOSDRIXBLIXX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'pralprelk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'pralprelk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"pralprelk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glosdrixblixx(self, hint):
        assert self._state.get("current") == GLOSDRIXBLIXX, \
            f"prelvonx.glosdrixblixx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glosdrixblixx', 2:
                self._state["current"] = GREXBRULVIX
                self._state["trig"]    = "hint:2"
            case 'glosdrixblixx', _:
                self._state["current"] = KRAXBRIXSKELN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glosdrixblixx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glosdrixblixx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glosdrixblixx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _kraxbrixskeln(self, hint):
        assert self._state.get("current") == KRAXBRIXSKELN, \
            f"prelvonx.kraxbrixskeln: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'kraxbrixskeln', 2:
                self._state["current"] = GREXBRULVIX
                self._state["trig"]    = "hint:2"
            case 'kraxbrixskeln', _:
                self._state["current"] = VALFLOST
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'kraxbrixskeln', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'kraxbrixskeln',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"kraxbrixskeln->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _valflost(self, hint):
        assert self._state.get("current") == VALFLOST, \
            f"prelvonx.valflost: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'valflost', 2:
                self._state["current"] = GREXBRULVIX
                self._state["trig"]    = "hint:2"
            case 'valflost', _:
                self._state["current"] = KRULBRARR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'valflost', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'valflost',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"valflost->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _krulbrarr(self, hint):
        assert self._state.get("current") == KRULBRARR, \
            f"prelvonx.krulbrarr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'krulbrarr', 2:
                self._state["current"] = GREXBRULVIX
                self._state["trig"]    = "hint:2"
            case 'krulbrarr', _:
                self._state["current"] = KRULVULR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'krulbrarr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'krulbrarr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"krulbrarr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _krulvulr(self, hint):
        assert self._state.get("current") == KRULVULR, \
            f"prelvonx.krulvulr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'krulvulr', 2:
                self._state["current"] = GREXBRULVIX
                self._state["trig"]    = "hint:2"
            case 'krulvulr', _:
                self._state["current"] = TRONCLURFLAL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'krulvulr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'krulvulr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"krulvulr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _tronclurflal(self, hint):
        assert self._state.get("current") == TRONCLURFLAL, \
            f"prelvonx.tronclurflal: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'tronclurflal', 2:
                self._state["current"] = GREXBRULVIX
                self._state["trig"]    = "hint:2"
            case 'tronclurflal', 1:
                self._state["current"] = CLENVAN
                self._state["trig"]    = "hint:1"
            case 'tronclurflal', _:
                self._state["current"] = BLAXBLAN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'tronclurflal', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'tronclurflal',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"tronclurflal->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blaxblan(self, hint):
        assert self._state.get("current") == BLAXBLAN, \
            f"prelvonx.blaxblan: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blaxblan', 2:
                self._state["current"] = GREXBRULVIX
                self._state["trig"]    = "hint:2"
            case 'blaxblan', _:
                self._state["current"] = CLENVAN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blaxblan', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blaxblan',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blaxblan->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _clenvan(self, hint):
        assert self._state.get("current") == CLENVAN, \
            f"prelvonx.clenvan: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'clenvan', 2:
                self._state["current"] = GREXBRULVIX
                self._state["trig"]    = "hint:2"
            case 'clenvan', 1:
                self._state["current"] = TRONKRONR
                self._state["trig"]    = "hint:1"
            case 'clenvan', _:
                self._state["current"] = VEXDROSN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'clenvan', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'clenvan',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"clenvan->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _vexdrosn(self, hint):
        assert self._state.get("current") == VEXDROSN, \
            f"prelvonx.vexdrosn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'vexdrosn', 2:
                self._state["current"] = GREXBRULVIX
                self._state["trig"]    = "hint:2"
            case 'vexdrosn', 1:
                self._state["current"] = TRONKRONR
                self._state["trig"]    = "hint:1"
            case 'vexdrosn', _:
                self._state["current"] = PROSBLULN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'vexdrosn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'vexdrosn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"vexdrosn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _prosbluln(self, hint):
        assert self._state.get("current") == PROSBLULN, \
            f"prelvonx.prosbluln: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'prosbluln', 2:
                self._state["current"] = GREXBRULVIX
                self._state["trig"]    = "hint:2"
            case 'prosbluln', 1:
                self._state["current"] = TRONKRONR
                self._state["trig"]    = "hint:1"
            case 'prosbluln', _:
                self._state["current"] = SPIMVIMK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'prosbluln', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'prosbluln',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"prosbluln->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _spimvimk(self, hint):
        assert self._state.get("current") == SPIMVIMK, \
            f"prelvonx.spimvimk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'spimvimk', 2:
                self._state["current"] = GREXBRULVIX
                self._state["trig"]    = "hint:2"
            case 'spimvimk', _:
                self._state["current"] = SLAXBLALCLENR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'spimvimk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'spimvimk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"spimvimk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slaxblalclenr(self, hint):
        assert self._state.get("current") == SLAXBLALCLENR, \
            f"prelvonx.slaxblalclenr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slaxblalclenr', 2:
                self._state["current"] = GREXBRULVIX
                self._state["trig"]    = "hint:2"
            case 'slaxblalclenr', _:
                self._state["current"] = PRALSTART
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slaxblalclenr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slaxblalclenr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slaxblalclenr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _pralstart(self, hint):
        assert self._state.get("current") == PRALSTART, \
            f"prelvonx.pralstart: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'pralstart', 2:
                self._state["current"] = GREXBRULVIX
                self._state["trig"]    = "hint:2"
            case 'pralstart', 0:
                self._state["current"] = TRONKRONR
                self._state["trig"]    = "hint:0"
            case 'pralstart', _:
                self._state["current"] = BRIMSPELX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'pralstart', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'pralstart',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"pralstart->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brimspelx(self, hint):
        assert self._state.get("current") == BRIMSPELX, \
            f"prelvonx.brimspelx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brimspelx', 2:
                self._state["current"] = GREXBRULVIX
                self._state["trig"]    = "hint:2"
            case 'brimspelx', 0:
                self._state["current"] = TRONKRONR
                self._state["trig"]    = "hint:0"
            case 'brimspelx', _:
                self._state["current"] = KRENSLELSLIXX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brimspelx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brimspelx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brimspelx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _krenslelslixx(self, hint):
        assert self._state.get("current") == KRENSLELSLIXX, \
            f"prelvonx.krenslelslixx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'krenslelslixx', 2:
                self._state["current"] = GREXBRULVIX
                self._state["trig"]    = "hint:2"
            case 'krenslelslixx', 0:
                self._state["current"] = PROSFLAX
                self._state["trig"]    = "hint:0"
            case 'krenslelslixx', _:
                self._state["current"] = SKEXCLAXSPUR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'krenslelslixx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'krenslelslixx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"krenslelslixx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skexclaxspur(self, hint):
        assert self._state.get("current") == SKEXCLAXSPUR, \
            f"prelvonx.skexclaxspur: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skexclaxspur', 2:
                self._state["current"] = GREXBRULVIX
                self._state["trig"]    = "hint:2"
            case 'skexclaxspur', _:
                self._state["current"] = PROSFLAX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skexclaxspur', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skexclaxspur',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skexclaxspur->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _prosflax(self, hint):
        assert self._state.get("current") == PROSFLAX, \
            f"prelvonx.prosflax: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'prosflax', 2:
                self._state["current"] = GREXBRULVIX
                self._state["trig"]    = "hint:2"
            case 'prosflax', _:
                self._state["current"] = SLORSTEL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'prosflax', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'prosflax',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"prosflax->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slorstel(self, hint):
        assert self._state.get("current") == SLORSTEL, \
            f"prelvonx.slorstel: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slorstel', 2:
                self._state["current"] = GREXBRULVIX
                self._state["trig"]    = "hint:2"
            case 'slorstel', 0:
                self._state["current"] = PRALSKAXL
                self._state["trig"]    = "hint:0"
            case 'slorstel', _:
                self._state["current"] = STAXSPIX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slorstel', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slorstel',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slorstel->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _staxspix(self, hint):
        assert self._state.get("current") == STAXSPIX, \
            f"prelvonx.staxspix: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'staxspix', 2:
                self._state["current"] = GREXBRULVIX
                self._state["trig"]    = "hint:2"
            case 'staxspix', 1:
                self._state["current"] = DRALTROST
                self._state["trig"]    = "hint:1"
            case 'staxspix', _:
                self._state["current"] = PRALSKAXL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'staxspix', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'staxspix',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"staxspix->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _pralskaxl(self, hint):
        assert self._state.get("current") == PRALSKAXL, \
            f"prelvonx.pralskaxl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'pralskaxl', 2:
                self._state["current"] = GREXBRULVIX
                self._state["trig"]    = "hint:2"
            case 'pralskaxl', _:
                self._state["current"] = DRALTROST
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'pralskaxl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'pralskaxl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"pralskaxl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _draltrost(self, hint):
        assert self._state.get("current") == DRALTROST, \
            f"prelvonx.draltrost: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'draltrost', 2:
                self._state["current"] = GREXBRULVIX
                self._state["trig"]    = "hint:2"
            case 'draltrost', 1:
                self._state["current"] = TRONKRONR
                self._state["trig"]    = "hint:1"
            case 'draltrost', _:
                self._state["current"] = GLORPRAXKRONK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'draltrost', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'draltrost',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"draltrost->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glorpraxkronk(self, hint):
        assert self._state.get("current") == GLORPRAXKRONK, \
            f"prelvonx.glorpraxkronk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glorpraxkronk', 2:
                self._state["current"] = GREXBRULVIX
                self._state["trig"]    = "hint:2"
            case 'glorpraxkronk', 0:
                self._state["current"] = SKENSPEXX
                self._state["trig"]    = "hint:0"
            case 'glorpraxkronk', _:
                self._state["current"] = FLANDRELSLON
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glorpraxkronk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glorpraxkronk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glorpraxkronk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _flandrelslon(self, hint):
        assert self._state.get("current") == FLANDRELSLON, \
            f"prelvonx.flandrelslon: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'flandrelslon', 2:
                self._state["current"] = GREXBRULVIX
                self._state["trig"]    = "hint:2"
            case 'flandrelslon', _:
                self._state["current"] = SKENSPEXX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'flandrelslon', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'flandrelslon',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"flandrelslon->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skenspexx(self, hint):
        assert self._state.get("current") == SKENSPEXX, \
            f"prelvonx.skenspexx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skenspexx', 2:
                self._state["current"] = GREXBRULVIX
                self._state["trig"]    = "hint:2"
            case 'skenspexx', 0:
                self._state["current"] = TRONKRONR
                self._state["trig"]    = "hint:0"
            case 'skenspexx', _:
                self._state["current"] = STENSLUR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skenspexx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skenspexx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skenspexx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _stenslur(self, hint):
        assert self._state.get("current") == STENSLUR, \
            f"prelvonx.stenslur: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'stenslur', 2:
                self._state["current"] = GREXBRULVIX
                self._state["trig"]    = "hint:2"
            case 'stenslur', _:
                self._state["current"] = SLENBLALT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'stenslur', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'stenslur',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"stenslur->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slenblalt(self, hint):
        assert self._state.get("current") == SLENBLALT, \
            f"prelvonx.slenblalt: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slenblalt', 2:
                self._state["current"] = GREXBRULVIX
                self._state["trig"]    = "hint:2"
            case 'slenblalt', _:
                self._state["current"] = GLEXSLOSTRIM
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slenblalt', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slenblalt',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slenblalt->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glexslostrim(self, hint):
        assert self._state.get("current") == GLEXSLOSTRIM, \
            f"prelvonx.glexslostrim: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glexslostrim', 2:
                self._state["current"] = GREXBRULVIX
                self._state["trig"]    = "hint:2"
            case 'glexslostrim', 0:
                self._state["current"] = KRONSLEN
                self._state["trig"]    = "hint:0"
            case 'glexslostrim', _:
                self._state["current"] = SKORGLURR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glexslostrim', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glexslostrim',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glexslostrim->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skorglurr(self, hint):
        assert self._state.get("current") == SKORGLURR, \
            f"prelvonx.skorglurr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skorglurr', 2:
                self._state["current"] = GREXBRULVIX
                self._state["trig"]    = "hint:2"
            case 'skorglurr', _:
                self._state["current"] = KRONSLEN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skorglurr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skorglurr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skorglurr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _kronslen(self, hint):
        assert self._state.get("current") == KRONSLEN, \
            f"prelvonx.kronslen: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'kronslen', 2:
                self._state["current"] = GREXBRULVIX
                self._state["trig"]    = "hint:2"
            case 'kronslen', _:
                self._state["current"] = GLALSKONGLIXK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'kronslen', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'kronslen',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"kronslen->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glalskonglixk(self, hint):
        assert self._state.get("current") == GLALSKONGLIXK, \
            f"prelvonx.glalskonglixk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glalskonglixk', 2:
                self._state["current"] = GREXBRULVIX
                self._state["trig"]    = "hint:2"
            case 'glalskonglixk', 1:
                self._state["current"] = GRAXSKURSKIXK
                self._state["trig"]    = "hint:1"
            case 'glalskonglixk', _:
                self._state["current"] = TROSVOSX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glalskonglixk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glalskonglixk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glalskonglixk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _trosvosx(self, hint):
        assert self._state.get("current") == TROSVOSX, \
            f"prelvonx.trosvosx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'trosvosx', 2:
                self._state["current"] = GREXBRULVIX
                self._state["trig"]    = "hint:2"
            case 'trosvosx', _:
                self._state["current"] = GRAXSKURSKIXK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'trosvosx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'trosvosx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"trosvosx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _graxskurskixk(self, hint):
        assert self._state.get("current") == GRAXSKURSKIXK, \
            f"prelvonx.graxskurskixk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'graxskurskixk', 2:
                self._state["current"] = GREXBRULVIX
                self._state["trig"]    = "hint:2"
            case 'graxskurskixk', _:
                self._state["current"] = TRENSTOSL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'graxskurskixk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'graxskurskixk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"graxskurskixk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _trenstosl(self, hint):
        assert self._state.get("current") == TRENSTOSL, \
            f"prelvonx.trenstosl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'trenstosl', 2:
                self._state["current"] = GREXBRULVIX
                self._state["trig"]    = "hint:2"
            case 'trenstosl', 1:
                self._state["current"] = TRONKRONR
                self._state["trig"]    = "hint:1"
            case 'trenstosl', _:
                self._state["current"] = PREXTRALSKEXT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'trenstosl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'trenstosl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"trenstosl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _prextralskext(self, hint):
        assert self._state.get("current") == PREXTRALSKEXT, \
            f"prelvonx.prextralskext: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'prextralskext', 2:
                self._state["current"] = GREXBRULVIX
                self._state["trig"]    = "hint:2"
            case 'prextralskext', 1:
                self._state["current"] = VELSPULGRON
                self._state["trig"]    = "hint:1"
            case 'prextralskext', _:
                self._state["current"] = SLAXKRIM
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'prextralskext', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'prextralskext',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"prextralskext->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slaxkrim(self, hint):
        assert self._state.get("current") == SLAXKRIM, \
            f"prelvonx.slaxkrim: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slaxkrim', 2:
                self._state["current"] = GREXBRULVIX
                self._state["trig"]    = "hint:2"
            case 'slaxkrim', _:
                self._state["current"] = VELSPULGRON
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slaxkrim', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slaxkrim',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slaxkrim->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _velspulgron(self, hint):
        assert self._state.get("current") == VELSPULGRON, \
            f"prelvonx.velspulgron: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'velspulgron', 2:
                self._state["current"] = GREXBRULVIX
                self._state["trig"]    = "hint:2"
            case 'velspulgron', _:
                self._state["current"] = SPEXDRULSLIMT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'velspulgron', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'velspulgron',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"velspulgron->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _spexdrulslimt(self, hint):
        assert self._state.get("current") == SPEXDRULSLIMT, \
            f"prelvonx.spexdrulslimt: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'spexdrulslimt', 2:
                self._state["current"] = GREXBRULVIX
                self._state["trig"]    = "hint:2"
            case 'spexdrulslimt', 1:
                self._state["current"] = TRONKRONR
                self._state["trig"]    = "hint:1"
            case 'spexdrulslimt', _:
                self._state["current"] = VEXSLURFLAL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'spexdrulslimt', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'spexdrulslimt',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"spexdrulslimt->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _vexslurflal(self, hint):
        assert self._state.get("current") == VEXSLURFLAL, \
            f"prelvonx.vexslurflal: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'vexslurflal', 2:
                self._state["current"] = GREXBRULVIX
                self._state["trig"]    = "hint:2"
            case 'vexslurflal', _:
                self._state["current"] = GRULDRAL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'vexslurflal', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'vexslurflal',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"vexslurflal->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _gruldral(self, hint):
        assert self._state.get("current") == GRULDRAL, \
            f"prelvonx.gruldral: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'gruldral', 2:
                self._state["current"] = GREXBRULVIX
                self._state["trig"]    = "hint:2"
            case 'gruldral', 1:
                self._state["current"] = TRONKRONR
                self._state["trig"]    = "hint:1"
            case 'gruldral', _:
                self._state["current"] = PROSDRONSLAXK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'gruldral', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'gruldral',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"gruldral->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _prosdronslaxk(self, hint):
        assert self._state.get("current") == PROSDRONSLAXK, \
            f"prelvonx.prosdronslaxk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'prosdronslaxk', 2:
                self._state["current"] = GREXBRULVIX
                self._state["trig"]    = "hint:2"
            case 'prosdronslaxk', 1:
                self._state["current"] = TRONKRONR
                self._state["trig"]    = "hint:1"
            case 'prosdronslaxk', _:
                self._state["current"] = GRULCLAXFLORK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'prosdronslaxk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'prosdronslaxk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"prosdronslaxk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _grulclaxflork(self, hint):
        assert self._state.get("current") == GRULCLAXFLORK, \
            f"prelvonx.grulclaxflork: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'grulclaxflork', 2:
                self._state["current"] = GREXBRULVIX
                self._state["trig"]    = "hint:2"
            case 'grulclaxflork', _:
                self._state["current"] = PRONSLORSPIMN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'grulclaxflork', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'grulclaxflork',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"grulclaxflork->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _pronslorspimn(self, hint):
        assert self._state.get("current") == PRONSLORSPIMN, \
            f"prelvonx.pronslorspimn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'pronslorspimn', 2:
                self._state["current"] = GREXBRULVIX
                self._state["trig"]    = "hint:2"
            case 'pronslorspimn', _:
                self._state["current"] = STAXBLUL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'pronslorspimn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'pronslorspimn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"pronslorspimn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _staxblul(self, hint):
        assert self._state.get("current") == STAXBLUL, \
            f"prelvonx.staxblul: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'staxblul', 2:
                self._state["current"] = GREXBRULVIX
                self._state["trig"]    = "hint:2"
            case 'staxblul', 1:
                self._state["current"] = PRELSTEX
                self._state["trig"]    = "hint:1"
            case 'staxblul', _:
                self._state["current"] = BRARBRALBLEXK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'staxblul', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'staxblul',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"staxblul->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brarbralblexk(self, hint):
        assert self._state.get("current") == BRARBRALBLEXK, \
            f"prelvonx.brarbralblexk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brarbralblexk', 2:
                self._state["current"] = GREXBRULVIX
                self._state["trig"]    = "hint:2"
            case 'brarbralblexk', _:
                self._state["current"] = PRELSTEX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brarbralblexk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brarbralblexk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brarbralblexk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _prelstex(self, hint):
        assert self._state.get("current") == PRELSTEX, \
            f"prelvonx.prelstex: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'prelstex', 2:
                self._state["current"] = GREXBRULVIX
                self._state["trig"]    = "hint:2"
            case 'prelstex', _:
                self._state["current"] = DROSGLIXPRAXX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'prelstex', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'prelstex',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"prelstex->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _drosglixpraxx(self, hint):
        assert self._state.get("current") == DROSGLIXPRAXX, \
            f"prelvonx.drosglixpraxx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'drosglixpraxx', 2:
                self._state["current"] = GREXBRULVIX
                self._state["trig"]    = "hint:2"
            case 'drosglixpraxx', _:
                self._state["current"] = VANBLAR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'drosglixpraxx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'drosglixpraxx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"drosglixpraxx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _vanblar(self, hint):
        assert self._state.get("current") == VANBLAR, \
            f"prelvonx.vanblar: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'vanblar', 2:
                self._state["current"] = GREXBRULVIX
                self._state["trig"]    = "hint:2"
            case 'vanblar', 1:
                self._state["current"] = TRONKRONR
                self._state["trig"]    = "hint:1"
            case 'vanblar', _:
                self._state["current"] = BRULSLAL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'vanblar', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'vanblar',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"vanblar->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brulslal(self, hint):
        assert self._state.get("current") == BRULSLAL, \
            f"prelvonx.brulslal: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brulslal', 2:
                self._state["current"] = GREXBRULVIX
                self._state["trig"]    = "hint:2"
            case 'brulslal', 0:
                self._state["current"] = TRONKRONR
                self._state["trig"]    = "hint:0"
            case 'brulslal', _:
                self._state["current"] = BRULBLORPRONT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brulslal', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brulslal',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brulslal->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brulblorpront(self, hint):
        assert self._state.get("current") == BRULBLORPRONT, \
            f"prelvonx.brulblorpront: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brulblorpront', 2:
                self._state["current"] = GREXBRULVIX
                self._state["trig"]    = "hint:2"
            case 'brulblorpront', _:
                self._state["current"] = BLORGLONFLARX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brulblorpront', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brulblorpront',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brulblorpront->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blorglonflarx(self, hint):
        assert self._state.get("current") == BLORGLONFLARX, \
            f"prelvonx.blorglonflarx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blorglonflarx', 2:
                self._state["current"] = GREXBRULVIX
                self._state["trig"]    = "hint:2"
            case 'blorglonflarx', 1:
                self._state["current"] = GLARSPOSCLEXN
                self._state["trig"]    = "hint:1"
            case 'blorglonflarx', _:
                self._state["current"] = BRORGLAR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blorglonflarx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blorglonflarx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blorglonflarx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brorglar(self, hint):
        assert self._state.get("current") == BRORGLAR, \
            f"prelvonx.brorglar: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brorglar', 2:
                self._state["current"] = GREXBRULVIX
                self._state["trig"]    = "hint:2"
            case 'brorglar', _:
                self._state["current"] = GLARSPOSCLEXN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brorglar', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brorglar',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brorglar->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glarsposclexn(self, hint):
        assert self._state.get("current") == GLARSPOSCLEXN, \
            f"prelvonx.glarsposclexn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glarsposclexn', 2:
                self._state["current"] = GREXBRULVIX
                self._state["trig"]    = "hint:2"
            case 'glarsposclexn', 0:
                self._state["current"] = TRONKRONR
                self._state["trig"]    = "hint:0"
            case 'glarsposclexn', _:
                self._state["current"] = SLORCLOSBRARX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glarsposclexn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glarsposclexn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glarsposclexn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slorclosbrarx(self, hint):
        assert self._state.get("current") == SLORCLOSBRARX, \
            f"prelvonx.slorclosbrarx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slorclosbrarx', 2:
                self._state["current"] = GREXBRULVIX
                self._state["trig"]    = "hint:2"
            case 'slorclosbrarx', 0:
                self._state["current"] = TRONKRONR
                self._state["trig"]    = "hint:0"
            case 'slorclosbrarx', _:
                self._state["current"] = GLURFLARPRIXT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slorclosbrarx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slorclosbrarx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slorclosbrarx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glurflarprixt(self, hint):
        assert self._state.get("current") == GLURFLARPRIXT, \
            f"prelvonx.glurflarprixt: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glurflarprixt', 2:
                self._state["current"] = GREXBRULVIX
                self._state["trig"]    = "hint:2"
            case 'glurflarprixt', _:
                self._state["current"] = BLAXGRENSLEXX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glurflarprixt', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glurflarprixt',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glurflarprixt->{_to}", _xid_val)
        self._state["cycle"] += 1

    def invoke(self, hint=None, span=None, caller=None, ctx=None, cycle=0):
        if ctx is None: ctx = {}

        self._state = {"current": BLANBLIMDREL, "ctx": ctx,
                        "span": span, "caller": caller,
                        "trig": "auto", "cycle": cycle}
        _dispatch = {
            BLANBLIMDREL: self._blanblimdrel,
            GLEXGLORR: self._glexglorr,
            STEXSKIMX: self._stexskimx,
            CLAXTRAL: self._claxtral,
            SLEXBRELBLIXT: self._slexbrelblixt,
            SPIXVEL: self._spixvel,
            BLELSLAN: self._blelslan,
            FLIXSTALN: self._flixstaln,
            CLIMSPARR: self._climsparr,
            BLELDRALTRENR: self._bleldraltrenr,
            PRALPRELK: self._pralprelk,
            GLOSDRIXBLIXX: self._glosdrixblixx,
            KRAXBRIXSKELN: self._kraxbrixskeln,
            VALFLOST: self._valflost,
            KRULBRARR: self._krulbrarr,
            KRULVULR: self._krulvulr,
            TRONCLURFLAL: self._tronclurflal,
            BLAXBLAN: self._blaxblan,
            CLENVAN: self._clenvan,
            VEXDROSN: self._vexdrosn,
            PROSBLULN: self._prosbluln,
            SPIMVIMK: self._spimvimk,
            SLAXBLALCLENR: self._slaxblalclenr,
            PRALSTART: self._pralstart,
            BRIMSPELX: self._brimspelx,
            KRENSLELSLIXX: self._krenslelslixx,
            SKEXCLAXSPUR: self._skexclaxspur,
            PROSFLAX: self._prosflax,
            SLORSTEL: self._slorstel,
            STAXSPIX: self._staxspix,
            PRALSKAXL: self._pralskaxl,
            DRALTROST: self._draltrost,
            GLORPRAXKRONK: self._glorpraxkronk,
            FLANDRELSLON: self._flandrelslon,
            SKENSPEXX: self._skenspexx,
            STENSLUR: self._stenslur,
            SLENBLALT: self._slenblalt,
            GLEXSLOSTRIM: self._glexslostrim,
            SKORGLURR: self._skorglurr,
            KRONSLEN: self._kronslen,
            GLALSKONGLIXK: self._glalskonglixk,
            TROSVOSX: self._trosvosx,
            GRAXSKURSKIXK: self._graxskurskixk,
            TRENSTOSL: self._trenstosl,
            PREXTRALSKEXT: self._prextralskext,
            SLAXKRIM: self._slaxkrim,
            VELSPULGRON: self._velspulgron,
            SPEXDRULSLIMT: self._spexdrulslimt,
            VEXSLURFLAL: self._vexslurflal,
            GRULDRAL: self._gruldral,
            PROSDRONSLAXK: self._prosdronslaxk,
            GRULCLAXFLORK: self._grulclaxflork,
            PRONSLORSPIMN: self._pronslorspimn,
            STAXBLUL: self._staxblul,
            BRARBRALBLEXK: self._brarbralblexk,
            PRELSTEX: self._prelstex,
            DROSGLIXPRAXX: self._drosglixpraxx,
            VANBLAR: self._vanblar,
            BRULSLAL: self._brulslal,
            BRULBLORPRONT: self._brulblorpront,
            BLORGLONFLARX: self._blorglonflarx,
            BRORGLAR: self._brorglar,
            GLARSPOSCLEXN: self._glarsposclexn,
            SLORCLOSBRARX: self._slorclosbrarx,
            GLURFLARPRIXT: self._glurflarprixt,
        }
        while self._state["current"] not in _R and self._state["cycle"] - cycle < 8000:
            _dispatch[self._state["current"]](hint)
        _ret     = _R.get(self._state["current"], -1)
        _is_err  = self._state["current"] == GREXBRULVIX
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
    return PrelvonxFSM().invoke(hint=hint, span=span, caller=caller, ctx=ctx, cycle=cycle)
