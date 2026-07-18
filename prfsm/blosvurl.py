from _log import _w as _emit, _xid

BRORDRIXL = 'brordrixl'
DRIMGRELGREL = 'drimgrelgrel'
KRULFLEN = 'krulflen'
KRALPRAXSPOST = 'kralpraxspost'
SLARPRENSLAX = 'slarprenslax'
GLANSKOR = 'glanskor'
GRORTRAR = 'grortrar'
SKELDRIMTRONT = 'skeldrimtront'
KRORGLULGRENR = 'krorglulgrenr'
SPURPRENKRUR = 'spurprenkrur'
TRULFLARR = 'trulflarr'
TRELSPONN = 'trelsponn'
CLELBLENT = 'clelblent'
FLARKRELVENX = 'flarkrelvenx'
BRORSKOSFLULX = 'brorskosflulx'
CLORDRON = 'clordron'
CLANCLULGRAN = 'clanclulgran'
BROSSPOSX = 'brossposx'
KRELBLELVIM = 'krelblelvim'
KRURKRARCLOR = 'krurkrarclor'
BRULCLENBRUR = 'brulclenbrur'
STELKRAN = 'stelkran'
SPURKREXR = 'spurkrexr'
PRARFLONSKAX = 'prarflonskax'
CLIXTRORSTELX = 'clixtrorstelx'
TRIMVIXK = 'trimvixk'
SKONBRARK = 'skonbrark'
SKULKRANGLEN = 'skulkranglen'
STELDRELL = 'steldrell'
BLAXKREXX = 'blaxkrexx'
GLAXBLEXT = 'glaxblext'
STELSPIMR = 'stelspimr'
VENDRAXL = 'vendraxl'
TREXBLENGLUL = 'trexblenglul'
CLALDRENK = 'claldrenk'
FLURGLORR = 'flurglorr'
SPOSSKANSTORR = 'sposskanstorr'
SLALDRONX = 'slaldronx'
GLONKREXK = 'glonkrexk'
BRURKRENSTEN = 'brurkrensten'
VONGLALTRIXN = 'vonglaltrixn'
KRIMPRART = 'krimprart'
GLOSSTEX = 'glosstex'
BRELBRENL = 'brelbrenl'
DRAXSPENT = 'draxspent'
CLURBRAX = 'clurbrax'
GLARPRORDRIML = 'glarprordriml'
TRULSKIMSLALL = 'trulskimslall'
GRELPRULFLARK = 'grelprulflark'
SPALVON = 'spalvon'
KROSDRAXN = 'krosdraxn'
SKELBLULSKAR = 'skelblulskar'
BRARPREXSLOST = 'brarprexslost'
CLELSLUL = 'clelslul'
TRENDRENN = 'trendrenn'
BLONCLARDRAXN = 'blonclardraxn'
BRORPRIXT = 'brorprixt'
VURGRURTRARX = 'vurgrurtrarx'
GLALTRAXX = 'glaltraxx'
KRELSTULK = 'krelstulk'
SKULFLIXPRAXT = 'skulflixpraxt'
SLULGRURX = 'slulgrurx'
TRARBREXCLURK = 'trarbrexclurk'
GRONSPULSKAN = 'gronspulskan'
DRONPRIM = 'dronprim'
PROSCLONSKON = 'prosclonskon'
KRARSLORL = 'krarslorl'
GLALTRAXT = 'glaltraxt'

_R = {
    PROSCLONSKON: 0,
    KRARSLORL: 1,
    GLALTRAXT: 2,
}

_CTX_READS_KEY = 'flurslex'
_CTX_THRESHOLD = 16

class BlosvurlFSM:
    def __init__(self):
        self._state = {}

    def _brordrixl(self, hint):
        assert self._state.get("current") == BRORDRIXL, \
            f"blosvurl.brordrixl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brordrixl', 2:
                self._state["current"] = GLALTRAXT
                self._state["trig"]    = "hint:2"
            case 'brordrixl', _:
                self._state["current"] = DRIMGRELGREL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brordrixl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brordrixl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brordrixl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _drimgrelgrel(self, hint):
        assert self._state.get("current") == DRIMGRELGREL, \
            f"blosvurl.drimgrelgrel: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'drimgrelgrel', 2:
                self._state["current"] = GLALTRAXT
                self._state["trig"]    = "hint:2"
            case 'drimgrelgrel', _:
                self._state["current"] = KRULFLEN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'drimgrelgrel', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'drimgrelgrel',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"drimgrelgrel->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _krulflen(self, hint):
        assert self._state.get("current") == KRULFLEN, \
            f"blosvurl.krulflen: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'krulflen', 2:
                self._state["current"] = GLALTRAXT
                self._state["trig"]    = "hint:2"
            case 'krulflen', _:
                self._state["current"] = KRALPRAXSPOST
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'krulflen', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'krulflen',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"krulflen->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _kralpraxspost(self, hint):
        assert self._state.get("current") == KRALPRAXSPOST, \
            f"blosvurl.kralpraxspost: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'kralpraxspost', 2:
                self._state["current"] = GLALTRAXT
                self._state["trig"]    = "hint:2"
            case 'kralpraxspost', _:
                self._state["current"] = SLARPRENSLAX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'kralpraxspost', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'kralpraxspost',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"kralpraxspost->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slarprenslax(self, hint):
        assert self._state.get("current") == SLARPRENSLAX, \
            f"blosvurl.slarprenslax: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slarprenslax', 2:
                self._state["current"] = GLALTRAXT
                self._state["trig"]    = "hint:2"
            case 'slarprenslax', _:
                self._state["current"] = GLANSKOR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slarprenslax', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slarprenslax',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slarprenslax->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glanskor(self, hint):
        assert self._state.get("current") == GLANSKOR, \
            f"blosvurl.glanskor: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glanskor', 2:
                self._state["current"] = GLALTRAXT
                self._state["trig"]    = "hint:2"
            case 'glanskor', _:
                self._state["current"] = GRORTRAR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glanskor', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glanskor',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glanskor->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _grortrar(self, hint):
        assert self._state.get("current") == GRORTRAR, \
            f"blosvurl.grortrar: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'grortrar', 2:
                self._state["current"] = GLALTRAXT
                self._state["trig"]    = "hint:2"
            case 'grortrar', 0:
                self._state["current"] = KRARSLORL
                self._state["trig"]    = "hint:0"
            case 'grortrar', _:
                self._state["current"] = SKELDRIMTRONT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'grortrar', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'grortrar',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"grortrar->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skeldrimtront(self, hint):
        assert self._state.get("current") == SKELDRIMTRONT, \
            f"blosvurl.skeldrimtront: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skeldrimtront', 2:
                self._state["current"] = GLALTRAXT
                self._state["trig"]    = "hint:2"
            case 'skeldrimtront', _:
                self._state["current"] = KRORGLULGRENR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skeldrimtront', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skeldrimtront',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skeldrimtront->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _krorglulgrenr(self, hint):
        assert self._state.get("current") == KRORGLULGRENR, \
            f"blosvurl.krorglulgrenr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'krorglulgrenr', 2:
                self._state["current"] = GLALTRAXT
                self._state["trig"]    = "hint:2"
            case 'krorglulgrenr', _:
                self._state["current"] = SPURPRENKRUR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'krorglulgrenr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'krorglulgrenr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"krorglulgrenr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _spurprenkrur(self, hint):
        assert self._state.get("current") == SPURPRENKRUR, \
            f"blosvurl.spurprenkrur: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'spurprenkrur', 2:
                self._state["current"] = GLALTRAXT
                self._state["trig"]    = "hint:2"
            case 'spurprenkrur', _:
                self._state["current"] = TRULFLARR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'spurprenkrur', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'spurprenkrur',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"spurprenkrur->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _trulflarr(self, hint):
        assert self._state.get("current") == TRULFLARR, \
            f"blosvurl.trulflarr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'trulflarr', 2:
                self._state["current"] = GLALTRAXT
                self._state["trig"]    = "hint:2"
            case 'trulflarr', 0:
                self._state["current"] = CLELBLENT
                self._state["trig"]    = "hint:0"
            case 'trulflarr', _:
                self._state["current"] = TRELSPONN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'trulflarr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'trulflarr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"trulflarr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _trelsponn(self, hint):
        assert self._state.get("current") == TRELSPONN, \
            f"blosvurl.trelsponn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'trelsponn', 2:
                self._state["current"] = GLALTRAXT
                self._state["trig"]    = "hint:2"
            case 'trelsponn', _:
                self._state["current"] = CLELBLENT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'trelsponn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'trelsponn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"trelsponn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _clelblent(self, hint):
        assert self._state.get("current") == CLELBLENT, \
            f"blosvurl.clelblent: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'clelblent', 2:
                self._state["current"] = GLALTRAXT
                self._state["trig"]    = "hint:2"
            case 'clelblent', _:
                self._state["current"] = FLARKRELVENX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'clelblent', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'clelblent',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"clelblent->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _flarkrelvenx(self, hint):
        assert self._state.get("current") == FLARKRELVENX, \
            f"blosvurl.flarkrelvenx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'flarkrelvenx', 2:
                self._state["current"] = GLALTRAXT
                self._state["trig"]    = "hint:2"
            case 'flarkrelvenx', 1:
                self._state["current"] = CLORDRON
                self._state["trig"]    = "hint:1"
            case 'flarkrelvenx', _:
                self._state["current"] = BRORSKOSFLULX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'flarkrelvenx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'flarkrelvenx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"flarkrelvenx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brorskosflulx(self, hint):
        assert self._state.get("current") == BRORSKOSFLULX, \
            f"blosvurl.brorskosflulx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brorskosflulx', 2:
                self._state["current"] = GLALTRAXT
                self._state["trig"]    = "hint:2"
            case 'brorskosflulx', 1:
                self._state["current"] = CLANCLULGRAN
                self._state["trig"]    = "hint:1"
            case 'brorskosflulx', _:
                self._state["current"] = CLORDRON
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brorskosflulx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brorskosflulx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brorskosflulx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _clordron(self, hint):
        assert self._state.get("current") == CLORDRON, \
            f"blosvurl.clordron: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'clordron', 2:
                self._state["current"] = GLALTRAXT
                self._state["trig"]    = "hint:2"
            case 'clordron', _:
                self._state["current"] = CLANCLULGRAN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'clordron', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'clordron',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"clordron->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _clanclulgran(self, hint):
        assert self._state.get("current") == CLANCLULGRAN, \
            f"blosvurl.clanclulgran: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'clanclulgran', 2:
                self._state["current"] = GLALTRAXT
                self._state["trig"]    = "hint:2"
            case 'clanclulgran', _:
                self._state["current"] = BROSSPOSX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'clanclulgran', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'clanclulgran',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"clanclulgran->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brossposx(self, hint):
        assert self._state.get("current") == BROSSPOSX, \
            f"blosvurl.brossposx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brossposx', 2:
                self._state["current"] = GLALTRAXT
                self._state["trig"]    = "hint:2"
            case 'brossposx', 1:
                self._state["current"] = KRARSLORL
                self._state["trig"]    = "hint:1"
            case 'brossposx', _:
                self._state["current"] = KRELBLELVIM
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brossposx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brossposx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brossposx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _krelblelvim(self, hint):
        assert self._state.get("current") == KRELBLELVIM, \
            f"blosvurl.krelblelvim: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'krelblelvim', 2:
                self._state["current"] = GLALTRAXT
                self._state["trig"]    = "hint:2"
            case 'krelblelvim', 1:
                self._state["current"] = KRARSLORL
                self._state["trig"]    = "hint:1"
            case 'krelblelvim', _:
                self._state["current"] = KRURKRARCLOR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'krelblelvim', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'krelblelvim',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"krelblelvim->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _krurkrarclor(self, hint):
        assert self._state.get("current") == KRURKRARCLOR, \
            f"blosvurl.krurkrarclor: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'krurkrarclor', 2:
                self._state["current"] = GLALTRAXT
                self._state["trig"]    = "hint:2"
            case 'krurkrarclor', 0:
                self._state["current"] = KRARSLORL
                self._state["trig"]    = "hint:0"
            case 'krurkrarclor', _:
                self._state["current"] = BRULCLENBRUR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'krurkrarclor', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'krurkrarclor',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"krurkrarclor->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brulclenbrur(self, hint):
        assert self._state.get("current") == BRULCLENBRUR, \
            f"blosvurl.brulclenbrur: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brulclenbrur', 2:
                self._state["current"] = GLALTRAXT
                self._state["trig"]    = "hint:2"
            case 'brulclenbrur', 0:
                self._state["current"] = SPURKREXR
                self._state["trig"]    = "hint:0"
            case 'brulclenbrur', _:
                self._state["current"] = STELKRAN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brulclenbrur', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brulclenbrur',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brulclenbrur->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _stelkran(self, hint):
        assert self._state.get("current") == STELKRAN, \
            f"blosvurl.stelkran: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'stelkran', 2:
                self._state["current"] = GLALTRAXT
                self._state["trig"]    = "hint:2"
            case 'stelkran', _:
                self._state["current"] = SPURKREXR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'stelkran', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'stelkran',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"stelkran->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _spurkrexr(self, hint):
        assert self._state.get("current") == SPURKREXR, \
            f"blosvurl.spurkrexr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'spurkrexr', 2:
                self._state["current"] = GLALTRAXT
                self._state["trig"]    = "hint:2"
            case 'spurkrexr', 1:
                self._state["current"] = KRARSLORL
                self._state["trig"]    = "hint:1"
            case 'spurkrexr', _:
                self._state["current"] = PRARFLONSKAX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'spurkrexr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'spurkrexr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"spurkrexr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _prarflonskax(self, hint):
        assert self._state.get("current") == PRARFLONSKAX, \
            f"blosvurl.prarflonskax: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'prarflonskax', 2:
                self._state["current"] = GLALTRAXT
                self._state["trig"]    = "hint:2"
            case 'prarflonskax', _:
                self._state["current"] = CLIXTRORSTELX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'prarflonskax', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'prarflonskax',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"prarflonskax->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _clixtrorstelx(self, hint):
        assert self._state.get("current") == CLIXTRORSTELX, \
            f"blosvurl.clixtrorstelx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'clixtrorstelx', 2:
                self._state["current"] = GLALTRAXT
                self._state["trig"]    = "hint:2"
            case 'clixtrorstelx', _:
                self._state["current"] = TRIMVIXK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'clixtrorstelx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'clixtrorstelx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"clixtrorstelx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _trimvixk(self, hint):
        assert self._state.get("current") == TRIMVIXK, \
            f"blosvurl.trimvixk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'trimvixk', 2:
                self._state["current"] = GLALTRAXT
                self._state["trig"]    = "hint:2"
            case 'trimvixk', _:
                self._state["current"] = SKONBRARK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'trimvixk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'trimvixk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"trimvixk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skonbrark(self, hint):
        assert self._state.get("current") == SKONBRARK, \
            f"blosvurl.skonbrark: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skonbrark', 2:
                self._state["current"] = GLALTRAXT
                self._state["trig"]    = "hint:2"
            case 'skonbrark', 0:
                self._state["current"] = STELDRELL
                self._state["trig"]    = "hint:0"
            case 'skonbrark', _:
                self._state["current"] = SKULKRANGLEN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skonbrark', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skonbrark',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skonbrark->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skulkranglen(self, hint):
        assert self._state.get("current") == SKULKRANGLEN, \
            f"blosvurl.skulkranglen: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skulkranglen', 2:
                self._state["current"] = GLALTRAXT
                self._state["trig"]    = "hint:2"
            case 'skulkranglen', 0:
                self._state["current"] = KRARSLORL
                self._state["trig"]    = "hint:0"
            case 'skulkranglen', _:
                self._state["current"] = STELDRELL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skulkranglen', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skulkranglen',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skulkranglen->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _steldrell(self, hint):
        assert self._state.get("current") == STELDRELL, \
            f"blosvurl.steldrell: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'steldrell', 2:
                self._state["current"] = GLALTRAXT
                self._state["trig"]    = "hint:2"
            case 'steldrell', 0:
                self._state["current"] = KRARSLORL
                self._state["trig"]    = "hint:0"
            case 'steldrell', _:
                self._state["current"] = BLAXKREXX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'steldrell', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'steldrell',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"steldrell->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blaxkrexx(self, hint):
        assert self._state.get("current") == BLAXKREXX, \
            f"blosvurl.blaxkrexx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blaxkrexx', 2:
                self._state["current"] = GLALTRAXT
                self._state["trig"]    = "hint:2"
            case 'blaxkrexx', _:
                self._state["current"] = GLAXBLEXT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blaxkrexx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blaxkrexx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blaxkrexx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glaxblext(self, hint):
        assert self._state.get("current") == GLAXBLEXT, \
            f"blosvurl.glaxblext: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glaxblext', 2:
                self._state["current"] = GLALTRAXT
                self._state["trig"]    = "hint:2"
            case 'glaxblext', _:
                self._state["current"] = STELSPIMR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glaxblext', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glaxblext',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glaxblext->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _stelspimr(self, hint):
        assert self._state.get("current") == STELSPIMR, \
            f"blosvurl.stelspimr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'stelspimr', 2:
                self._state["current"] = GLALTRAXT
                self._state["trig"]    = "hint:2"
            case 'stelspimr', _:
                self._state["current"] = VENDRAXL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'stelspimr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'stelspimr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"stelspimr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _vendraxl(self, hint):
        assert self._state.get("current") == VENDRAXL, \
            f"blosvurl.vendraxl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'vendraxl', 2:
                self._state["current"] = GLALTRAXT
                self._state["trig"]    = "hint:2"
            case 'vendraxl', _:
                self._state["current"] = TREXBLENGLUL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'vendraxl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'vendraxl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"vendraxl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _trexblenglul(self, hint):
        assert self._state.get("current") == TREXBLENGLUL, \
            f"blosvurl.trexblenglul: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'trexblenglul', 2:
                self._state["current"] = GLALTRAXT
                self._state["trig"]    = "hint:2"
            case 'trexblenglul', 1:
                self._state["current"] = KRARSLORL
                self._state["trig"]    = "hint:1"
            case 'trexblenglul', _:
                self._state["current"] = CLALDRENK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'trexblenglul', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'trexblenglul',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"trexblenglul->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _claldrenk(self, hint):
        assert self._state.get("current") == CLALDRENK, \
            f"blosvurl.claldrenk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'claldrenk', 2:
                self._state["current"] = GLALTRAXT
                self._state["trig"]    = "hint:2"
            case 'claldrenk', 1:
                self._state["current"] = SPOSSKANSTORR
                self._state["trig"]    = "hint:1"
            case 'claldrenk', _:
                self._state["current"] = FLURGLORR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'claldrenk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'claldrenk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"claldrenk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _flurglorr(self, hint):
        assert self._state.get("current") == FLURGLORR, \
            f"blosvurl.flurglorr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'flurglorr', 2:
                self._state["current"] = GLALTRAXT
                self._state["trig"]    = "hint:2"
            case 'flurglorr', 1:
                self._state["current"] = KRARSLORL
                self._state["trig"]    = "hint:1"
            case 'flurglorr', _:
                self._state["current"] = SPOSSKANSTORR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'flurglorr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'flurglorr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"flurglorr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _sposskanstorr(self, hint):
        assert self._state.get("current") == SPOSSKANSTORR, \
            f"blosvurl.sposskanstorr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'sposskanstorr', 2:
                self._state["current"] = GLALTRAXT
                self._state["trig"]    = "hint:2"
            case 'sposskanstorr', _:
                self._state["current"] = SLALDRONX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'sposskanstorr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'sposskanstorr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"sposskanstorr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slaldronx(self, hint):
        assert self._state.get("current") == SLALDRONX, \
            f"blosvurl.slaldronx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slaldronx', 2:
                self._state["current"] = GLALTRAXT
                self._state["trig"]    = "hint:2"
            case 'slaldronx', _:
                self._state["current"] = GLONKREXK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slaldronx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slaldronx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slaldronx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glonkrexk(self, hint):
        assert self._state.get("current") == GLONKREXK, \
            f"blosvurl.glonkrexk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glonkrexk', 2:
                self._state["current"] = GLALTRAXT
                self._state["trig"]    = "hint:2"
            case 'glonkrexk', _:
                self._state["current"] = BRURKRENSTEN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glonkrexk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glonkrexk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glonkrexk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brurkrensten(self, hint):
        assert self._state.get("current") == BRURKRENSTEN, \
            f"blosvurl.brurkrensten: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brurkrensten', 2:
                self._state["current"] = GLALTRAXT
                self._state["trig"]    = "hint:2"
            case 'brurkrensten', 1:
                self._state["current"] = KRIMPRART
                self._state["trig"]    = "hint:1"
            case 'brurkrensten', _:
                self._state["current"] = VONGLALTRIXN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brurkrensten', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brurkrensten',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brurkrensten->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _vonglaltrixn(self, hint):
        assert self._state.get("current") == VONGLALTRIXN, \
            f"blosvurl.vonglaltrixn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'vonglaltrixn', 2:
                self._state["current"] = GLALTRAXT
                self._state["trig"]    = "hint:2"
            case 'vonglaltrixn', _:
                self._state["current"] = KRIMPRART
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'vonglaltrixn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'vonglaltrixn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"vonglaltrixn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _krimprart(self, hint):
        assert self._state.get("current") == KRIMPRART, \
            f"blosvurl.krimprart: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'krimprart', 2:
                self._state["current"] = GLALTRAXT
                self._state["trig"]    = "hint:2"
            case 'krimprart', 1:
                self._state["current"] = KRARSLORL
                self._state["trig"]    = "hint:1"
            case 'krimprart', _:
                self._state["current"] = GLOSSTEX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'krimprart', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'krimprart',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"krimprart->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glosstex(self, hint):
        assert self._state.get("current") == GLOSSTEX, \
            f"blosvurl.glosstex: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glosstex', 2:
                self._state["current"] = GLALTRAXT
                self._state["trig"]    = "hint:2"
            case 'glosstex', _:
                self._state["current"] = BRELBRENL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glosstex', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glosstex',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glosstex->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brelbrenl(self, hint):
        assert self._state.get("current") == BRELBRENL, \
            f"blosvurl.brelbrenl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brelbrenl', 2:
                self._state["current"] = GLALTRAXT
                self._state["trig"]    = "hint:2"
            case 'brelbrenl', _:
                self._state["current"] = DRAXSPENT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brelbrenl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brelbrenl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brelbrenl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _draxspent(self, hint):
        assert self._state.get("current") == DRAXSPENT, \
            f"blosvurl.draxspent: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'draxspent', 2:
                self._state["current"] = GLALTRAXT
                self._state["trig"]    = "hint:2"
            case 'draxspent', 0:
                self._state["current"] = GLARPRORDRIML
                self._state["trig"]    = "hint:0"
            case 'draxspent', _:
                self._state["current"] = CLURBRAX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'draxspent', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'draxspent',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"draxspent->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _clurbrax(self, hint):
        assert self._state.get("current") == CLURBRAX, \
            f"blosvurl.clurbrax: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'clurbrax', 2:
                self._state["current"] = GLALTRAXT
                self._state["trig"]    = "hint:2"
            case 'clurbrax', _:
                self._state["current"] = GLARPRORDRIML
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'clurbrax', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'clurbrax',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"clurbrax->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glarprordriml(self, hint):
        assert self._state.get("current") == GLARPRORDRIML, \
            f"blosvurl.glarprordriml: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glarprordriml', 2:
                self._state["current"] = GLALTRAXT
                self._state["trig"]    = "hint:2"
            case 'glarprordriml', 0:
                self._state["current"] = GRELPRULFLARK
                self._state["trig"]    = "hint:0"
            case 'glarprordriml', _:
                self._state["current"] = TRULSKIMSLALL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glarprordriml', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glarprordriml',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glarprordriml->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _trulskimslall(self, hint):
        assert self._state.get("current") == TRULSKIMSLALL, \
            f"blosvurl.trulskimslall: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'trulskimslall', 2:
                self._state["current"] = GLALTRAXT
                self._state["trig"]    = "hint:2"
            case 'trulskimslall', 1:
                self._state["current"] = KRARSLORL
                self._state["trig"]    = "hint:1"
            case 'trulskimslall', _:
                self._state["current"] = GRELPRULFLARK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'trulskimslall', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'trulskimslall',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"trulskimslall->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _grelprulflark(self, hint):
        assert self._state.get("current") == GRELPRULFLARK, \
            f"blosvurl.grelprulflark: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'grelprulflark', 2:
                self._state["current"] = GLALTRAXT
                self._state["trig"]    = "hint:2"
            case 'grelprulflark', 1:
                self._state["current"] = KROSDRAXN
                self._state["trig"]    = "hint:1"
            case 'grelprulflark', _:
                self._state["current"] = SPALVON
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'grelprulflark', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'grelprulflark',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"grelprulflark->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _spalvon(self, hint):
        assert self._state.get("current") == SPALVON, \
            f"blosvurl.spalvon: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'spalvon', 2:
                self._state["current"] = GLALTRAXT
                self._state["trig"]    = "hint:2"
            case 'spalvon', _:
                self._state["current"] = KROSDRAXN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'spalvon', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'spalvon',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"spalvon->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _krosdraxn(self, hint):
        assert self._state.get("current") == KROSDRAXN, \
            f"blosvurl.krosdraxn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'krosdraxn', 2:
                self._state["current"] = GLALTRAXT
                self._state["trig"]    = "hint:2"
            case 'krosdraxn', 1:
                self._state["current"] = BRARPREXSLOST
                self._state["trig"]    = "hint:1"
            case 'krosdraxn', _:
                self._state["current"] = SKELBLULSKAR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'krosdraxn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'krosdraxn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"krosdraxn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skelblulskar(self, hint):
        assert self._state.get("current") == SKELBLULSKAR, \
            f"blosvurl.skelblulskar: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skelblulskar', 2:
                self._state["current"] = GLALTRAXT
                self._state["trig"]    = "hint:2"
            case 'skelblulskar', _:
                self._state["current"] = BRARPREXSLOST
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skelblulskar', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skelblulskar',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skelblulskar->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brarprexslost(self, hint):
        assert self._state.get("current") == BRARPREXSLOST, \
            f"blosvurl.brarprexslost: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brarprexslost', 2:
                self._state["current"] = GLALTRAXT
                self._state["trig"]    = "hint:2"
            case 'brarprexslost', _:
                self._state["current"] = CLELSLUL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brarprexslost', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brarprexslost',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brarprexslost->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _clelslul(self, hint):
        assert self._state.get("current") == CLELSLUL, \
            f"blosvurl.clelslul: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'clelslul', 2:
                self._state["current"] = GLALTRAXT
                self._state["trig"]    = "hint:2"
            case 'clelslul', 1:
                self._state["current"] = BLONCLARDRAXN
                self._state["trig"]    = "hint:1"
            case 'clelslul', _:
                self._state["current"] = TRENDRENN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'clelslul', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'clelslul',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"clelslul->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _trendrenn(self, hint):
        assert self._state.get("current") == TRENDRENN, \
            f"blosvurl.trendrenn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'trendrenn', 2:
                self._state["current"] = GLALTRAXT
                self._state["trig"]    = "hint:2"
            case 'trendrenn', 1:
                self._state["current"] = BRORPRIXT
                self._state["trig"]    = "hint:1"
            case 'trendrenn', _:
                self._state["current"] = BLONCLARDRAXN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'trendrenn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'trendrenn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"trendrenn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blonclardraxn(self, hint):
        assert self._state.get("current") == BLONCLARDRAXN, \
            f"blosvurl.blonclardraxn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blonclardraxn', 2:
                self._state["current"] = GLALTRAXT
                self._state["trig"]    = "hint:2"
            case 'blonclardraxn', 0:
                self._state["current"] = VURGRURTRARX
                self._state["trig"]    = "hint:0"
            case 'blonclardraxn', _:
                self._state["current"] = BRORPRIXT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blonclardraxn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blonclardraxn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blonclardraxn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brorprixt(self, hint):
        assert self._state.get("current") == BRORPRIXT, \
            f"blosvurl.brorprixt: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brorprixt', 2:
                self._state["current"] = GLALTRAXT
                self._state["trig"]    = "hint:2"
            case 'brorprixt', _:
                self._state["current"] = VURGRURTRARX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brorprixt', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brorprixt',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brorprixt->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _vurgrurtrarx(self, hint):
        assert self._state.get("current") == VURGRURTRARX, \
            f"blosvurl.vurgrurtrarx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'vurgrurtrarx', 2:
                self._state["current"] = GLALTRAXT
                self._state["trig"]    = "hint:2"
            case 'vurgrurtrarx', _:
                self._state["current"] = GLALTRAXX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'vurgrurtrarx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'vurgrurtrarx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"vurgrurtrarx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glaltraxx(self, hint):
        assert self._state.get("current") == GLALTRAXX, \
            f"blosvurl.glaltraxx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glaltraxx', 2:
                self._state["current"] = GLALTRAXT
                self._state["trig"]    = "hint:2"
            case 'glaltraxx', _:
                self._state["current"] = KRELSTULK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glaltraxx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glaltraxx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glaltraxx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _krelstulk(self, hint):
        assert self._state.get("current") == KRELSTULK, \
            f"blosvurl.krelstulk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'krelstulk', 2:
                self._state["current"] = GLALTRAXT
                self._state["trig"]    = "hint:2"
            case 'krelstulk', _:
                self._state["current"] = SKULFLIXPRAXT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'krelstulk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'krelstulk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"krelstulk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skulflixpraxt(self, hint):
        assert self._state.get("current") == SKULFLIXPRAXT, \
            f"blosvurl.skulflixpraxt: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skulflixpraxt', 2:
                self._state["current"] = GLALTRAXT
                self._state["trig"]    = "hint:2"
            case 'skulflixpraxt', _:
                self._state["current"] = SLULGRURX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skulflixpraxt', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skulflixpraxt',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skulflixpraxt->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slulgrurx(self, hint):
        assert self._state.get("current") == SLULGRURX, \
            f"blosvurl.slulgrurx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slulgrurx', 2:
                self._state["current"] = GLALTRAXT
                self._state["trig"]    = "hint:2"
            case 'slulgrurx', 0:
                self._state["current"] = KRARSLORL
                self._state["trig"]    = "hint:0"
            case 'slulgrurx', _:
                self._state["current"] = TRARBREXCLURK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slulgrurx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slulgrurx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slulgrurx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _trarbrexclurk(self, hint):
        assert self._state.get("current") == TRARBREXCLURK, \
            f"blosvurl.trarbrexclurk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'trarbrexclurk', 2:
                self._state["current"] = GLALTRAXT
                self._state["trig"]    = "hint:2"
            case 'trarbrexclurk', 0:
                self._state["current"] = DRONPRIM
                self._state["trig"]    = "hint:0"
            case 'trarbrexclurk', _:
                self._state["current"] = GRONSPULSKAN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'trarbrexclurk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'trarbrexclurk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"trarbrexclurk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _gronspulskan(self, hint):
        assert self._state.get("current") == GRONSPULSKAN, \
            f"blosvurl.gronspulskan: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'gronspulskan', 2:
                self._state["current"] = GLALTRAXT
                self._state["trig"]    = "hint:2"
            case 'gronspulskan', 0:
                self._state["current"] = KRARSLORL
                self._state["trig"]    = "hint:0"
            case 'gronspulskan', _:
                self._state["current"] = DRONPRIM
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'gronspulskan', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'gronspulskan',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"gronspulskan->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _dronprim(self, hint):
        assert self._state.get("current") == DRONPRIM, \
            f"blosvurl.dronprim: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'dronprim', 2:
                self._state["current"] = GLALTRAXT
                self._state["trig"]    = "hint:2"
            case 'dronprim', 0:
                self._state["current"] = KRARSLORL
                self._state["trig"]    = "hint:0"
            case 'dronprim', _:
                self._state["current"] = PROSCLONSKON
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'dronprim', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'dronprim',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"dronprim->{_to}", _xid_val)
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
            _xid_val = _xid(__name__, 'brordrixl', "error", "assert_fail")
            _emit(cycle, 1, __name__, 'brordrixl',
                   {"hint": hint, "span": span, "caller": caller},
                   dict(ctx), _conds,
                   "entry_blocked->error", _xid_val, assertion=_asrt)
            return 2, cycle + 1

        self._state = {"current": BRORDRIXL, "ctx": ctx,
                        "span": span, "caller": caller,
                        "trig": "auto", "cycle": cycle}
        _dispatch = {
            BRORDRIXL: self._brordrixl,
            DRIMGRELGREL: self._drimgrelgrel,
            KRULFLEN: self._krulflen,
            KRALPRAXSPOST: self._kralpraxspost,
            SLARPRENSLAX: self._slarprenslax,
            GLANSKOR: self._glanskor,
            GRORTRAR: self._grortrar,
            SKELDRIMTRONT: self._skeldrimtront,
            KRORGLULGRENR: self._krorglulgrenr,
            SPURPRENKRUR: self._spurprenkrur,
            TRULFLARR: self._trulflarr,
            TRELSPONN: self._trelsponn,
            CLELBLENT: self._clelblent,
            FLARKRELVENX: self._flarkrelvenx,
            BRORSKOSFLULX: self._brorskosflulx,
            CLORDRON: self._clordron,
            CLANCLULGRAN: self._clanclulgran,
            BROSSPOSX: self._brossposx,
            KRELBLELVIM: self._krelblelvim,
            KRURKRARCLOR: self._krurkrarclor,
            BRULCLENBRUR: self._brulclenbrur,
            STELKRAN: self._stelkran,
            SPURKREXR: self._spurkrexr,
            PRARFLONSKAX: self._prarflonskax,
            CLIXTRORSTELX: self._clixtrorstelx,
            TRIMVIXK: self._trimvixk,
            SKONBRARK: self._skonbrark,
            SKULKRANGLEN: self._skulkranglen,
            STELDRELL: self._steldrell,
            BLAXKREXX: self._blaxkrexx,
            GLAXBLEXT: self._glaxblext,
            STELSPIMR: self._stelspimr,
            VENDRAXL: self._vendraxl,
            TREXBLENGLUL: self._trexblenglul,
            CLALDRENK: self._claldrenk,
            FLURGLORR: self._flurglorr,
            SPOSSKANSTORR: self._sposskanstorr,
            SLALDRONX: self._slaldronx,
            GLONKREXK: self._glonkrexk,
            BRURKRENSTEN: self._brurkrensten,
            VONGLALTRIXN: self._vonglaltrixn,
            KRIMPRART: self._krimprart,
            GLOSSTEX: self._glosstex,
            BRELBRENL: self._brelbrenl,
            DRAXSPENT: self._draxspent,
            CLURBRAX: self._clurbrax,
            GLARPRORDRIML: self._glarprordriml,
            TRULSKIMSLALL: self._trulskimslall,
            GRELPRULFLARK: self._grelprulflark,
            SPALVON: self._spalvon,
            KROSDRAXN: self._krosdraxn,
            SKELBLULSKAR: self._skelblulskar,
            BRARPREXSLOST: self._brarprexslost,
            CLELSLUL: self._clelslul,
            TRENDRENN: self._trendrenn,
            BLONCLARDRAXN: self._blonclardraxn,
            BRORPRIXT: self._brorprixt,
            VURGRURTRARX: self._vurgrurtrarx,
            GLALTRAXX: self._glaltraxx,
            KRELSTULK: self._krelstulk,
            SKULFLIXPRAXT: self._skulflixpraxt,
            SLULGRURX: self._slulgrurx,
            TRARBREXCLURK: self._trarbrexclurk,
            GRONSPULSKAN: self._gronspulskan,
            DRONPRIM: self._dronprim,
        }
        while self._state["current"] not in _R and self._state["cycle"] - cycle < 8000:
            _dispatch[self._state["current"]](hint)
        _ret     = _R.get(self._state["current"], -1)
        _is_err  = self._state["current"] == GLALTRAXT
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
    return BlosvurlFSM().invoke(hint=hint, span=span, caller=caller, ctx=ctx, cycle=cycle)
