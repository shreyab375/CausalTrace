from _log import _w as _emit, _xid

VIXBLALGRIM = 'vixblalgrim'
DRALGRAR = 'dralgrar'
SPOSVEXN = 'sposvexn'
GLAXSTIMT = 'glaxstimt'
STIMGLORTRUR = 'stimglortrur'
GLIMSPURTROS = 'glimspurtros'
SKEXPRIMGLIM = 'skexprimglim'
DREXSTORFLURR = 'drexstorflurr'
KRENSPELN = 'krenspeln'
SPIMGLOSBLOR = 'spimglosblor'
KROSGLUR = 'krosglur'
GLORGLULTRIM = 'glorglultrim'
TRIMCLAN = 'trimclan'
KRULPRELBRURT = 'krulprelbrurt'
KRONBLAXFLONN = 'kronblaxflonn'
GRALPRIM = 'gralprim'
SLEXKRAL = 'slexkral'
SKOSSTOSL = 'skosstosl'
SLALDRORSLON = 'slaldrorslon'
GRANFLURSKURN = 'granflurskurn'
FLALKRULPRAXN = 'flalkrulpraxn'
SPULGRULPREL = 'spulgrulprel'
VEXBRURK = 'vexbrurk'
GLIXGLEXL = 'glixglexl'
STOSBLURN = 'stosblurn'
BLIMGLURN = 'blimglurn'
PRANSKANSKORX = 'pranskanskorx'
VALSKEXR = 'valskexr'
DRANDROSGLULT = 'drandrosglult'
PRIXSKIMT = 'prixskimt'
DRULFLAN = 'drulflan'
DRAXPRIMDROS = 'draxprimdros'
BRULGLOR = 'brulglor'
SKIMBRALX = 'skimbralx'
CLENBLALT = 'clenblalt'
BRARSPAXTRORR = 'brarspaxtrorr'
CLULGLOSX = 'clulglosx'
GRANFLURR = 'granflurr'
SLULSLANKRIM = 'slulslankrim'
GLURSTANN = 'glurstann'
DRIXBLIXBRIXX = 'drixblixbrixx'
GRONSLORBLEN = 'gronslorblen'
DRARFLELBRANX = 'drarflelbranx'
DRIMKRANX = 'drimkranx'
BLOSFLALGRORN = 'blosflalgrorn'
TRELBLIXBREL = 'trelblixbrel'
STAXSPANCLOR = 'staxspanclor'
VORSKULSTEXT = 'vorskulstext'
STAXVIXBRIX = 'staxvixbrix'
TRARFLEL = 'trarflel'
CLURBRALFLOR = 'clurbralflor'
VOSKRALR = 'voskralr'
DRALBLAXR = 'dralblaxr'
SPEXGRON = 'spexgron'
BLURTROSSKIX = 'blurtrosskix'
SLELSKEXK = 'slelskexk'
TRANGRIXSPURK = 'trangrixspurk'
BRURCLIMK = 'brurclimk'
TRALSLELBRAR = 'tralslelbrar'
SKARBLULFLUR = 'skarblulflur'
GRURVULT = 'grurvult'
KRIXPRENX = 'krixprenx'
TRALSKALL = 'tralskall'
SLELPRAXTRIMT = 'slelpraxtrimt'
DRIMKREN = 'drimkren'
GLIMVEXSPEX = 'glimvexspex'
BLULSPIMFLAX = 'blulspimflax'
KRORSLAN = 'krorslan'

_R = {
    GLIMVEXSPEX: 0,
    BLULSPIMFLAX: 1,
    KRORSLAN: 2,
}

_CTX_READS_KEY = 'flurslex'
_CTX_THRESHOLD = 16

class FlelskalkFSM:
    def __init__(self):
        self._state = {}

    def _vixblalgrim(self, hint):
        assert self._state.get("current") == VIXBLALGRIM, \
            f"flelskalk.vixblalgrim: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'vixblalgrim', 2:
                self._state["current"] = KRORSLAN
                self._state["trig"]    = "hint:2"
            case 'vixblalgrim', _:
                self._state["current"] = DRALGRAR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'vixblalgrim', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'vixblalgrim',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"vixblalgrim->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _dralgrar(self, hint):
        assert self._state.get("current") == DRALGRAR, \
            f"flelskalk.dralgrar: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'dralgrar', 2:
                self._state["current"] = KRORSLAN
                self._state["trig"]    = "hint:2"
            case 'dralgrar', _:
                self._state["current"] = SPOSVEXN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'dralgrar', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'dralgrar',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"dralgrar->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _sposvexn(self, hint):
        assert self._state.get("current") == SPOSVEXN, \
            f"flelskalk.sposvexn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'sposvexn', 2:
                self._state["current"] = KRORSLAN
                self._state["trig"]    = "hint:2"
            case 'sposvexn', _:
                self._state["current"] = GLAXSTIMT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'sposvexn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'sposvexn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"sposvexn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glaxstimt(self, hint):
        assert self._state.get("current") == GLAXSTIMT, \
            f"flelskalk.glaxstimt: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glaxstimt', 2:
                self._state["current"] = KRORSLAN
                self._state["trig"]    = "hint:2"
            case 'glaxstimt', 1:
                self._state["current"] = BLULSPIMFLAX
                self._state["trig"]    = "hint:1"
            case 'glaxstimt', _:
                self._state["current"] = STIMGLORTRUR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glaxstimt', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glaxstimt',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glaxstimt->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _stimglortrur(self, hint):
        assert self._state.get("current") == STIMGLORTRUR, \
            f"flelskalk.stimglortrur: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'stimglortrur', 2:
                self._state["current"] = KRORSLAN
                self._state["trig"]    = "hint:2"
            case 'stimglortrur', _:
                self._state["current"] = GLIMSPURTROS
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'stimglortrur', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'stimglortrur',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"stimglortrur->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glimspurtros(self, hint):
        assert self._state.get("current") == GLIMSPURTROS, \
            f"flelskalk.glimspurtros: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glimspurtros', 2:
                self._state["current"] = KRORSLAN
                self._state["trig"]    = "hint:2"
            case 'glimspurtros', 0:
                self._state["current"] = BLULSPIMFLAX
                self._state["trig"]    = "hint:0"
            case 'glimspurtros', _:
                self._state["current"] = SKEXPRIMGLIM
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glimspurtros', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glimspurtros',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glimspurtros->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skexprimglim(self, hint):
        assert self._state.get("current") == SKEXPRIMGLIM, \
            f"flelskalk.skexprimglim: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skexprimglim', 2:
                self._state["current"] = KRORSLAN
                self._state["trig"]    = "hint:2"
            case 'skexprimglim', _:
                self._state["current"] = DREXSTORFLURR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skexprimglim', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skexprimglim',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skexprimglim->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _drexstorflurr(self, hint):
        assert self._state.get("current") == DREXSTORFLURR, \
            f"flelskalk.drexstorflurr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'drexstorflurr', 2:
                self._state["current"] = KRORSLAN
                self._state["trig"]    = "hint:2"
            case 'drexstorflurr', 0:
                self._state["current"] = SPIMGLOSBLOR
                self._state["trig"]    = "hint:0"
            case 'drexstorflurr', _:
                self._state["current"] = KRENSPELN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'drexstorflurr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'drexstorflurr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"drexstorflurr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _krenspeln(self, hint):
        assert self._state.get("current") == KRENSPELN, \
            f"flelskalk.krenspeln: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'krenspeln', 2:
                self._state["current"] = KRORSLAN
                self._state["trig"]    = "hint:2"
            case 'krenspeln', 1:
                self._state["current"] = BLULSPIMFLAX
                self._state["trig"]    = "hint:1"
            case 'krenspeln', _:
                self._state["current"] = SPIMGLOSBLOR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'krenspeln', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'krenspeln',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"krenspeln->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _spimglosblor(self, hint):
        assert self._state.get("current") == SPIMGLOSBLOR, \
            f"flelskalk.spimglosblor: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'spimglosblor', 2:
                self._state["current"] = KRORSLAN
                self._state["trig"]    = "hint:2"
            case 'spimglosblor', _:
                self._state["current"] = KROSGLUR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'spimglosblor', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'spimglosblor',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"spimglosblor->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _krosglur(self, hint):
        assert self._state.get("current") == KROSGLUR, \
            f"flelskalk.krosglur: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'krosglur', 2:
                self._state["current"] = KRORSLAN
                self._state["trig"]    = "hint:2"
            case 'krosglur', _:
                self._state["current"] = GLORGLULTRIM
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'krosglur', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'krosglur',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"krosglur->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glorglultrim(self, hint):
        assert self._state.get("current") == GLORGLULTRIM, \
            f"flelskalk.glorglultrim: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glorglultrim', 2:
                self._state["current"] = KRORSLAN
                self._state["trig"]    = "hint:2"
            case 'glorglultrim', 1:
                self._state["current"] = KRULPRELBRURT
                self._state["trig"]    = "hint:1"
            case 'glorglultrim', _:
                self._state["current"] = TRIMCLAN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glorglultrim', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glorglultrim',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glorglultrim->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _trimclan(self, hint):
        assert self._state.get("current") == TRIMCLAN, \
            f"flelskalk.trimclan: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'trimclan', 2:
                self._state["current"] = KRORSLAN
                self._state["trig"]    = "hint:2"
            case 'trimclan', 0:
                self._state["current"] = KRONBLAXFLONN
                self._state["trig"]    = "hint:0"
            case 'trimclan', _:
                self._state["current"] = KRULPRELBRURT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'trimclan', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'trimclan',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"trimclan->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _krulprelbrurt(self, hint):
        assert self._state.get("current") == KRULPRELBRURT, \
            f"flelskalk.krulprelbrurt: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'krulprelbrurt', 2:
                self._state["current"] = KRORSLAN
                self._state["trig"]    = "hint:2"
            case 'krulprelbrurt', _:
                self._state["current"] = KRONBLAXFLONN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'krulprelbrurt', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'krulprelbrurt',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"krulprelbrurt->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _kronblaxflonn(self, hint):
        assert self._state.get("current") == KRONBLAXFLONN, \
            f"flelskalk.kronblaxflonn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'kronblaxflonn', 2:
                self._state["current"] = KRORSLAN
                self._state["trig"]    = "hint:2"
            case 'kronblaxflonn', 1:
                self._state["current"] = BLULSPIMFLAX
                self._state["trig"]    = "hint:1"
            case 'kronblaxflonn', _:
                self._state["current"] = GRALPRIM
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'kronblaxflonn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'kronblaxflonn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"kronblaxflonn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _gralprim(self, hint):
        assert self._state.get("current") == GRALPRIM, \
            f"flelskalk.gralprim: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'gralprim', 2:
                self._state["current"] = KRORSLAN
                self._state["trig"]    = "hint:2"
            case 'gralprim', 0:
                self._state["current"] = SKOSSTOSL
                self._state["trig"]    = "hint:0"
            case 'gralprim', _:
                self._state["current"] = SLEXKRAL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'gralprim', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'gralprim',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"gralprim->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slexkral(self, hint):
        assert self._state.get("current") == SLEXKRAL, \
            f"flelskalk.slexkral: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slexkral', 2:
                self._state["current"] = KRORSLAN
                self._state["trig"]    = "hint:2"
            case 'slexkral', _:
                self._state["current"] = SKOSSTOSL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slexkral', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slexkral',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slexkral->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skosstosl(self, hint):
        assert self._state.get("current") == SKOSSTOSL, \
            f"flelskalk.skosstosl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skosstosl', 2:
                self._state["current"] = KRORSLAN
                self._state["trig"]    = "hint:2"
            case 'skosstosl', 1:
                self._state["current"] = GRANFLURSKURN
                self._state["trig"]    = "hint:1"
            case 'skosstosl', _:
                self._state["current"] = SLALDRORSLON
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skosstosl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skosstosl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skosstosl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slaldrorslon(self, hint):
        assert self._state.get("current") == SLALDRORSLON, \
            f"flelskalk.slaldrorslon: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slaldrorslon', 2:
                self._state["current"] = KRORSLAN
                self._state["trig"]    = "hint:2"
            case 'slaldrorslon', _:
                self._state["current"] = GRANFLURSKURN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slaldrorslon', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slaldrorslon',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slaldrorslon->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _granflurskurn(self, hint):
        assert self._state.get("current") == GRANFLURSKURN, \
            f"flelskalk.granflurskurn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'granflurskurn', 2:
                self._state["current"] = KRORSLAN
                self._state["trig"]    = "hint:2"
            case 'granflurskurn', 1:
                self._state["current"] = BLULSPIMFLAX
                self._state["trig"]    = "hint:1"
            case 'granflurskurn', _:
                self._state["current"] = FLALKRULPRAXN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'granflurskurn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'granflurskurn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"granflurskurn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _flalkrulpraxn(self, hint):
        assert self._state.get("current") == FLALKRULPRAXN, \
            f"flelskalk.flalkrulpraxn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'flalkrulpraxn', 2:
                self._state["current"] = KRORSLAN
                self._state["trig"]    = "hint:2"
            case 'flalkrulpraxn', _:
                self._state["current"] = SPULGRULPREL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'flalkrulpraxn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'flalkrulpraxn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"flalkrulpraxn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _spulgrulprel(self, hint):
        assert self._state.get("current") == SPULGRULPREL, \
            f"flelskalk.spulgrulprel: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'spulgrulprel', 2:
                self._state["current"] = KRORSLAN
                self._state["trig"]    = "hint:2"
            case 'spulgrulprel', 0:
                self._state["current"] = BLULSPIMFLAX
                self._state["trig"]    = "hint:0"
            case 'spulgrulprel', _:
                self._state["current"] = VEXBRURK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'spulgrulprel', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'spulgrulprel',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"spulgrulprel->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _vexbrurk(self, hint):
        assert self._state.get("current") == VEXBRURK, \
            f"flelskalk.vexbrurk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'vexbrurk', 2:
                self._state["current"] = KRORSLAN
                self._state["trig"]    = "hint:2"
            case 'vexbrurk', _:
                self._state["current"] = GLIXGLEXL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'vexbrurk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'vexbrurk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"vexbrurk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glixglexl(self, hint):
        assert self._state.get("current") == GLIXGLEXL, \
            f"flelskalk.glixglexl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glixglexl', 2:
                self._state["current"] = KRORSLAN
                self._state["trig"]    = "hint:2"
            case 'glixglexl', _:
                self._state["current"] = STOSBLURN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glixglexl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glixglexl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glixglexl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _stosblurn(self, hint):
        assert self._state.get("current") == STOSBLURN, \
            f"flelskalk.stosblurn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'stosblurn', 2:
                self._state["current"] = KRORSLAN
                self._state["trig"]    = "hint:2"
            case 'stosblurn', 0:
                self._state["current"] = BLULSPIMFLAX
                self._state["trig"]    = "hint:0"
            case 'stosblurn', _:
                self._state["current"] = BLIMGLURN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'stosblurn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'stosblurn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"stosblurn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blimglurn(self, hint):
        assert self._state.get("current") == BLIMGLURN, \
            f"flelskalk.blimglurn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blimglurn', 2:
                self._state["current"] = KRORSLAN
                self._state["trig"]    = "hint:2"
            case 'blimglurn', _:
                self._state["current"] = PRANSKANSKORX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blimglurn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blimglurn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blimglurn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _pranskanskorx(self, hint):
        assert self._state.get("current") == PRANSKANSKORX, \
            f"flelskalk.pranskanskorx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'pranskanskorx', 2:
                self._state["current"] = KRORSLAN
                self._state["trig"]    = "hint:2"
            case 'pranskanskorx', 0:
                self._state["current"] = BLULSPIMFLAX
                self._state["trig"]    = "hint:0"
            case 'pranskanskorx', _:
                self._state["current"] = VALSKEXR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'pranskanskorx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'pranskanskorx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"pranskanskorx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _valskexr(self, hint):
        assert self._state.get("current") == VALSKEXR, \
            f"flelskalk.valskexr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'valskexr', 2:
                self._state["current"] = KRORSLAN
                self._state["trig"]    = "hint:2"
            case 'valskexr', _:
                self._state["current"] = DRANDROSGLULT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'valskexr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'valskexr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"valskexr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _drandrosglult(self, hint):
        assert self._state.get("current") == DRANDROSGLULT, \
            f"flelskalk.drandrosglult: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'drandrosglult', 2:
                self._state["current"] = KRORSLAN
                self._state["trig"]    = "hint:2"
            case 'drandrosglult', 0:
                self._state["current"] = DRULFLAN
                self._state["trig"]    = "hint:0"
            case 'drandrosglult', _:
                self._state["current"] = PRIXSKIMT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'drandrosglult', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'drandrosglult',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"drandrosglult->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _prixskimt(self, hint):
        assert self._state.get("current") == PRIXSKIMT, \
            f"flelskalk.prixskimt: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'prixskimt', 2:
                self._state["current"] = KRORSLAN
                self._state["trig"]    = "hint:2"
            case 'prixskimt', 1:
                self._state["current"] = DRAXPRIMDROS
                self._state["trig"]    = "hint:1"
            case 'prixskimt', _:
                self._state["current"] = DRULFLAN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'prixskimt', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'prixskimt',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"prixskimt->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _drulflan(self, hint):
        assert self._state.get("current") == DRULFLAN, \
            f"flelskalk.drulflan: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'drulflan', 2:
                self._state["current"] = KRORSLAN
                self._state["trig"]    = "hint:2"
            case 'drulflan', _:
                self._state["current"] = DRAXPRIMDROS
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'drulflan', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'drulflan',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"drulflan->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _draxprimdros(self, hint):
        assert self._state.get("current") == DRAXPRIMDROS, \
            f"flelskalk.draxprimdros: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'draxprimdros', 2:
                self._state["current"] = KRORSLAN
                self._state["trig"]    = "hint:2"
            case 'draxprimdros', _:
                self._state["current"] = BRULGLOR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'draxprimdros', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'draxprimdros',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"draxprimdros->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brulglor(self, hint):
        assert self._state.get("current") == BRULGLOR, \
            f"flelskalk.brulglor: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brulglor', 2:
                self._state["current"] = KRORSLAN
                self._state["trig"]    = "hint:2"
            case 'brulglor', _:
                self._state["current"] = SKIMBRALX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brulglor', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brulglor',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brulglor->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skimbralx(self, hint):
        assert self._state.get("current") == SKIMBRALX, \
            f"flelskalk.skimbralx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skimbralx', 2:
                self._state["current"] = KRORSLAN
                self._state["trig"]    = "hint:2"
            case 'skimbralx', 1:
                self._state["current"] = BLULSPIMFLAX
                self._state["trig"]    = "hint:1"
            case 'skimbralx', _:
                self._state["current"] = CLENBLALT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skimbralx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skimbralx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skimbralx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _clenblalt(self, hint):
        assert self._state.get("current") == CLENBLALT, \
            f"flelskalk.clenblalt: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'clenblalt', 2:
                self._state["current"] = KRORSLAN
                self._state["trig"]    = "hint:2"
            case 'clenblalt', _:
                self._state["current"] = BRARSPAXTRORR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'clenblalt', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'clenblalt',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"clenblalt->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brarspaxtrorr(self, hint):
        assert self._state.get("current") == BRARSPAXTRORR, \
            f"flelskalk.brarspaxtrorr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brarspaxtrorr', 2:
                self._state["current"] = KRORSLAN
                self._state["trig"]    = "hint:2"
            case 'brarspaxtrorr', 0:
                self._state["current"] = GRANFLURR
                self._state["trig"]    = "hint:0"
            case 'brarspaxtrorr', _:
                self._state["current"] = CLULGLOSX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brarspaxtrorr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brarspaxtrorr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brarspaxtrorr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _clulglosx(self, hint):
        assert self._state.get("current") == CLULGLOSX, \
            f"flelskalk.clulglosx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'clulglosx', 2:
                self._state["current"] = KRORSLAN
                self._state["trig"]    = "hint:2"
            case 'clulglosx', 0:
                self._state["current"] = BLULSPIMFLAX
                self._state["trig"]    = "hint:0"
            case 'clulglosx', _:
                self._state["current"] = GRANFLURR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'clulglosx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'clulglosx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"clulglosx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _granflurr(self, hint):
        assert self._state.get("current") == GRANFLURR, \
            f"flelskalk.granflurr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'granflurr', 2:
                self._state["current"] = KRORSLAN
                self._state["trig"]    = "hint:2"
            case 'granflurr', _:
                self._state["current"] = SLULSLANKRIM
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'granflurr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'granflurr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"granflurr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slulslankrim(self, hint):
        assert self._state.get("current") == SLULSLANKRIM, \
            f"flelskalk.slulslankrim: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slulslankrim', 2:
                self._state["current"] = KRORSLAN
                self._state["trig"]    = "hint:2"
            case 'slulslankrim', 0:
                self._state["current"] = BLULSPIMFLAX
                self._state["trig"]    = "hint:0"
            case 'slulslankrim', _:
                self._state["current"] = GLURSTANN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slulslankrim', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slulslankrim',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slulslankrim->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glurstann(self, hint):
        assert self._state.get("current") == GLURSTANN, \
            f"flelskalk.glurstann: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glurstann', 2:
                self._state["current"] = KRORSLAN
                self._state["trig"]    = "hint:2"
            case 'glurstann', 1:
                self._state["current"] = GRONSLORBLEN
                self._state["trig"]    = "hint:1"
            case 'glurstann', _:
                self._state["current"] = DRIXBLIXBRIXX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glurstann', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glurstann',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glurstann->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _drixblixbrixx(self, hint):
        assert self._state.get("current") == DRIXBLIXBRIXX, \
            f"flelskalk.drixblixbrixx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'drixblixbrixx', 2:
                self._state["current"] = KRORSLAN
                self._state["trig"]    = "hint:2"
            case 'drixblixbrixx', 1:
                self._state["current"] = DRARFLELBRANX
                self._state["trig"]    = "hint:1"
            case 'drixblixbrixx', _:
                self._state["current"] = GRONSLORBLEN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'drixblixbrixx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'drixblixbrixx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"drixblixbrixx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _gronslorblen(self, hint):
        assert self._state.get("current") == GRONSLORBLEN, \
            f"flelskalk.gronslorblen: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'gronslorblen', 2:
                self._state["current"] = KRORSLAN
                self._state["trig"]    = "hint:2"
            case 'gronslorblen', _:
                self._state["current"] = DRARFLELBRANX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'gronslorblen', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'gronslorblen',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"gronslorblen->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _drarflelbranx(self, hint):
        assert self._state.get("current") == DRARFLELBRANX, \
            f"flelskalk.drarflelbranx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'drarflelbranx', 2:
                self._state["current"] = KRORSLAN
                self._state["trig"]    = "hint:2"
            case 'drarflelbranx', _:
                self._state["current"] = DRIMKRANX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'drarflelbranx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'drarflelbranx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"drarflelbranx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _drimkranx(self, hint):
        assert self._state.get("current") == DRIMKRANX, \
            f"flelskalk.drimkranx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'drimkranx', 2:
                self._state["current"] = KRORSLAN
                self._state["trig"]    = "hint:2"
            case 'drimkranx', 1:
                self._state["current"] = BLULSPIMFLAX
                self._state["trig"]    = "hint:1"
            case 'drimkranx', _:
                self._state["current"] = BLOSFLALGRORN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'drimkranx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'drimkranx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"drimkranx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blosflalgrorn(self, hint):
        assert self._state.get("current") == BLOSFLALGRORN, \
            f"flelskalk.blosflalgrorn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blosflalgrorn', 2:
                self._state["current"] = KRORSLAN
                self._state["trig"]    = "hint:2"
            case 'blosflalgrorn', _:
                self._state["current"] = TRELBLIXBREL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blosflalgrorn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blosflalgrorn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blosflalgrorn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _trelblixbrel(self, hint):
        assert self._state.get("current") == TRELBLIXBREL, \
            f"flelskalk.trelblixbrel: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'trelblixbrel', 2:
                self._state["current"] = KRORSLAN
                self._state["trig"]    = "hint:2"
            case 'trelblixbrel', 0:
                self._state["current"] = VORSKULSTEXT
                self._state["trig"]    = "hint:0"
            case 'trelblixbrel', _:
                self._state["current"] = STAXSPANCLOR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'trelblixbrel', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'trelblixbrel',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"trelblixbrel->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _staxspanclor(self, hint):
        assert self._state.get("current") == STAXSPANCLOR, \
            f"flelskalk.staxspanclor: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'staxspanclor', 2:
                self._state["current"] = KRORSLAN
                self._state["trig"]    = "hint:2"
            case 'staxspanclor', 0:
                self._state["current"] = BLULSPIMFLAX
                self._state["trig"]    = "hint:0"
            case 'staxspanclor', _:
                self._state["current"] = VORSKULSTEXT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'staxspanclor', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'staxspanclor',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"staxspanclor->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _vorskulstext(self, hint):
        assert self._state.get("current") == VORSKULSTEXT, \
            f"flelskalk.vorskulstext: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'vorskulstext', 2:
                self._state["current"] = KRORSLAN
                self._state["trig"]    = "hint:2"
            case 'vorskulstext', 1:
                self._state["current"] = TRARFLEL
                self._state["trig"]    = "hint:1"
            case 'vorskulstext', _:
                self._state["current"] = STAXVIXBRIX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'vorskulstext', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'vorskulstext',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"vorskulstext->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _staxvixbrix(self, hint):
        assert self._state.get("current") == STAXVIXBRIX, \
            f"flelskalk.staxvixbrix: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'staxvixbrix', 2:
                self._state["current"] = KRORSLAN
                self._state["trig"]    = "hint:2"
            case 'staxvixbrix', _:
                self._state["current"] = TRARFLEL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'staxvixbrix', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'staxvixbrix',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"staxvixbrix->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _trarflel(self, hint):
        assert self._state.get("current") == TRARFLEL, \
            f"flelskalk.trarflel: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'trarflel', 2:
                self._state["current"] = KRORSLAN
                self._state["trig"]    = "hint:2"
            case 'trarflel', 1:
                self._state["current"] = VOSKRALR
                self._state["trig"]    = "hint:1"
            case 'trarflel', _:
                self._state["current"] = CLURBRALFLOR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'trarflel', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'trarflel',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"trarflel->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _clurbralflor(self, hint):
        assert self._state.get("current") == CLURBRALFLOR, \
            f"flelskalk.clurbralflor: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'clurbralflor', 2:
                self._state["current"] = KRORSLAN
                self._state["trig"]    = "hint:2"
            case 'clurbralflor', _:
                self._state["current"] = VOSKRALR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'clurbralflor', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'clurbralflor',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"clurbralflor->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _voskralr(self, hint):
        assert self._state.get("current") == VOSKRALR, \
            f"flelskalk.voskralr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'voskralr', 2:
                self._state["current"] = KRORSLAN
                self._state["trig"]    = "hint:2"
            case 'voskralr', 0:
                self._state["current"] = SPEXGRON
                self._state["trig"]    = "hint:0"
            case 'voskralr', _:
                self._state["current"] = DRALBLAXR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'voskralr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'voskralr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"voskralr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _dralblaxr(self, hint):
        assert self._state.get("current") == DRALBLAXR, \
            f"flelskalk.dralblaxr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'dralblaxr', 2:
                self._state["current"] = KRORSLAN
                self._state["trig"]    = "hint:2"
            case 'dralblaxr', 0:
                self._state["current"] = BLURTROSSKIX
                self._state["trig"]    = "hint:0"
            case 'dralblaxr', _:
                self._state["current"] = SPEXGRON
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'dralblaxr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'dralblaxr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"dralblaxr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _spexgron(self, hint):
        assert self._state.get("current") == SPEXGRON, \
            f"flelskalk.spexgron: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'spexgron', 2:
                self._state["current"] = KRORSLAN
                self._state["trig"]    = "hint:2"
            case 'spexgron', 1:
                self._state["current"] = SLELSKEXK
                self._state["trig"]    = "hint:1"
            case 'spexgron', _:
                self._state["current"] = BLURTROSSKIX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'spexgron', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'spexgron',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"spexgron->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blurtrosskix(self, hint):
        assert self._state.get("current") == BLURTROSSKIX, \
            f"flelskalk.blurtrosskix: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blurtrosskix', 2:
                self._state["current"] = KRORSLAN
                self._state["trig"]    = "hint:2"
            case 'blurtrosskix', 0:
                self._state["current"] = BLULSPIMFLAX
                self._state["trig"]    = "hint:0"
            case 'blurtrosskix', _:
                self._state["current"] = SLELSKEXK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blurtrosskix', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blurtrosskix',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blurtrosskix->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slelskexk(self, hint):
        assert self._state.get("current") == SLELSKEXK, \
            f"flelskalk.slelskexk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slelskexk', 2:
                self._state["current"] = KRORSLAN
                self._state["trig"]    = "hint:2"
            case 'slelskexk', 0:
                self._state["current"] = BLULSPIMFLAX
                self._state["trig"]    = "hint:0"
            case 'slelskexk', _:
                self._state["current"] = TRANGRIXSPURK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slelskexk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slelskexk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slelskexk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _trangrixspurk(self, hint):
        assert self._state.get("current") == TRANGRIXSPURK, \
            f"flelskalk.trangrixspurk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'trangrixspurk', 2:
                self._state["current"] = KRORSLAN
                self._state["trig"]    = "hint:2"
            case 'trangrixspurk', _:
                self._state["current"] = BRURCLIMK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'trangrixspurk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'trangrixspurk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"trangrixspurk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brurclimk(self, hint):
        assert self._state.get("current") == BRURCLIMK, \
            f"flelskalk.brurclimk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brurclimk', 2:
                self._state["current"] = KRORSLAN
                self._state["trig"]    = "hint:2"
            case 'brurclimk', _:
                self._state["current"] = TRALSLELBRAR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brurclimk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brurclimk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brurclimk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _tralslelbrar(self, hint):
        assert self._state.get("current") == TRALSLELBRAR, \
            f"flelskalk.tralslelbrar: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'tralslelbrar', 2:
                self._state["current"] = KRORSLAN
                self._state["trig"]    = "hint:2"
            case 'tralslelbrar', _:
                self._state["current"] = SKARBLULFLUR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'tralslelbrar', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'tralslelbrar',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"tralslelbrar->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skarblulflur(self, hint):
        assert self._state.get("current") == SKARBLULFLUR, \
            f"flelskalk.skarblulflur: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skarblulflur', 2:
                self._state["current"] = KRORSLAN
                self._state["trig"]    = "hint:2"
            case 'skarblulflur', _:
                self._state["current"] = GRURVULT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skarblulflur', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skarblulflur',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skarblulflur->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _grurvult(self, hint):
        assert self._state.get("current") == GRURVULT, \
            f"flelskalk.grurvult: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'grurvult', 2:
                self._state["current"] = KRORSLAN
                self._state["trig"]    = "hint:2"
            case 'grurvult', 1:
                self._state["current"] = BLULSPIMFLAX
                self._state["trig"]    = "hint:1"
            case 'grurvult', _:
                self._state["current"] = KRIXPRENX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'grurvult', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'grurvult',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"grurvult->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _krixprenx(self, hint):
        assert self._state.get("current") == KRIXPRENX, \
            f"flelskalk.krixprenx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'krixprenx', 2:
                self._state["current"] = KRORSLAN
                self._state["trig"]    = "hint:2"
            case 'krixprenx', _:
                self._state["current"] = TRALSKALL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'krixprenx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'krixprenx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"krixprenx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _tralskall(self, hint):
        assert self._state.get("current") == TRALSKALL, \
            f"flelskalk.tralskall: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'tralskall', 2:
                self._state["current"] = KRORSLAN
                self._state["trig"]    = "hint:2"
            case 'tralskall', 1:
                self._state["current"] = DRIMKREN
                self._state["trig"]    = "hint:1"
            case 'tralskall', _:
                self._state["current"] = SLELPRAXTRIMT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'tralskall', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'tralskall',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"tralskall->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slelpraxtrimt(self, hint):
        assert self._state.get("current") == SLELPRAXTRIMT, \
            f"flelskalk.slelpraxtrimt: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slelpraxtrimt', 2:
                self._state["current"] = KRORSLAN
                self._state["trig"]    = "hint:2"
            case 'slelpraxtrimt', 1:
                self._state["current"] = BLULSPIMFLAX
                self._state["trig"]    = "hint:1"
            case 'slelpraxtrimt', _:
                self._state["current"] = DRIMKREN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slelpraxtrimt', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slelpraxtrimt',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slelpraxtrimt->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _drimkren(self, hint):
        assert self._state.get("current") == DRIMKREN, \
            f"flelskalk.drimkren: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'drimkren', 2:
                self._state["current"] = KRORSLAN
                self._state["trig"]    = "hint:2"
            case 'drimkren', _:
                self._state["current"] = GLIMVEXSPEX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'drimkren', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'drimkren',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"drimkren->{_to}", _xid_val)
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
            _xid_val = _xid(__name__, 'vixblalgrim', "error", "assert_fail")
            _emit(cycle, 1, __name__, 'vixblalgrim',
                   {"hint": hint, "span": span, "caller": caller},
                   dict(ctx), _conds,
                   "entry_blocked->error", _xid_val, assertion=_asrt)
            return 2, cycle + 1

        self._state = {"current": VIXBLALGRIM, "ctx": ctx,
                        "span": span, "caller": caller,
                        "trig": "auto", "cycle": cycle}
        _dispatch = {
            VIXBLALGRIM: self._vixblalgrim,
            DRALGRAR: self._dralgrar,
            SPOSVEXN: self._sposvexn,
            GLAXSTIMT: self._glaxstimt,
            STIMGLORTRUR: self._stimglortrur,
            GLIMSPURTROS: self._glimspurtros,
            SKEXPRIMGLIM: self._skexprimglim,
            DREXSTORFLURR: self._drexstorflurr,
            KRENSPELN: self._krenspeln,
            SPIMGLOSBLOR: self._spimglosblor,
            KROSGLUR: self._krosglur,
            GLORGLULTRIM: self._glorglultrim,
            TRIMCLAN: self._trimclan,
            KRULPRELBRURT: self._krulprelbrurt,
            KRONBLAXFLONN: self._kronblaxflonn,
            GRALPRIM: self._gralprim,
            SLEXKRAL: self._slexkral,
            SKOSSTOSL: self._skosstosl,
            SLALDRORSLON: self._slaldrorslon,
            GRANFLURSKURN: self._granflurskurn,
            FLALKRULPRAXN: self._flalkrulpraxn,
            SPULGRULPREL: self._spulgrulprel,
            VEXBRURK: self._vexbrurk,
            GLIXGLEXL: self._glixglexl,
            STOSBLURN: self._stosblurn,
            BLIMGLURN: self._blimglurn,
            PRANSKANSKORX: self._pranskanskorx,
            VALSKEXR: self._valskexr,
            DRANDROSGLULT: self._drandrosglult,
            PRIXSKIMT: self._prixskimt,
            DRULFLAN: self._drulflan,
            DRAXPRIMDROS: self._draxprimdros,
            BRULGLOR: self._brulglor,
            SKIMBRALX: self._skimbralx,
            CLENBLALT: self._clenblalt,
            BRARSPAXTRORR: self._brarspaxtrorr,
            CLULGLOSX: self._clulglosx,
            GRANFLURR: self._granflurr,
            SLULSLANKRIM: self._slulslankrim,
            GLURSTANN: self._glurstann,
            DRIXBLIXBRIXX: self._drixblixbrixx,
            GRONSLORBLEN: self._gronslorblen,
            DRARFLELBRANX: self._drarflelbranx,
            DRIMKRANX: self._drimkranx,
            BLOSFLALGRORN: self._blosflalgrorn,
            TRELBLIXBREL: self._trelblixbrel,
            STAXSPANCLOR: self._staxspanclor,
            VORSKULSTEXT: self._vorskulstext,
            STAXVIXBRIX: self._staxvixbrix,
            TRARFLEL: self._trarflel,
            CLURBRALFLOR: self._clurbralflor,
            VOSKRALR: self._voskralr,
            DRALBLAXR: self._dralblaxr,
            SPEXGRON: self._spexgron,
            BLURTROSSKIX: self._blurtrosskix,
            SLELSKEXK: self._slelskexk,
            TRANGRIXSPURK: self._trangrixspurk,
            BRURCLIMK: self._brurclimk,
            TRALSLELBRAR: self._tralslelbrar,
            SKARBLULFLUR: self._skarblulflur,
            GRURVULT: self._grurvult,
            KRIXPRENX: self._krixprenx,
            TRALSKALL: self._tralskall,
            SLELPRAXTRIMT: self._slelpraxtrimt,
            DRIMKREN: self._drimkren,
        }
        while self._state["current"] not in _R and self._state["cycle"] - cycle < 8000:
            _dispatch[self._state["current"]](hint)
        _ret     = _R.get(self._state["current"], -1)
        _is_err  = self._state["current"] == KRORSLAN
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
    return FlelskalkFSM().invoke(hint=hint, span=span, caller=caller, ctx=ctx, cycle=cycle)
