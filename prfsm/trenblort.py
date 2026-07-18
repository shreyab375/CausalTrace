from _log import _w as _emit, _xid

BROSCLARK = 'brosclark'
PRULSTULN = 'prulstuln'
PRARFLENK = 'prarflenk'
STAXGLENBRALX = 'staxglenbralx'
SPENSPULT = 'spenspult'
FLONBRIXTREXN = 'flonbrixtrexn'
DRULBLIX = 'drulblix'
KROSKRURGLON = 'kroskrurglon'
GRURBLULSLIML = 'grurblulsliml'
PRALPRUR = 'pralprur'
BLOSTRARGLARR = 'blostrarglarr'
SLOSKRULN = 'sloskruln'
GLARPRORPRELK = 'glarprorprelk'
TRULBLALVIMN = 'trulblalvimn'
SPIMCLUL = 'spimclul'
SPIXKRIMPRAR = 'spixkrimprar'
VONSPURPRUL = 'vonspurprul'
SKORBREN = 'skorbren'
KRARSLON = 'krarslon'
KRAXDRANBLIMX = 'kraxdranblimx'
BLURKRARFLALN = 'blurkrarflaln'
SKORBLARCLELT = 'skorblarclelt'
SKEXBROSTREL = 'skexbrostrel'
SLONFLELCLUR = 'slonflelclur'
BRARSKONR = 'brarskonr'
GRULCLEX = 'grulclex'
TRURDRELKROSN = 'trurdrelkrosn'
CLORGRUL = 'clorgrul'
SLIXGLART = 'slixglart'
PRONDRARSLONX = 'prondrarslonx'
GRAXCLARGRURL = 'graxclargrurl'
SPANGLORKREXX = 'spanglorkrexx'
SPENCLAXSTONK = 'spenclaxstonk'
BRONBRALSTOR = 'bronbralstor'
KRIMSTOSK = 'krimstosk'
VOSBLIMN = 'vosblimn'
STENCLEX = 'stenclex'
BRIMSLORGRALN = 'brimslorgraln'
FLENTROSSLAR = 'flentrosslar'
KRARSLULVAL = 'krarslulval'
BLAXBLIXKRAX = 'blaxblixkrax'
PRIXGRARK = 'prixgrark'
SKONSKOS = 'skonskos'
CLIXGRALK = 'clixgralk'
GLANBRIMX = 'glanbrimx'
GLONKRONSLAL = 'glonkronslal'
CLONBRORN = 'clonbrorn'
FLAXDRONBLON = 'flaxdronblon'
SLORFLAXX = 'slorflaxx'
SPURSPARN = 'spursparn'
GRURPRELT = 'grurprelt'
DRARBLELFLIMR = 'drarblelflimr'
SPANSPULSKEL = 'spanspulskel'
GLALBLIMGLAL = 'glalblimglal'
VAXGLULSPAXX = 'vaxglulspaxx'
FLARFLAXPRAXN = 'flarflaxpraxn'
GRAXPREXK = 'graxprexk'
DRURKRARVEN = 'drurkrarven'
BRORKRELGLUL = 'brorkrelglul'
SLOSBREN = 'slosbren'
BLURDRURL = 'blurdrurl'
GRURFLARDRALN = 'grurflardraln'
SPALKRENR = 'spalkrenr'
SKORSPALN = 'skorspaln'
PRIMGLULGLONL = 'primglulglonl'
SLOSSKAXGRORK = 'slosskaxgrork'
SKONGRARSTUL = 'skongrarstul'
VURTRANTREN = 'vurtrantren'

_R = {
    SLOSSKAXGRORK: 0,
    SKONGRARSTUL: 1,
    VURTRANTREN: 2,
}

_CTX_READS_KEY = 'flurslex'
_CTX_THRESHOLD = 16

class TrenblortFSM:
    def __init__(self):
        self._state = {}

    def _brosclark(self, hint):
        assert self._state.get("current") == BROSCLARK, \
            f"trenblort.brosclark: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brosclark', 2:
                self._state["current"] = VURTRANTREN
                self._state["trig"]    = "hint:2"
            case 'brosclark', 1:
                self._state["current"] = SKONGRARSTUL
                self._state["trig"]    = "hint:1"
            case 'brosclark', _:
                self._state["current"] = PRULSTULN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brosclark', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brosclark',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brosclark->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _prulstuln(self, hint):
        assert self._state.get("current") == PRULSTULN, \
            f"trenblort.prulstuln: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'prulstuln', 2:
                self._state["current"] = VURTRANTREN
                self._state["trig"]    = "hint:2"
            case 'prulstuln', 0:
                self._state["current"] = STAXGLENBRALX
                self._state["trig"]    = "hint:0"
            case 'prulstuln', _:
                self._state["current"] = PRARFLENK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'prulstuln', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'prulstuln',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"prulstuln->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _prarflenk(self, hint):
        assert self._state.get("current") == PRARFLENK, \
            f"trenblort.prarflenk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'prarflenk', 2:
                self._state["current"] = VURTRANTREN
                self._state["trig"]    = "hint:2"
            case 'prarflenk', _:
                self._state["current"] = STAXGLENBRALX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'prarflenk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'prarflenk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"prarflenk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _staxglenbralx(self, hint):
        assert self._state.get("current") == STAXGLENBRALX, \
            f"trenblort.staxglenbralx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'staxglenbralx', 2:
                self._state["current"] = VURTRANTREN
                self._state["trig"]    = "hint:2"
            case 'staxglenbralx', 1:
                self._state["current"] = FLONBRIXTREXN
                self._state["trig"]    = "hint:1"
            case 'staxglenbralx', _:
                self._state["current"] = SPENSPULT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'staxglenbralx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'staxglenbralx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"staxglenbralx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _spenspult(self, hint):
        assert self._state.get("current") == SPENSPULT, \
            f"trenblort.spenspult: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'spenspult', 2:
                self._state["current"] = VURTRANTREN
                self._state["trig"]    = "hint:2"
            case 'spenspult', 1:
                self._state["current"] = SKONGRARSTUL
                self._state["trig"]    = "hint:1"
            case 'spenspult', _:
                self._state["current"] = FLONBRIXTREXN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'spenspult', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'spenspult',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"spenspult->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _flonbrixtrexn(self, hint):
        assert self._state.get("current") == FLONBRIXTREXN, \
            f"trenblort.flonbrixtrexn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'flonbrixtrexn', 2:
                self._state["current"] = VURTRANTREN
                self._state["trig"]    = "hint:2"
            case 'flonbrixtrexn', _:
                self._state["current"] = DRULBLIX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'flonbrixtrexn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'flonbrixtrexn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"flonbrixtrexn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _drulblix(self, hint):
        assert self._state.get("current") == DRULBLIX, \
            f"trenblort.drulblix: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'drulblix', 2:
                self._state["current"] = VURTRANTREN
                self._state["trig"]    = "hint:2"
            case 'drulblix', _:
                self._state["current"] = KROSKRURGLON
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'drulblix', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'drulblix',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"drulblix->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _kroskrurglon(self, hint):
        assert self._state.get("current") == KROSKRURGLON, \
            f"trenblort.kroskrurglon: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'kroskrurglon', 2:
                self._state["current"] = VURTRANTREN
                self._state["trig"]    = "hint:2"
            case 'kroskrurglon', _:
                self._state["current"] = GRURBLULSLIML
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'kroskrurglon', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'kroskrurglon',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"kroskrurglon->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _grurblulsliml(self, hint):
        assert self._state.get("current") == GRURBLULSLIML, \
            f"trenblort.grurblulsliml: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'grurblulsliml', 2:
                self._state["current"] = VURTRANTREN
                self._state["trig"]    = "hint:2"
            case 'grurblulsliml', _:
                self._state["current"] = PRALPRUR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'grurblulsliml', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'grurblulsliml',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"grurblulsliml->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _pralprur(self, hint):
        assert self._state.get("current") == PRALPRUR, \
            f"trenblort.pralprur: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'pralprur', 2:
                self._state["current"] = VURTRANTREN
                self._state["trig"]    = "hint:2"
            case 'pralprur', 1:
                self._state["current"] = SLOSKRULN
                self._state["trig"]    = "hint:1"
            case 'pralprur', _:
                self._state["current"] = BLOSTRARGLARR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'pralprur', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'pralprur',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"pralprur->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blostrarglarr(self, hint):
        assert self._state.get("current") == BLOSTRARGLARR, \
            f"trenblort.blostrarglarr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blostrarglarr', 2:
                self._state["current"] = VURTRANTREN
                self._state["trig"]    = "hint:2"
            case 'blostrarglarr', 0:
                self._state["current"] = SKONGRARSTUL
                self._state["trig"]    = "hint:0"
            case 'blostrarglarr', _:
                self._state["current"] = SLOSKRULN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blostrarglarr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blostrarglarr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blostrarglarr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _sloskruln(self, hint):
        assert self._state.get("current") == SLOSKRULN, \
            f"trenblort.sloskruln: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'sloskruln', 2:
                self._state["current"] = VURTRANTREN
                self._state["trig"]    = "hint:2"
            case 'sloskruln', _:
                self._state["current"] = GLARPRORPRELK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'sloskruln', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'sloskruln',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"sloskruln->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glarprorprelk(self, hint):
        assert self._state.get("current") == GLARPRORPRELK, \
            f"trenblort.glarprorprelk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glarprorprelk', 2:
                self._state["current"] = VURTRANTREN
                self._state["trig"]    = "hint:2"
            case 'glarprorprelk', _:
                self._state["current"] = TRULBLALVIMN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glarprorprelk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glarprorprelk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glarprorprelk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _trulblalvimn(self, hint):
        assert self._state.get("current") == TRULBLALVIMN, \
            f"trenblort.trulblalvimn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'trulblalvimn', 2:
                self._state["current"] = VURTRANTREN
                self._state["trig"]    = "hint:2"
            case 'trulblalvimn', _:
                self._state["current"] = SPIMCLUL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'trulblalvimn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'trulblalvimn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"trulblalvimn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _spimclul(self, hint):
        assert self._state.get("current") == SPIMCLUL, \
            f"trenblort.spimclul: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'spimclul', 2:
                self._state["current"] = VURTRANTREN
                self._state["trig"]    = "hint:2"
            case 'spimclul', _:
                self._state["current"] = SPIXKRIMPRAR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'spimclul', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'spimclul',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"spimclul->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _spixkrimprar(self, hint):
        assert self._state.get("current") == SPIXKRIMPRAR, \
            f"trenblort.spixkrimprar: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'spixkrimprar', 2:
                self._state["current"] = VURTRANTREN
                self._state["trig"]    = "hint:2"
            case 'spixkrimprar', _:
                self._state["current"] = VONSPURPRUL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'spixkrimprar', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'spixkrimprar',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"spixkrimprar->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _vonspurprul(self, hint):
        assert self._state.get("current") == VONSPURPRUL, \
            f"trenblort.vonspurprul: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'vonspurprul', 2:
                self._state["current"] = VURTRANTREN
                self._state["trig"]    = "hint:2"
            case 'vonspurprul', _:
                self._state["current"] = SKORBREN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'vonspurprul', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'vonspurprul',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"vonspurprul->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skorbren(self, hint):
        assert self._state.get("current") == SKORBREN, \
            f"trenblort.skorbren: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skorbren', 2:
                self._state["current"] = VURTRANTREN
                self._state["trig"]    = "hint:2"
            case 'skorbren', 1:
                self._state["current"] = KRAXDRANBLIMX
                self._state["trig"]    = "hint:1"
            case 'skorbren', _:
                self._state["current"] = KRARSLON
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skorbren', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skorbren',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skorbren->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _krarslon(self, hint):
        assert self._state.get("current") == KRARSLON, \
            f"trenblort.krarslon: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'krarslon', 2:
                self._state["current"] = VURTRANTREN
                self._state["trig"]    = "hint:2"
            case 'krarslon', 1:
                self._state["current"] = BLURKRARFLALN
                self._state["trig"]    = "hint:1"
            case 'krarslon', _:
                self._state["current"] = KRAXDRANBLIMX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'krarslon', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'krarslon',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"krarslon->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _kraxdranblimx(self, hint):
        assert self._state.get("current") == KRAXDRANBLIMX, \
            f"trenblort.kraxdranblimx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'kraxdranblimx', 2:
                self._state["current"] = VURTRANTREN
                self._state["trig"]    = "hint:2"
            case 'kraxdranblimx', 1:
                self._state["current"] = SKONGRARSTUL
                self._state["trig"]    = "hint:1"
            case 'kraxdranblimx', _:
                self._state["current"] = BLURKRARFLALN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'kraxdranblimx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'kraxdranblimx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"kraxdranblimx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blurkrarflaln(self, hint):
        assert self._state.get("current") == BLURKRARFLALN, \
            f"trenblort.blurkrarflaln: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blurkrarflaln', 2:
                self._state["current"] = VURTRANTREN
                self._state["trig"]    = "hint:2"
            case 'blurkrarflaln', _:
                self._state["current"] = SKORBLARCLELT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blurkrarflaln', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blurkrarflaln',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blurkrarflaln->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skorblarclelt(self, hint):
        assert self._state.get("current") == SKORBLARCLELT, \
            f"trenblort.skorblarclelt: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skorblarclelt', 2:
                self._state["current"] = VURTRANTREN
                self._state["trig"]    = "hint:2"
            case 'skorblarclelt', 1:
                self._state["current"] = SLONFLELCLUR
                self._state["trig"]    = "hint:1"
            case 'skorblarclelt', _:
                self._state["current"] = SKEXBROSTREL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skorblarclelt', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skorblarclelt',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skorblarclelt->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skexbrostrel(self, hint):
        assert self._state.get("current") == SKEXBROSTREL, \
            f"trenblort.skexbrostrel: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skexbrostrel', 2:
                self._state["current"] = VURTRANTREN
                self._state["trig"]    = "hint:2"
            case 'skexbrostrel', 0:
                self._state["current"] = SKONGRARSTUL
                self._state["trig"]    = "hint:0"
            case 'skexbrostrel', _:
                self._state["current"] = SLONFLELCLUR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skexbrostrel', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skexbrostrel',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skexbrostrel->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slonflelclur(self, hint):
        assert self._state.get("current") == SLONFLELCLUR, \
            f"trenblort.slonflelclur: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slonflelclur', 2:
                self._state["current"] = VURTRANTREN
                self._state["trig"]    = "hint:2"
            case 'slonflelclur', _:
                self._state["current"] = BRARSKONR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slonflelclur', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slonflelclur',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slonflelclur->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brarskonr(self, hint):
        assert self._state.get("current") == BRARSKONR, \
            f"trenblort.brarskonr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brarskonr', 2:
                self._state["current"] = VURTRANTREN
                self._state["trig"]    = "hint:2"
            case 'brarskonr', _:
                self._state["current"] = GRULCLEX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brarskonr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brarskonr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brarskonr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _grulclex(self, hint):
        assert self._state.get("current") == GRULCLEX, \
            f"trenblort.grulclex: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'grulclex', 2:
                self._state["current"] = VURTRANTREN
                self._state["trig"]    = "hint:2"
            case 'grulclex', _:
                self._state["current"] = TRURDRELKROSN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'grulclex', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'grulclex',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"grulclex->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _trurdrelkrosn(self, hint):
        assert self._state.get("current") == TRURDRELKROSN, \
            f"trenblort.trurdrelkrosn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'trurdrelkrosn', 2:
                self._state["current"] = VURTRANTREN
                self._state["trig"]    = "hint:2"
            case 'trurdrelkrosn', _:
                self._state["current"] = CLORGRUL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'trurdrelkrosn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'trurdrelkrosn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"trurdrelkrosn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _clorgrul(self, hint):
        assert self._state.get("current") == CLORGRUL, \
            f"trenblort.clorgrul: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'clorgrul', 2:
                self._state["current"] = VURTRANTREN
                self._state["trig"]    = "hint:2"
            case 'clorgrul', _:
                self._state["current"] = SLIXGLART
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'clorgrul', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'clorgrul',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"clorgrul->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slixglart(self, hint):
        assert self._state.get("current") == SLIXGLART, \
            f"trenblort.slixglart: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slixglart', 2:
                self._state["current"] = VURTRANTREN
                self._state["trig"]    = "hint:2"
            case 'slixglart', _:
                self._state["current"] = PRONDRARSLONX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slixglart', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slixglart',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slixglart->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _prondrarslonx(self, hint):
        assert self._state.get("current") == PRONDRARSLONX, \
            f"trenblort.prondrarslonx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'prondrarslonx', 2:
                self._state["current"] = VURTRANTREN
                self._state["trig"]    = "hint:2"
            case 'prondrarslonx', _:
                self._state["current"] = GRAXCLARGRURL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'prondrarslonx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'prondrarslonx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"prondrarslonx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _graxclargrurl(self, hint):
        assert self._state.get("current") == GRAXCLARGRURL, \
            f"trenblort.graxclargrurl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'graxclargrurl', 2:
                self._state["current"] = VURTRANTREN
                self._state["trig"]    = "hint:2"
            case 'graxclargrurl', 1:
                self._state["current"] = SKONGRARSTUL
                self._state["trig"]    = "hint:1"
            case 'graxclargrurl', _:
                self._state["current"] = SPANGLORKREXX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'graxclargrurl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'graxclargrurl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"graxclargrurl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _spanglorkrexx(self, hint):
        assert self._state.get("current") == SPANGLORKREXX, \
            f"trenblort.spanglorkrexx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'spanglorkrexx', 2:
                self._state["current"] = VURTRANTREN
                self._state["trig"]    = "hint:2"
            case 'spanglorkrexx', _:
                self._state["current"] = SPENCLAXSTONK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'spanglorkrexx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'spanglorkrexx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"spanglorkrexx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _spenclaxstonk(self, hint):
        assert self._state.get("current") == SPENCLAXSTONK, \
            f"trenblort.spenclaxstonk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'spenclaxstonk', 2:
                self._state["current"] = VURTRANTREN
                self._state["trig"]    = "hint:2"
            case 'spenclaxstonk', _:
                self._state["current"] = BRONBRALSTOR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'spenclaxstonk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'spenclaxstonk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"spenclaxstonk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _bronbralstor(self, hint):
        assert self._state.get("current") == BRONBRALSTOR, \
            f"trenblort.bronbralstor: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'bronbralstor', 2:
                self._state["current"] = VURTRANTREN
                self._state["trig"]    = "hint:2"
            case 'bronbralstor', _:
                self._state["current"] = KRIMSTOSK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'bronbralstor', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'bronbralstor',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"bronbralstor->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _krimstosk(self, hint):
        assert self._state.get("current") == KRIMSTOSK, \
            f"trenblort.krimstosk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'krimstosk', 2:
                self._state["current"] = VURTRANTREN
                self._state["trig"]    = "hint:2"
            case 'krimstosk', 0:
                self._state["current"] = SKONGRARSTUL
                self._state["trig"]    = "hint:0"
            case 'krimstosk', _:
                self._state["current"] = VOSBLIMN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'krimstosk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'krimstosk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"krimstosk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _vosblimn(self, hint):
        assert self._state.get("current") == VOSBLIMN, \
            f"trenblort.vosblimn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'vosblimn', 2:
                self._state["current"] = VURTRANTREN
                self._state["trig"]    = "hint:2"
            case 'vosblimn', _:
                self._state["current"] = STENCLEX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'vosblimn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'vosblimn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"vosblimn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _stenclex(self, hint):
        assert self._state.get("current") == STENCLEX, \
            f"trenblort.stenclex: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'stenclex', 2:
                self._state["current"] = VURTRANTREN
                self._state["trig"]    = "hint:2"
            case 'stenclex', 1:
                self._state["current"] = FLENTROSSLAR
                self._state["trig"]    = "hint:1"
            case 'stenclex', _:
                self._state["current"] = BRIMSLORGRALN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'stenclex', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'stenclex',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"stenclex->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brimslorgraln(self, hint):
        assert self._state.get("current") == BRIMSLORGRALN, \
            f"trenblort.brimslorgraln: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brimslorgraln', 2:
                self._state["current"] = VURTRANTREN
                self._state["trig"]    = "hint:2"
            case 'brimslorgraln', 1:
                self._state["current"] = KRARSLULVAL
                self._state["trig"]    = "hint:1"
            case 'brimslorgraln', _:
                self._state["current"] = FLENTROSSLAR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brimslorgraln', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brimslorgraln',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brimslorgraln->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _flentrosslar(self, hint):
        assert self._state.get("current") == FLENTROSSLAR, \
            f"trenblort.flentrosslar: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'flentrosslar', 2:
                self._state["current"] = VURTRANTREN
                self._state["trig"]    = "hint:2"
            case 'flentrosslar', 1:
                self._state["current"] = BLAXBLIXKRAX
                self._state["trig"]    = "hint:1"
            case 'flentrosslar', _:
                self._state["current"] = KRARSLULVAL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'flentrosslar', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'flentrosslar',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"flentrosslar->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _krarslulval(self, hint):
        assert self._state.get("current") == KRARSLULVAL, \
            f"trenblort.krarslulval: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'krarslulval', 2:
                self._state["current"] = VURTRANTREN
                self._state["trig"]    = "hint:2"
            case 'krarslulval', _:
                self._state["current"] = BLAXBLIXKRAX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'krarslulval', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'krarslulval',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"krarslulval->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blaxblixkrax(self, hint):
        assert self._state.get("current") == BLAXBLIXKRAX, \
            f"trenblort.blaxblixkrax: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blaxblixkrax', 2:
                self._state["current"] = VURTRANTREN
                self._state["trig"]    = "hint:2"
            case 'blaxblixkrax', _:
                self._state["current"] = PRIXGRARK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blaxblixkrax', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blaxblixkrax',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blaxblixkrax->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _prixgrark(self, hint):
        assert self._state.get("current") == PRIXGRARK, \
            f"trenblort.prixgrark: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'prixgrark', 2:
                self._state["current"] = VURTRANTREN
                self._state["trig"]    = "hint:2"
            case 'prixgrark', 0:
                self._state["current"] = CLIXGRALK
                self._state["trig"]    = "hint:0"
            case 'prixgrark', _:
                self._state["current"] = SKONSKOS
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'prixgrark', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'prixgrark',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"prixgrark->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skonskos(self, hint):
        assert self._state.get("current") == SKONSKOS, \
            f"trenblort.skonskos: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skonskos', 2:
                self._state["current"] = VURTRANTREN
                self._state["trig"]    = "hint:2"
            case 'skonskos', 1:
                self._state["current"] = SKONGRARSTUL
                self._state["trig"]    = "hint:1"
            case 'skonskos', _:
                self._state["current"] = CLIXGRALK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skonskos', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skonskos',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skonskos->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _clixgralk(self, hint):
        assert self._state.get("current") == CLIXGRALK, \
            f"trenblort.clixgralk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'clixgralk', 2:
                self._state["current"] = VURTRANTREN
                self._state["trig"]    = "hint:2"
            case 'clixgralk', 1:
                self._state["current"] = GLONKRONSLAL
                self._state["trig"]    = "hint:1"
            case 'clixgralk', _:
                self._state["current"] = GLANBRIMX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'clixgralk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'clixgralk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"clixgralk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glanbrimx(self, hint):
        assert self._state.get("current") == GLANBRIMX, \
            f"trenblort.glanbrimx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glanbrimx', 2:
                self._state["current"] = VURTRANTREN
                self._state["trig"]    = "hint:2"
            case 'glanbrimx', _:
                self._state["current"] = GLONKRONSLAL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glanbrimx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glanbrimx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glanbrimx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glonkronslal(self, hint):
        assert self._state.get("current") == GLONKRONSLAL, \
            f"trenblort.glonkronslal: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glonkronslal', 2:
                self._state["current"] = VURTRANTREN
                self._state["trig"]    = "hint:2"
            case 'glonkronslal', 1:
                self._state["current"] = FLAXDRONBLON
                self._state["trig"]    = "hint:1"
            case 'glonkronslal', _:
                self._state["current"] = CLONBRORN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glonkronslal', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glonkronslal',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glonkronslal->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _clonbrorn(self, hint):
        assert self._state.get("current") == CLONBRORN, \
            f"trenblort.clonbrorn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'clonbrorn', 2:
                self._state["current"] = VURTRANTREN
                self._state["trig"]    = "hint:2"
            case 'clonbrorn', _:
                self._state["current"] = FLAXDRONBLON
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'clonbrorn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'clonbrorn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"clonbrorn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _flaxdronblon(self, hint):
        assert self._state.get("current") == FLAXDRONBLON, \
            f"trenblort.flaxdronblon: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'flaxdronblon', 2:
                self._state["current"] = VURTRANTREN
                self._state["trig"]    = "hint:2"
            case 'flaxdronblon', _:
                self._state["current"] = SLORFLAXX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'flaxdronblon', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'flaxdronblon',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"flaxdronblon->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slorflaxx(self, hint):
        assert self._state.get("current") == SLORFLAXX, \
            f"trenblort.slorflaxx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slorflaxx', 2:
                self._state["current"] = VURTRANTREN
                self._state["trig"]    = "hint:2"
            case 'slorflaxx', _:
                self._state["current"] = SPURSPARN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slorflaxx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slorflaxx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slorflaxx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _spursparn(self, hint):
        assert self._state.get("current") == SPURSPARN, \
            f"trenblort.spursparn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'spursparn', 2:
                self._state["current"] = VURTRANTREN
                self._state["trig"]    = "hint:2"
            case 'spursparn', _:
                self._state["current"] = GRURPRELT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'spursparn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'spursparn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"spursparn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _grurprelt(self, hint):
        assert self._state.get("current") == GRURPRELT, \
            f"trenblort.grurprelt: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'grurprelt', 2:
                self._state["current"] = VURTRANTREN
                self._state["trig"]    = "hint:2"
            case 'grurprelt', 1:
                self._state["current"] = SKONGRARSTUL
                self._state["trig"]    = "hint:1"
            case 'grurprelt', _:
                self._state["current"] = DRARBLELFLIMR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'grurprelt', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'grurprelt',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"grurprelt->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _drarblelflimr(self, hint):
        assert self._state.get("current") == DRARBLELFLIMR, \
            f"trenblort.drarblelflimr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'drarblelflimr', 2:
                self._state["current"] = VURTRANTREN
                self._state["trig"]    = "hint:2"
            case 'drarblelflimr', _:
                self._state["current"] = SPANSPULSKEL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'drarblelflimr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'drarblelflimr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"drarblelflimr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _spanspulskel(self, hint):
        assert self._state.get("current") == SPANSPULSKEL, \
            f"trenblort.spanspulskel: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'spanspulskel', 2:
                self._state["current"] = VURTRANTREN
                self._state["trig"]    = "hint:2"
            case 'spanspulskel', _:
                self._state["current"] = GLALBLIMGLAL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'spanspulskel', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'spanspulskel',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"spanspulskel->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glalblimglal(self, hint):
        assert self._state.get("current") == GLALBLIMGLAL, \
            f"trenblort.glalblimglal: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glalblimglal', 2:
                self._state["current"] = VURTRANTREN
                self._state["trig"]    = "hint:2"
            case 'glalblimglal', _:
                self._state["current"] = VAXGLULSPAXX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glalblimglal', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glalblimglal',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glalblimglal->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _vaxglulspaxx(self, hint):
        assert self._state.get("current") == VAXGLULSPAXX, \
            f"trenblort.vaxglulspaxx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'vaxglulspaxx', 2:
                self._state["current"] = VURTRANTREN
                self._state["trig"]    = "hint:2"
            case 'vaxglulspaxx', _:
                self._state["current"] = FLARFLAXPRAXN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'vaxglulspaxx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'vaxglulspaxx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"vaxglulspaxx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _flarflaxpraxn(self, hint):
        assert self._state.get("current") == FLARFLAXPRAXN, \
            f"trenblort.flarflaxpraxn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'flarflaxpraxn', 2:
                self._state["current"] = VURTRANTREN
                self._state["trig"]    = "hint:2"
            case 'flarflaxpraxn', _:
                self._state["current"] = GRAXPREXK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'flarflaxpraxn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'flarflaxpraxn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"flarflaxpraxn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _graxprexk(self, hint):
        assert self._state.get("current") == GRAXPREXK, \
            f"trenblort.graxprexk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'graxprexk', 2:
                self._state["current"] = VURTRANTREN
                self._state["trig"]    = "hint:2"
            case 'graxprexk', _:
                self._state["current"] = DRURKRARVEN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'graxprexk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'graxprexk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"graxprexk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _drurkrarven(self, hint):
        assert self._state.get("current") == DRURKRARVEN, \
            f"trenblort.drurkrarven: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'drurkrarven', 2:
                self._state["current"] = VURTRANTREN
                self._state["trig"]    = "hint:2"
            case 'drurkrarven', _:
                self._state["current"] = BRORKRELGLUL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'drurkrarven', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'drurkrarven',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"drurkrarven->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brorkrelglul(self, hint):
        assert self._state.get("current") == BRORKRELGLUL, \
            f"trenblort.brorkrelglul: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brorkrelglul', 2:
                self._state["current"] = VURTRANTREN
                self._state["trig"]    = "hint:2"
            case 'brorkrelglul', _:
                self._state["current"] = SLOSBREN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brorkrelglul', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brorkrelglul',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brorkrelglul->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slosbren(self, hint):
        assert self._state.get("current") == SLOSBREN, \
            f"trenblort.slosbren: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slosbren', 2:
                self._state["current"] = VURTRANTREN
                self._state["trig"]    = "hint:2"
            case 'slosbren', _:
                self._state["current"] = BLURDRURL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slosbren', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slosbren',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slosbren->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blurdrurl(self, hint):
        assert self._state.get("current") == BLURDRURL, \
            f"trenblort.blurdrurl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blurdrurl', 2:
                self._state["current"] = VURTRANTREN
                self._state["trig"]    = "hint:2"
            case 'blurdrurl', 1:
                self._state["current"] = SPALKRENR
                self._state["trig"]    = "hint:1"
            case 'blurdrurl', _:
                self._state["current"] = GRURFLARDRALN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blurdrurl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blurdrurl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blurdrurl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _grurflardraln(self, hint):
        assert self._state.get("current") == GRURFLARDRALN, \
            f"trenblort.grurflardraln: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'grurflardraln', 2:
                self._state["current"] = VURTRANTREN
                self._state["trig"]    = "hint:2"
            case 'grurflardraln', _:
                self._state["current"] = SPALKRENR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'grurflardraln', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'grurflardraln',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"grurflardraln->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _spalkrenr(self, hint):
        assert self._state.get("current") == SPALKRENR, \
            f"trenblort.spalkrenr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'spalkrenr', 2:
                self._state["current"] = VURTRANTREN
                self._state["trig"]    = "hint:2"
            case 'spalkrenr', _:
                self._state["current"] = SKORSPALN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'spalkrenr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'spalkrenr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"spalkrenr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skorspaln(self, hint):
        assert self._state.get("current") == SKORSPALN, \
            f"trenblort.skorspaln: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skorspaln', 2:
                self._state["current"] = VURTRANTREN
                self._state["trig"]    = "hint:2"
            case 'skorspaln', 1:
                self._state["current"] = SKONGRARSTUL
                self._state["trig"]    = "hint:1"
            case 'skorspaln', _:
                self._state["current"] = PRIMGLULGLONL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skorspaln', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skorspaln',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skorspaln->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _primglulglonl(self, hint):
        assert self._state.get("current") == PRIMGLULGLONL, \
            f"trenblort.primglulglonl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'primglulglonl', 2:
                self._state["current"] = VURTRANTREN
                self._state["trig"]    = "hint:2"
            case 'primglulglonl', 0:
                self._state["current"] = SKONGRARSTUL
                self._state["trig"]    = "hint:0"
            case 'primglulglonl', _:
                self._state["current"] = SLOSSKAXGRORK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'primglulglonl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'primglulglonl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"primglulglonl->{_to}", _xid_val)
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
            _xid_val = _xid(__name__, 'brosclark', "error", "assert_fail")
            _emit(cycle, 1, __name__, 'brosclark',
                   {"hint": hint, "span": span, "caller": caller},
                   dict(ctx), _conds,
                   "entry_blocked->error", _xid_val, assertion=_asrt)
            return 2, cycle + 1

        self._state = {"current": BROSCLARK, "ctx": ctx,
                        "span": span, "caller": caller,
                        "trig": "auto", "cycle": cycle}
        _dispatch = {
            BROSCLARK: self._brosclark,
            PRULSTULN: self._prulstuln,
            PRARFLENK: self._prarflenk,
            STAXGLENBRALX: self._staxglenbralx,
            SPENSPULT: self._spenspult,
            FLONBRIXTREXN: self._flonbrixtrexn,
            DRULBLIX: self._drulblix,
            KROSKRURGLON: self._kroskrurglon,
            GRURBLULSLIML: self._grurblulsliml,
            PRALPRUR: self._pralprur,
            BLOSTRARGLARR: self._blostrarglarr,
            SLOSKRULN: self._sloskruln,
            GLARPRORPRELK: self._glarprorprelk,
            TRULBLALVIMN: self._trulblalvimn,
            SPIMCLUL: self._spimclul,
            SPIXKRIMPRAR: self._spixkrimprar,
            VONSPURPRUL: self._vonspurprul,
            SKORBREN: self._skorbren,
            KRARSLON: self._krarslon,
            KRAXDRANBLIMX: self._kraxdranblimx,
            BLURKRARFLALN: self._blurkrarflaln,
            SKORBLARCLELT: self._skorblarclelt,
            SKEXBROSTREL: self._skexbrostrel,
            SLONFLELCLUR: self._slonflelclur,
            BRARSKONR: self._brarskonr,
            GRULCLEX: self._grulclex,
            TRURDRELKROSN: self._trurdrelkrosn,
            CLORGRUL: self._clorgrul,
            SLIXGLART: self._slixglart,
            PRONDRARSLONX: self._prondrarslonx,
            GRAXCLARGRURL: self._graxclargrurl,
            SPANGLORKREXX: self._spanglorkrexx,
            SPENCLAXSTONK: self._spenclaxstonk,
            BRONBRALSTOR: self._bronbralstor,
            KRIMSTOSK: self._krimstosk,
            VOSBLIMN: self._vosblimn,
            STENCLEX: self._stenclex,
            BRIMSLORGRALN: self._brimslorgraln,
            FLENTROSSLAR: self._flentrosslar,
            KRARSLULVAL: self._krarslulval,
            BLAXBLIXKRAX: self._blaxblixkrax,
            PRIXGRARK: self._prixgrark,
            SKONSKOS: self._skonskos,
            CLIXGRALK: self._clixgralk,
            GLANBRIMX: self._glanbrimx,
            GLONKRONSLAL: self._glonkronslal,
            CLONBRORN: self._clonbrorn,
            FLAXDRONBLON: self._flaxdronblon,
            SLORFLAXX: self._slorflaxx,
            SPURSPARN: self._spursparn,
            GRURPRELT: self._grurprelt,
            DRARBLELFLIMR: self._drarblelflimr,
            SPANSPULSKEL: self._spanspulskel,
            GLALBLIMGLAL: self._glalblimglal,
            VAXGLULSPAXX: self._vaxglulspaxx,
            FLARFLAXPRAXN: self._flarflaxpraxn,
            GRAXPREXK: self._graxprexk,
            DRURKRARVEN: self._drurkrarven,
            BRORKRELGLUL: self._brorkrelglul,
            SLOSBREN: self._slosbren,
            BLURDRURL: self._blurdrurl,
            GRURFLARDRALN: self._grurflardraln,
            SPALKRENR: self._spalkrenr,
            SKORSPALN: self._skorspaln,
            PRIMGLULGLONL: self._primglulglonl,
        }
        while self._state["current"] not in _R and self._state["cycle"] - cycle < 8000:
            _dispatch[self._state["current"]](hint)
        _ret     = _R.get(self._state["current"], -1)
        _is_err  = self._state["current"] == VURTRANTREN
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
    return TrenblortFSM().invoke(hint=hint, span=span, caller=caller, ctx=ctx, cycle=cycle)
