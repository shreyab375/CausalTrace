from _log import _w as _emit, _xid

SLOSBROS = 'slosbros'
SLENDRELFLIMN = 'slendrelflimn'
VULCLENSLEN = 'vulclenslen'
VONDRAL = 'vondral'
BLORSKORBLONX = 'blorskorblonx'
SKIXBLORT = 'skixblort'
BLIMKRANDRON = 'blimkrandron'
GRALGLURK = 'gralglurk'
KRONDROSSLORT = 'krondrosslort'
GRANFLOR = 'granflor'
DRELGLORBLELT = 'drelglorblelt'
BLONSKORSTONN = 'blonskorstonn'
SLARKROSSPEX = 'slarkrosspex'
BRULKRIM = 'brulkrim'
STENSTIMBLON = 'stenstimblon'
BLULSTUL = 'blulstul'
SLELSKIMDRUR = 'slelskimdrur'
BLONCLEX = 'blonclex'
FLARTRAL = 'flartral'
VEXKREX = 'vexkrex'
BLANFLOS = 'blanflos'
BLEXFLELN = 'blexfleln'
STAXGREXX = 'staxgrexx'
TRARSKOSX = 'trarskosx'
FLORSPARK = 'florspark'
CLURGRARL = 'clurgrarl'
VANGLANGLAN = 'vanglanglan'
SKURCLANX = 'skurclanx'
DRONBLAR = 'dronblar'
BRURSLEX = 'brurslex'
GLALCLIMX = 'glalclimx'
GRULPRELGLEX = 'grulprelglex'
STORDREXSKOR = 'stordrexskor'
STARFLURDRORL = 'starflurdrorl'
GRULBRANR = 'grulbranr'
VIMVAN = 'vimvan'
TRENPRENK = 'trenprenk'
FLORTRULSPELX = 'flortrulspelx'
FLIXGRENPRANX = 'flixgrenpranx'
CLANFLONVALR = 'clanflonvalr'
BLULSPOS = 'blulspos'
SPENGLANGLIM = 'spenglanglim'
KRELVAX = 'krelvax'
SKULSTOSN = 'skulstosn'
STALCLAX = 'stalclax'
FLARBRIXR = 'flarbrixr'
FLALDRULX = 'flaldrulx'
KRONTRIM = 'krontrim'
FLIMPRAL = 'flimpral'
TRAXKRANBLUL = 'traxkranblul'
GRONCLOSX = 'gronclosx'
STURSTELT = 'sturstelt'
STALTRORGRURL = 'staltrorgrurl'
KRULGLIX = 'krulglix'
GREXPRORSTIX = 'grexprorstix'
PRELBRULL = 'prelbrull'
FLIMSKEXFLAN = 'flimskexflan'
GRIXFLONX = 'grixflonx'
GRONKRARSPOS = 'gronkrarspos'
VAXPRALVOSX = 'vaxpralvosx'
BLURSKENN = 'blurskenn'
SPENSLONDRUL = 'spenslondrul'
GLELDREL = 'gleldrel'
FLARCLURDREXX = 'flarclurdrexx'
SPELPRALX = 'spelpralx'
TRALGRIXR = 'tralgrixr'
CLELDRUR = 'cleldrur'
GLENTRELBREX = 'glentrelbrex'

_R = {
    TRALGRIXR: 0,
    CLELDRUR: 1,
    GLENTRELBREX: 2,
}

_CTX_READS_KEY = 'flurslex'
_CTX_THRESHOLD = 16

class SlonstexFSM:
    def __init__(self):
        self._state = {}

    def _slosbros(self, hint):
        assert self._state.get("current") == SLOSBROS, \
            f"slonstex.slosbros: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slosbros', 2:
                self._state["current"] = GLENTRELBREX
                self._state["trig"]    = "hint:2"
            case 'slosbros', _:
                self._state["current"] = SLENDRELFLIMN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slosbros', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slosbros',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slosbros->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slendrelflimn(self, hint):
        assert self._state.get("current") == SLENDRELFLIMN, \
            f"slonstex.slendrelflimn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slendrelflimn', 2:
                self._state["current"] = GLENTRELBREX
                self._state["trig"]    = "hint:2"
            case 'slendrelflimn', _:
                self._state["current"] = VULCLENSLEN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slendrelflimn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slendrelflimn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slendrelflimn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _vulclenslen(self, hint):
        assert self._state.get("current") == VULCLENSLEN, \
            f"slonstex.vulclenslen: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'vulclenslen', 2:
                self._state["current"] = GLENTRELBREX
                self._state["trig"]    = "hint:2"
            case 'vulclenslen', _:
                self._state["current"] = VONDRAL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'vulclenslen', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'vulclenslen',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"vulclenslen->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _vondral(self, hint):
        assert self._state.get("current") == VONDRAL, \
            f"slonstex.vondral: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'vondral', 2:
                self._state["current"] = GLENTRELBREX
                self._state["trig"]    = "hint:2"
            case 'vondral', 0:
                self._state["current"] = SKIXBLORT
                self._state["trig"]    = "hint:0"
            case 'vondral', _:
                self._state["current"] = BLORSKORBLONX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'vondral', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'vondral',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"vondral->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blorskorblonx(self, hint):
        assert self._state.get("current") == BLORSKORBLONX, \
            f"slonstex.blorskorblonx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blorskorblonx', 2:
                self._state["current"] = GLENTRELBREX
                self._state["trig"]    = "hint:2"
            case 'blorskorblonx', _:
                self._state["current"] = SKIXBLORT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blorskorblonx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blorskorblonx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blorskorblonx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skixblort(self, hint):
        assert self._state.get("current") == SKIXBLORT, \
            f"slonstex.skixblort: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skixblort', 2:
                self._state["current"] = GLENTRELBREX
                self._state["trig"]    = "hint:2"
            case 'skixblort', _:
                self._state["current"] = BLIMKRANDRON
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skixblort', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skixblort',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skixblort->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blimkrandron(self, hint):
        assert self._state.get("current") == BLIMKRANDRON, \
            f"slonstex.blimkrandron: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blimkrandron', 2:
                self._state["current"] = GLENTRELBREX
                self._state["trig"]    = "hint:2"
            case 'blimkrandron', 0:
                self._state["current"] = CLELDRUR
                self._state["trig"]    = "hint:0"
            case 'blimkrandron', _:
                self._state["current"] = GRALGLURK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blimkrandron', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blimkrandron',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blimkrandron->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _gralglurk(self, hint):
        assert self._state.get("current") == GRALGLURK, \
            f"slonstex.gralglurk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'gralglurk', 2:
                self._state["current"] = GLENTRELBREX
                self._state["trig"]    = "hint:2"
            case 'gralglurk', _:
                self._state["current"] = KRONDROSSLORT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'gralglurk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'gralglurk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"gralglurk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _krondrosslort(self, hint):
        assert self._state.get("current") == KRONDROSSLORT, \
            f"slonstex.krondrosslort: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'krondrosslort', 2:
                self._state["current"] = GLENTRELBREX
                self._state["trig"]    = "hint:2"
            case 'krondrosslort', 0:
                self._state["current"] = DRELGLORBLELT
                self._state["trig"]    = "hint:0"
            case 'krondrosslort', _:
                self._state["current"] = GRANFLOR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'krondrosslort', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'krondrosslort',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"krondrosslort->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _granflor(self, hint):
        assert self._state.get("current") == GRANFLOR, \
            f"slonstex.granflor: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'granflor', 2:
                self._state["current"] = GLENTRELBREX
                self._state["trig"]    = "hint:2"
            case 'granflor', 1:
                self._state["current"] = CLELDRUR
                self._state["trig"]    = "hint:1"
            case 'granflor', _:
                self._state["current"] = DRELGLORBLELT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'granflor', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'granflor',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"granflor->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _drelglorblelt(self, hint):
        assert self._state.get("current") == DRELGLORBLELT, \
            f"slonstex.drelglorblelt: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'drelglorblelt', 2:
                self._state["current"] = GLENTRELBREX
                self._state["trig"]    = "hint:2"
            case 'drelglorblelt', 1:
                self._state["current"] = CLELDRUR
                self._state["trig"]    = "hint:1"
            case 'drelglorblelt', _:
                self._state["current"] = BLONSKORSTONN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'drelglorblelt', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'drelglorblelt',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"drelglorblelt->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blonskorstonn(self, hint):
        assert self._state.get("current") == BLONSKORSTONN, \
            f"slonstex.blonskorstonn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blonskorstonn', 2:
                self._state["current"] = GLENTRELBREX
                self._state["trig"]    = "hint:2"
            case 'blonskorstonn', _:
                self._state["current"] = SLARKROSSPEX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blonskorstonn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blonskorstonn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blonskorstonn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slarkrosspex(self, hint):
        assert self._state.get("current") == SLARKROSSPEX, \
            f"slonstex.slarkrosspex: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slarkrosspex', 2:
                self._state["current"] = GLENTRELBREX
                self._state["trig"]    = "hint:2"
            case 'slarkrosspex', _:
                self._state["current"] = BRULKRIM
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slarkrosspex', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slarkrosspex',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slarkrosspex->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brulkrim(self, hint):
        assert self._state.get("current") == BRULKRIM, \
            f"slonstex.brulkrim: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brulkrim', 2:
                self._state["current"] = GLENTRELBREX
                self._state["trig"]    = "hint:2"
            case 'brulkrim', _:
                self._state["current"] = STENSTIMBLON
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brulkrim', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brulkrim',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brulkrim->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _stenstimblon(self, hint):
        assert self._state.get("current") == STENSTIMBLON, \
            f"slonstex.stenstimblon: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'stenstimblon', 2:
                self._state["current"] = GLENTRELBREX
                self._state["trig"]    = "hint:2"
            case 'stenstimblon', _:
                self._state["current"] = BLULSTUL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'stenstimblon', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'stenstimblon',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"stenstimblon->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blulstul(self, hint):
        assert self._state.get("current") == BLULSTUL, \
            f"slonstex.blulstul: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blulstul', 2:
                self._state["current"] = GLENTRELBREX
                self._state["trig"]    = "hint:2"
            case 'blulstul', _:
                self._state["current"] = SLELSKIMDRUR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blulstul', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blulstul',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blulstul->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slelskimdrur(self, hint):
        assert self._state.get("current") == SLELSKIMDRUR, \
            f"slonstex.slelskimdrur: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slelskimdrur', 2:
                self._state["current"] = GLENTRELBREX
                self._state["trig"]    = "hint:2"
            case 'slelskimdrur', _:
                self._state["current"] = BLONCLEX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slelskimdrur', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slelskimdrur',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slelskimdrur->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blonclex(self, hint):
        assert self._state.get("current") == BLONCLEX, \
            f"slonstex.blonclex: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blonclex', 2:
                self._state["current"] = GLENTRELBREX
                self._state["trig"]    = "hint:2"
            case 'blonclex', _:
                self._state["current"] = FLARTRAL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blonclex', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blonclex',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blonclex->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _flartral(self, hint):
        assert self._state.get("current") == FLARTRAL, \
            f"slonstex.flartral: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'flartral', 2:
                self._state["current"] = GLENTRELBREX
                self._state["trig"]    = "hint:2"
            case 'flartral', _:
                self._state["current"] = VEXKREX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'flartral', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'flartral',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"flartral->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _vexkrex(self, hint):
        assert self._state.get("current") == VEXKREX, \
            f"slonstex.vexkrex: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'vexkrex', 2:
                self._state["current"] = GLENTRELBREX
                self._state["trig"]    = "hint:2"
            case 'vexkrex', 1:
                self._state["current"] = BLEXFLELN
                self._state["trig"]    = "hint:1"
            case 'vexkrex', _:
                self._state["current"] = BLANFLOS
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'vexkrex', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'vexkrex',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"vexkrex->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blanflos(self, hint):
        assert self._state.get("current") == BLANFLOS, \
            f"slonstex.blanflos: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blanflos', 2:
                self._state["current"] = GLENTRELBREX
                self._state["trig"]    = "hint:2"
            case 'blanflos', _:
                self._state["current"] = BLEXFLELN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blanflos', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blanflos',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blanflos->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blexfleln(self, hint):
        assert self._state.get("current") == BLEXFLELN, \
            f"slonstex.blexfleln: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blexfleln', 2:
                self._state["current"] = GLENTRELBREX
                self._state["trig"]    = "hint:2"
            case 'blexfleln', 0:
                self._state["current"] = TRARSKOSX
                self._state["trig"]    = "hint:0"
            case 'blexfleln', _:
                self._state["current"] = STAXGREXX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blexfleln', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blexfleln',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blexfleln->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _staxgrexx(self, hint):
        assert self._state.get("current") == STAXGREXX, \
            f"slonstex.staxgrexx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'staxgrexx', 2:
                self._state["current"] = GLENTRELBREX
                self._state["trig"]    = "hint:2"
            case 'staxgrexx', _:
                self._state["current"] = TRARSKOSX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'staxgrexx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'staxgrexx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"staxgrexx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _trarskosx(self, hint):
        assert self._state.get("current") == TRARSKOSX, \
            f"slonstex.trarskosx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'trarskosx', 2:
                self._state["current"] = GLENTRELBREX
                self._state["trig"]    = "hint:2"
            case 'trarskosx', _:
                self._state["current"] = FLORSPARK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'trarskosx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'trarskosx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"trarskosx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _florspark(self, hint):
        assert self._state.get("current") == FLORSPARK, \
            f"slonstex.florspark: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'florspark', 2:
                self._state["current"] = GLENTRELBREX
                self._state["trig"]    = "hint:2"
            case 'florspark', _:
                self._state["current"] = CLURGRARL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'florspark', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'florspark',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"florspark->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _clurgrarl(self, hint):
        assert self._state.get("current") == CLURGRARL, \
            f"slonstex.clurgrarl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'clurgrarl', 2:
                self._state["current"] = GLENTRELBREX
                self._state["trig"]    = "hint:2"
            case 'clurgrarl', 1:
                self._state["current"] = SKURCLANX
                self._state["trig"]    = "hint:1"
            case 'clurgrarl', _:
                self._state["current"] = VANGLANGLAN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'clurgrarl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'clurgrarl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"clurgrarl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _vanglanglan(self, hint):
        assert self._state.get("current") == VANGLANGLAN, \
            f"slonstex.vanglanglan: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'vanglanglan', 2:
                self._state["current"] = GLENTRELBREX
                self._state["trig"]    = "hint:2"
            case 'vanglanglan', 1:
                self._state["current"] = CLELDRUR
                self._state["trig"]    = "hint:1"
            case 'vanglanglan', _:
                self._state["current"] = SKURCLANX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'vanglanglan', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'vanglanglan',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"vanglanglan->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skurclanx(self, hint):
        assert self._state.get("current") == SKURCLANX, \
            f"slonstex.skurclanx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skurclanx', 2:
                self._state["current"] = GLENTRELBREX
                self._state["trig"]    = "hint:2"
            case 'skurclanx', _:
                self._state["current"] = DRONBLAR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skurclanx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skurclanx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skurclanx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _dronblar(self, hint):
        assert self._state.get("current") == DRONBLAR, \
            f"slonstex.dronblar: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'dronblar', 2:
                self._state["current"] = GLENTRELBREX
                self._state["trig"]    = "hint:2"
            case 'dronblar', _:
                self._state["current"] = BRURSLEX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'dronblar', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'dronblar',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"dronblar->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brurslex(self, hint):
        assert self._state.get("current") == BRURSLEX, \
            f"slonstex.brurslex: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brurslex', 2:
                self._state["current"] = GLENTRELBREX
                self._state["trig"]    = "hint:2"
            case 'brurslex', _:
                self._state["current"] = GLALCLIMX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brurslex', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brurslex',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brurslex->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glalclimx(self, hint):
        assert self._state.get("current") == GLALCLIMX, \
            f"slonstex.glalclimx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glalclimx', 2:
                self._state["current"] = GLENTRELBREX
                self._state["trig"]    = "hint:2"
            case 'glalclimx', 0:
                self._state["current"] = STORDREXSKOR
                self._state["trig"]    = "hint:0"
            case 'glalclimx', _:
                self._state["current"] = GRULPRELGLEX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glalclimx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glalclimx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glalclimx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _grulprelglex(self, hint):
        assert self._state.get("current") == GRULPRELGLEX, \
            f"slonstex.grulprelglex: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'grulprelglex', 2:
                self._state["current"] = GLENTRELBREX
                self._state["trig"]    = "hint:2"
            case 'grulprelglex', _:
                self._state["current"] = STORDREXSKOR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'grulprelglex', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'grulprelglex',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"grulprelglex->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _stordrexskor(self, hint):
        assert self._state.get("current") == STORDREXSKOR, \
            f"slonstex.stordrexskor: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'stordrexskor', 2:
                self._state["current"] = GLENTRELBREX
                self._state["trig"]    = "hint:2"
            case 'stordrexskor', _:
                self._state["current"] = STARFLURDRORL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'stordrexskor', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'stordrexskor',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"stordrexskor->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _starflurdrorl(self, hint):
        assert self._state.get("current") == STARFLURDRORL, \
            f"slonstex.starflurdrorl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'starflurdrorl', 2:
                self._state["current"] = GLENTRELBREX
                self._state["trig"]    = "hint:2"
            case 'starflurdrorl', _:
                self._state["current"] = GRULBRANR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'starflurdrorl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'starflurdrorl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"starflurdrorl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _grulbranr(self, hint):
        assert self._state.get("current") == GRULBRANR, \
            f"slonstex.grulbranr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'grulbranr', 2:
                self._state["current"] = GLENTRELBREX
                self._state["trig"]    = "hint:2"
            case 'grulbranr', 1:
                self._state["current"] = CLELDRUR
                self._state["trig"]    = "hint:1"
            case 'grulbranr', _:
                self._state["current"] = VIMVAN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'grulbranr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'grulbranr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"grulbranr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _vimvan(self, hint):
        assert self._state.get("current") == VIMVAN, \
            f"slonstex.vimvan: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'vimvan', 2:
                self._state["current"] = GLENTRELBREX
                self._state["trig"]    = "hint:2"
            case 'vimvan', 1:
                self._state["current"] = FLORTRULSPELX
                self._state["trig"]    = "hint:1"
            case 'vimvan', _:
                self._state["current"] = TRENPRENK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'vimvan', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'vimvan',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"vimvan->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _trenprenk(self, hint):
        assert self._state.get("current") == TRENPRENK, \
            f"slonstex.trenprenk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'trenprenk', 2:
                self._state["current"] = GLENTRELBREX
                self._state["trig"]    = "hint:2"
            case 'trenprenk', 0:
                self._state["current"] = CLELDRUR
                self._state["trig"]    = "hint:0"
            case 'trenprenk', _:
                self._state["current"] = FLORTRULSPELX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'trenprenk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'trenprenk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"trenprenk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _flortrulspelx(self, hint):
        assert self._state.get("current") == FLORTRULSPELX, \
            f"slonstex.flortrulspelx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'flortrulspelx', 2:
                self._state["current"] = GLENTRELBREX
                self._state["trig"]    = "hint:2"
            case 'flortrulspelx', 1:
                self._state["current"] = CLANFLONVALR
                self._state["trig"]    = "hint:1"
            case 'flortrulspelx', _:
                self._state["current"] = FLIXGRENPRANX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'flortrulspelx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'flortrulspelx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"flortrulspelx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _flixgrenpranx(self, hint):
        assert self._state.get("current") == FLIXGRENPRANX, \
            f"slonstex.flixgrenpranx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'flixgrenpranx', 2:
                self._state["current"] = GLENTRELBREX
                self._state["trig"]    = "hint:2"
            case 'flixgrenpranx', _:
                self._state["current"] = CLANFLONVALR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'flixgrenpranx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'flixgrenpranx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"flixgrenpranx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _clanflonvalr(self, hint):
        assert self._state.get("current") == CLANFLONVALR, \
            f"slonstex.clanflonvalr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'clanflonvalr', 2:
                self._state["current"] = GLENTRELBREX
                self._state["trig"]    = "hint:2"
            case 'clanflonvalr', _:
                self._state["current"] = BLULSPOS
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'clanflonvalr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'clanflonvalr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"clanflonvalr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blulspos(self, hint):
        assert self._state.get("current") == BLULSPOS, \
            f"slonstex.blulspos: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blulspos', 2:
                self._state["current"] = GLENTRELBREX
                self._state["trig"]    = "hint:2"
            case 'blulspos', _:
                self._state["current"] = SPENGLANGLIM
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blulspos', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blulspos',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blulspos->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _spenglanglim(self, hint):
        assert self._state.get("current") == SPENGLANGLIM, \
            f"slonstex.spenglanglim: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'spenglanglim', 2:
                self._state["current"] = GLENTRELBREX
                self._state["trig"]    = "hint:2"
            case 'spenglanglim', 1:
                self._state["current"] = CLELDRUR
                self._state["trig"]    = "hint:1"
            case 'spenglanglim', _:
                self._state["current"] = KRELVAX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'spenglanglim', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'spenglanglim',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"spenglanglim->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _krelvax(self, hint):
        assert self._state.get("current") == KRELVAX, \
            f"slonstex.krelvax: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'krelvax', 2:
                self._state["current"] = GLENTRELBREX
                self._state["trig"]    = "hint:2"
            case 'krelvax', 0:
                self._state["current"] = STALCLAX
                self._state["trig"]    = "hint:0"
            case 'krelvax', _:
                self._state["current"] = SKULSTOSN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'krelvax', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'krelvax',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"krelvax->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skulstosn(self, hint):
        assert self._state.get("current") == SKULSTOSN, \
            f"slonstex.skulstosn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skulstosn', 2:
                self._state["current"] = GLENTRELBREX
                self._state["trig"]    = "hint:2"
            case 'skulstosn', 0:
                self._state["current"] = CLELDRUR
                self._state["trig"]    = "hint:0"
            case 'skulstosn', _:
                self._state["current"] = STALCLAX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skulstosn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skulstosn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skulstosn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _stalclax(self, hint):
        assert self._state.get("current") == STALCLAX, \
            f"slonstex.stalclax: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'stalclax', 2:
                self._state["current"] = GLENTRELBREX
                self._state["trig"]    = "hint:2"
            case 'stalclax', _:
                self._state["current"] = FLARBRIXR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'stalclax', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'stalclax',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"stalclax->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _flarbrixr(self, hint):
        assert self._state.get("current") == FLARBRIXR, \
            f"slonstex.flarbrixr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'flarbrixr', 2:
                self._state["current"] = GLENTRELBREX
                self._state["trig"]    = "hint:2"
            case 'flarbrixr', 0:
                self._state["current"] = KRONTRIM
                self._state["trig"]    = "hint:0"
            case 'flarbrixr', _:
                self._state["current"] = FLALDRULX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'flarbrixr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'flarbrixr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"flarbrixr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _flaldrulx(self, hint):
        assert self._state.get("current") == FLALDRULX, \
            f"slonstex.flaldrulx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'flaldrulx', 2:
                self._state["current"] = GLENTRELBREX
                self._state["trig"]    = "hint:2"
            case 'flaldrulx', _:
                self._state["current"] = KRONTRIM
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'flaldrulx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'flaldrulx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"flaldrulx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _krontrim(self, hint):
        assert self._state.get("current") == KRONTRIM, \
            f"slonstex.krontrim: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'krontrim', 2:
                self._state["current"] = GLENTRELBREX
                self._state["trig"]    = "hint:2"
            case 'krontrim', 0:
                self._state["current"] = CLELDRUR
                self._state["trig"]    = "hint:0"
            case 'krontrim', _:
                self._state["current"] = FLIMPRAL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'krontrim', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'krontrim',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"krontrim->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _flimpral(self, hint):
        assert self._state.get("current") == FLIMPRAL, \
            f"slonstex.flimpral: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'flimpral', 2:
                self._state["current"] = GLENTRELBREX
                self._state["trig"]    = "hint:2"
            case 'flimpral', 0:
                self._state["current"] = GRONCLOSX
                self._state["trig"]    = "hint:0"
            case 'flimpral', _:
                self._state["current"] = TRAXKRANBLUL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'flimpral', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'flimpral',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"flimpral->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _traxkranblul(self, hint):
        assert self._state.get("current") == TRAXKRANBLUL, \
            f"slonstex.traxkranblul: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'traxkranblul', 2:
                self._state["current"] = GLENTRELBREX
                self._state["trig"]    = "hint:2"
            case 'traxkranblul', 1:
                self._state["current"] = STURSTELT
                self._state["trig"]    = "hint:1"
            case 'traxkranblul', _:
                self._state["current"] = GRONCLOSX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'traxkranblul', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'traxkranblul',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"traxkranblul->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _gronclosx(self, hint):
        assert self._state.get("current") == GRONCLOSX, \
            f"slonstex.gronclosx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'gronclosx', 2:
                self._state["current"] = GLENTRELBREX
                self._state["trig"]    = "hint:2"
            case 'gronclosx', 0:
                self._state["current"] = STALTRORGRURL
                self._state["trig"]    = "hint:0"
            case 'gronclosx', _:
                self._state["current"] = STURSTELT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'gronclosx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'gronclosx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"gronclosx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _sturstelt(self, hint):
        assert self._state.get("current") == STURSTELT, \
            f"slonstex.sturstelt: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'sturstelt', 2:
                self._state["current"] = GLENTRELBREX
                self._state["trig"]    = "hint:2"
            case 'sturstelt', _:
                self._state["current"] = STALTRORGRURL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'sturstelt', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'sturstelt',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"sturstelt->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _staltrorgrurl(self, hint):
        assert self._state.get("current") == STALTRORGRURL, \
            f"slonstex.staltrorgrurl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'staltrorgrurl', 2:
                self._state["current"] = GLENTRELBREX
                self._state["trig"]    = "hint:2"
            case 'staltrorgrurl', _:
                self._state["current"] = KRULGLIX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'staltrorgrurl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'staltrorgrurl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"staltrorgrurl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _krulglix(self, hint):
        assert self._state.get("current") == KRULGLIX, \
            f"slonstex.krulglix: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'krulglix', 2:
                self._state["current"] = GLENTRELBREX
                self._state["trig"]    = "hint:2"
            case 'krulglix', 1:
                self._state["current"] = CLELDRUR
                self._state["trig"]    = "hint:1"
            case 'krulglix', _:
                self._state["current"] = GREXPRORSTIX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'krulglix', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'krulglix',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"krulglix->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _grexprorstix(self, hint):
        assert self._state.get("current") == GREXPRORSTIX, \
            f"slonstex.grexprorstix: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'grexprorstix', 2:
                self._state["current"] = GLENTRELBREX
                self._state["trig"]    = "hint:2"
            case 'grexprorstix', 1:
                self._state["current"] = FLIMSKEXFLAN
                self._state["trig"]    = "hint:1"
            case 'grexprorstix', _:
                self._state["current"] = PRELBRULL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'grexprorstix', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'grexprorstix',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"grexprorstix->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _prelbrull(self, hint):
        assert self._state.get("current") == PRELBRULL, \
            f"slonstex.prelbrull: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'prelbrull', 2:
                self._state["current"] = GLENTRELBREX
                self._state["trig"]    = "hint:2"
            case 'prelbrull', 0:
                self._state["current"] = CLELDRUR
                self._state["trig"]    = "hint:0"
            case 'prelbrull', _:
                self._state["current"] = FLIMSKEXFLAN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'prelbrull', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'prelbrull',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"prelbrull->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _flimskexflan(self, hint):
        assert self._state.get("current") == FLIMSKEXFLAN, \
            f"slonstex.flimskexflan: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'flimskexflan', 2:
                self._state["current"] = GLENTRELBREX
                self._state["trig"]    = "hint:2"
            case 'flimskexflan', _:
                self._state["current"] = GRIXFLONX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'flimskexflan', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'flimskexflan',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"flimskexflan->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _grixflonx(self, hint):
        assert self._state.get("current") == GRIXFLONX, \
            f"slonstex.grixflonx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'grixflonx', 2:
                self._state["current"] = GLENTRELBREX
                self._state["trig"]    = "hint:2"
            case 'grixflonx', 0:
                self._state["current"] = VAXPRALVOSX
                self._state["trig"]    = "hint:0"
            case 'grixflonx', _:
                self._state["current"] = GRONKRARSPOS
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'grixflonx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'grixflonx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"grixflonx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _gronkrarspos(self, hint):
        assert self._state.get("current") == GRONKRARSPOS, \
            f"slonstex.gronkrarspos: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'gronkrarspos', 2:
                self._state["current"] = GLENTRELBREX
                self._state["trig"]    = "hint:2"
            case 'gronkrarspos', _:
                self._state["current"] = VAXPRALVOSX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'gronkrarspos', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'gronkrarspos',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"gronkrarspos->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _vaxpralvosx(self, hint):
        assert self._state.get("current") == VAXPRALVOSX, \
            f"slonstex.vaxpralvosx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'vaxpralvosx', 2:
                self._state["current"] = GLENTRELBREX
                self._state["trig"]    = "hint:2"
            case 'vaxpralvosx', _:
                self._state["current"] = BLURSKENN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'vaxpralvosx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'vaxpralvosx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"vaxpralvosx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blurskenn(self, hint):
        assert self._state.get("current") == BLURSKENN, \
            f"slonstex.blurskenn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blurskenn', 2:
                self._state["current"] = GLENTRELBREX
                self._state["trig"]    = "hint:2"
            case 'blurskenn', 0:
                self._state["current"] = GLELDREL
                self._state["trig"]    = "hint:0"
            case 'blurskenn', _:
                self._state["current"] = SPENSLONDRUL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blurskenn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blurskenn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blurskenn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _spenslondrul(self, hint):
        assert self._state.get("current") == SPENSLONDRUL, \
            f"slonstex.spenslondrul: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'spenslondrul', 2:
                self._state["current"] = GLENTRELBREX
                self._state["trig"]    = "hint:2"
            case 'spenslondrul', 0:
                self._state["current"] = CLELDRUR
                self._state["trig"]    = "hint:0"
            case 'spenslondrul', _:
                self._state["current"] = GLELDREL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'spenslondrul', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'spenslondrul',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"spenslondrul->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _gleldrel(self, hint):
        assert self._state.get("current") == GLELDREL, \
            f"slonstex.gleldrel: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'gleldrel', 2:
                self._state["current"] = GLENTRELBREX
                self._state["trig"]    = "hint:2"
            case 'gleldrel', _:
                self._state["current"] = FLARCLURDREXX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'gleldrel', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'gleldrel',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"gleldrel->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _flarclurdrexx(self, hint):
        assert self._state.get("current") == FLARCLURDREXX, \
            f"slonstex.flarclurdrexx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'flarclurdrexx', 2:
                self._state["current"] = GLENTRELBREX
                self._state["trig"]    = "hint:2"
            case 'flarclurdrexx', 0:
                self._state["current"] = CLELDRUR
                self._state["trig"]    = "hint:0"
            case 'flarclurdrexx', _:
                self._state["current"] = SPELPRALX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'flarclurdrexx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'flarclurdrexx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"flarclurdrexx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _spelpralx(self, hint):
        assert self._state.get("current") == SPELPRALX, \
            f"slonstex.spelpralx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'spelpralx', 2:
                self._state["current"] = GLENTRELBREX
                self._state["trig"]    = "hint:2"
            case 'spelpralx', 0:
                self._state["current"] = CLELDRUR
                self._state["trig"]    = "hint:0"
            case 'spelpralx', _:
                self._state["current"] = TRALGRIXR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'spelpralx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'spelpralx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"spelpralx->{_to}", _xid_val)
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
            _xid_val = _xid(__name__, 'slosbros', "error", "assert_fail")
            _emit(cycle, 1, __name__, 'slosbros',
                   {"hint": hint, "span": span, "caller": caller},
                   dict(ctx), _conds,
                   "entry_blocked->error", _xid_val, assertion=_asrt)
            return 2, cycle + 1

        self._state = {"current": SLOSBROS, "ctx": ctx,
                        "span": span, "caller": caller,
                        "trig": "auto", "cycle": cycle}
        _dispatch = {
            SLOSBROS: self._slosbros,
            SLENDRELFLIMN: self._slendrelflimn,
            VULCLENSLEN: self._vulclenslen,
            VONDRAL: self._vondral,
            BLORSKORBLONX: self._blorskorblonx,
            SKIXBLORT: self._skixblort,
            BLIMKRANDRON: self._blimkrandron,
            GRALGLURK: self._gralglurk,
            KRONDROSSLORT: self._krondrosslort,
            GRANFLOR: self._granflor,
            DRELGLORBLELT: self._drelglorblelt,
            BLONSKORSTONN: self._blonskorstonn,
            SLARKROSSPEX: self._slarkrosspex,
            BRULKRIM: self._brulkrim,
            STENSTIMBLON: self._stenstimblon,
            BLULSTUL: self._blulstul,
            SLELSKIMDRUR: self._slelskimdrur,
            BLONCLEX: self._blonclex,
            FLARTRAL: self._flartral,
            VEXKREX: self._vexkrex,
            BLANFLOS: self._blanflos,
            BLEXFLELN: self._blexfleln,
            STAXGREXX: self._staxgrexx,
            TRARSKOSX: self._trarskosx,
            FLORSPARK: self._florspark,
            CLURGRARL: self._clurgrarl,
            VANGLANGLAN: self._vanglanglan,
            SKURCLANX: self._skurclanx,
            DRONBLAR: self._dronblar,
            BRURSLEX: self._brurslex,
            GLALCLIMX: self._glalclimx,
            GRULPRELGLEX: self._grulprelglex,
            STORDREXSKOR: self._stordrexskor,
            STARFLURDRORL: self._starflurdrorl,
            GRULBRANR: self._grulbranr,
            VIMVAN: self._vimvan,
            TRENPRENK: self._trenprenk,
            FLORTRULSPELX: self._flortrulspelx,
            FLIXGRENPRANX: self._flixgrenpranx,
            CLANFLONVALR: self._clanflonvalr,
            BLULSPOS: self._blulspos,
            SPENGLANGLIM: self._spenglanglim,
            KRELVAX: self._krelvax,
            SKULSTOSN: self._skulstosn,
            STALCLAX: self._stalclax,
            FLARBRIXR: self._flarbrixr,
            FLALDRULX: self._flaldrulx,
            KRONTRIM: self._krontrim,
            FLIMPRAL: self._flimpral,
            TRAXKRANBLUL: self._traxkranblul,
            GRONCLOSX: self._gronclosx,
            STURSTELT: self._sturstelt,
            STALTRORGRURL: self._staltrorgrurl,
            KRULGLIX: self._krulglix,
            GREXPRORSTIX: self._grexprorstix,
            PRELBRULL: self._prelbrull,
            FLIMSKEXFLAN: self._flimskexflan,
            GRIXFLONX: self._grixflonx,
            GRONKRARSPOS: self._gronkrarspos,
            VAXPRALVOSX: self._vaxpralvosx,
            BLURSKENN: self._blurskenn,
            SPENSLONDRUL: self._spenslondrul,
            GLELDREL: self._gleldrel,
            FLARCLURDREXX: self._flarclurdrexx,
            SPELPRALX: self._spelpralx,
        }
        while self._state["current"] not in _R and self._state["cycle"] - cycle < 8000:
            _dispatch[self._state["current"]](hint)
        _ret     = _R.get(self._state["current"], -1)
        _is_err  = self._state["current"] == GLENTRELBREX
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
    return SlonstexFSM().invoke(hint=hint, span=span, caller=caller, ctx=ctx, cycle=cycle)
