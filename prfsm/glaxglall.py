from _log import _w as _emit, _xid

SKIXKRANFLIMX = 'skixkranflimx'
GLOSTRIXT = 'glostrixt'
DRIMCLIM = 'drimclim'
GLARDRELBLOSX = 'glardrelblosx'
SPORSLORSLIXT = 'sporslorslixt'
PRAXTRIM = 'praxtrim'
BRIXBLELSKELR = 'brixblelskelr'
KRONSLULSKIM = 'kronslulskim'
FLURSTIX = 'flurstix'
TRURSLEXGRENN = 'trurslexgrenn'
SKARSPIXGROR = 'skarspixgror'
KRURTRIXBLENL = 'krurtrixblenl'
CLAXSLIXR = 'claxslixr'
PRIMBLAL = 'primblal'
CLURVULSPENT = 'clurvulspent'
TRONBRULDRULX = 'tronbruldrulx'
GRAXBRORKRIX = 'graxbrorkrix'
SKANTRENX = 'skantrenx'
CLORDRIM = 'clordrim'
STELFLAXL = 'stelflaxl'
SKULSTOS = 'skulstos'
TRAXKREXT = 'traxkrext'
SPALGLUR = 'spalglur'
STEXBRUL = 'stexbrul'
VURBLIM = 'vurblim'
GLELSTOS = 'glelstos'
GLARFLURX = 'glarflurx'
FLORBLURX = 'florblurx'
FLOSVEXFLANX = 'flosvexflanx'
BRORSKORN = 'brorskorn'
SPURSTARBLART = 'spurstarblart'
KRALSPURR = 'kralspurr'
VAXBREX = 'vaxbrex'
FLEXCLULSLEXK = 'flexclulslexk'
GLIMSPONSKONL = 'glimsponskonl'
KREXSKARKRURT = 'krexskarkrurt'
SKAXDRIMSLULL = 'skaxdrimslull'
VENBRIXGLANK = 'venbrixglank'
BROSSPUR = 'brosspur'
PRURSTULT = 'prurstult'
SLARSTARK = 'slarstark'
GRIXBRORTRANX = 'grixbrortranx'
STENVENR = 'stenvenr'
DRIMSTENSKEX = 'drimstenskex'
SLOSSKARL = 'slosskarl'
STEXKRAN = 'stexkran'
CLONFLAXN = 'clonflaxn'
PREXGRANL = 'prexgranl'
GRIMGRAXGRAN = 'grimgraxgran'
SLARGLARN = 'slarglarn'
PRURFLON = 'prurflon'
KROSTREN = 'krostren'
CLONPRAXKROR = 'clonpraxkror'
DRIMTRAXT = 'drimtraxt'
STANKRIXX = 'stankrixx'
GLOSSLORTREX = 'glosslortrex'
VELKROSK = 'velkrosk'
GLELBLARSLOR = 'glelblarslor'
DRELPRARGLEN = 'drelprarglen'
SKARSTIMFLEX = 'skarstimflex'
PRALGREXKRAL = 'pralgrexkral'
GLIMGLIXBLOSR = 'glimglixblosr'
GREXSTARCLULN = 'grexstarcluln'
GLOSSTELSKOR = 'glosstelskor'
SLIXBROR = 'slixbror'
TRONTRULSPENX = 'trontrulspenx'
SPARSLALL = 'sparslall'
TRULSKULR = 'trulskulr'

_R = {
    TRONTRULSPENX: 0,
    SPARSLALL: 1,
    TRULSKULR: 2,
}

_CTX_READS_KEY = 'flurslex'
_CTX_THRESHOLD = 16

class GlaxglallFSM:
    def __init__(self):
        self._state = {}

    def _skixkranflimx(self, hint):
        assert self._state.get("current") == SKIXKRANFLIMX, \
            f"glaxglall.skixkranflimx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skixkranflimx', 2:
                self._state["current"] = TRULSKULR
                self._state["trig"]    = "hint:2"
            case 'skixkranflimx', _:
                self._state["current"] = GLOSTRIXT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skixkranflimx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skixkranflimx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skixkranflimx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glostrixt(self, hint):
        assert self._state.get("current") == GLOSTRIXT, \
            f"glaxglall.glostrixt: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glostrixt', 2:
                self._state["current"] = TRULSKULR
                self._state["trig"]    = "hint:2"
            case 'glostrixt', 1:
                self._state["current"] = GLARDRELBLOSX
                self._state["trig"]    = "hint:1"
            case 'glostrixt', _:
                self._state["current"] = DRIMCLIM
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glostrixt', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glostrixt',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glostrixt->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _drimclim(self, hint):
        assert self._state.get("current") == DRIMCLIM, \
            f"glaxglall.drimclim: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'drimclim', 2:
                self._state["current"] = TRULSKULR
                self._state["trig"]    = "hint:2"
            case 'drimclim', 1:
                self._state["current"] = SPARSLALL
                self._state["trig"]    = "hint:1"
            case 'drimclim', _:
                self._state["current"] = GLARDRELBLOSX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'drimclim', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'drimclim',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"drimclim->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glardrelblosx(self, hint):
        assert self._state.get("current") == GLARDRELBLOSX, \
            f"glaxglall.glardrelblosx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glardrelblosx', 2:
                self._state["current"] = TRULSKULR
                self._state["trig"]    = "hint:2"
            case 'glardrelblosx', _:
                self._state["current"] = SPORSLORSLIXT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glardrelblosx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glardrelblosx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glardrelblosx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _sporslorslixt(self, hint):
        assert self._state.get("current") == SPORSLORSLIXT, \
            f"glaxglall.sporslorslixt: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'sporslorslixt', 2:
                self._state["current"] = TRULSKULR
                self._state["trig"]    = "hint:2"
            case 'sporslorslixt', 0:
                self._state["current"] = SPARSLALL
                self._state["trig"]    = "hint:0"
            case 'sporslorslixt', _:
                self._state["current"] = PRAXTRIM
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'sporslorslixt', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'sporslorslixt',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"sporslorslixt->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _praxtrim(self, hint):
        assert self._state.get("current") == PRAXTRIM, \
            f"glaxglall.praxtrim: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'praxtrim', 2:
                self._state["current"] = TRULSKULR
                self._state["trig"]    = "hint:2"
            case 'praxtrim', 0:
                self._state["current"] = SPARSLALL
                self._state["trig"]    = "hint:0"
            case 'praxtrim', _:
                self._state["current"] = BRIXBLELSKELR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'praxtrim', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'praxtrim',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"praxtrim->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brixblelskelr(self, hint):
        assert self._state.get("current") == BRIXBLELSKELR, \
            f"glaxglall.brixblelskelr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brixblelskelr', 2:
                self._state["current"] = TRULSKULR
                self._state["trig"]    = "hint:2"
            case 'brixblelskelr', 0:
                self._state["current"] = SPARSLALL
                self._state["trig"]    = "hint:0"
            case 'brixblelskelr', _:
                self._state["current"] = KRONSLULSKIM
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brixblelskelr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brixblelskelr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brixblelskelr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _kronslulskim(self, hint):
        assert self._state.get("current") == KRONSLULSKIM, \
            f"glaxglall.kronslulskim: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'kronslulskim', 2:
                self._state["current"] = TRULSKULR
                self._state["trig"]    = "hint:2"
            case 'kronslulskim', 1:
                self._state["current"] = SPARSLALL
                self._state["trig"]    = "hint:1"
            case 'kronslulskim', _:
                self._state["current"] = FLURSTIX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'kronslulskim', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'kronslulskim',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"kronslulskim->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _flurstix(self, hint):
        assert self._state.get("current") == FLURSTIX, \
            f"glaxglall.flurstix: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'flurstix', 2:
                self._state["current"] = TRULSKULR
                self._state["trig"]    = "hint:2"
            case 'flurstix', _:
                self._state["current"] = TRURSLEXGRENN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'flurstix', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'flurstix',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"flurstix->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _trurslexgrenn(self, hint):
        assert self._state.get("current") == TRURSLEXGRENN, \
            f"glaxglall.trurslexgrenn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'trurslexgrenn', 2:
                self._state["current"] = TRULSKULR
                self._state["trig"]    = "hint:2"
            case 'trurslexgrenn', 0:
                self._state["current"] = KRURTRIXBLENL
                self._state["trig"]    = "hint:0"
            case 'trurslexgrenn', _:
                self._state["current"] = SKARSPIXGROR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'trurslexgrenn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'trurslexgrenn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"trurslexgrenn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skarspixgror(self, hint):
        assert self._state.get("current") == SKARSPIXGROR, \
            f"glaxglall.skarspixgror: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skarspixgror', 2:
                self._state["current"] = TRULSKULR
                self._state["trig"]    = "hint:2"
            case 'skarspixgror', 1:
                self._state["current"] = SPARSLALL
                self._state["trig"]    = "hint:1"
            case 'skarspixgror', _:
                self._state["current"] = KRURTRIXBLENL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skarspixgror', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skarspixgror',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skarspixgror->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _krurtrixblenl(self, hint):
        assert self._state.get("current") == KRURTRIXBLENL, \
            f"glaxglall.krurtrixblenl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'krurtrixblenl', 2:
                self._state["current"] = TRULSKULR
                self._state["trig"]    = "hint:2"
            case 'krurtrixblenl', _:
                self._state["current"] = CLAXSLIXR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'krurtrixblenl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'krurtrixblenl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"krurtrixblenl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _claxslixr(self, hint):
        assert self._state.get("current") == CLAXSLIXR, \
            f"glaxglall.claxslixr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'claxslixr', 2:
                self._state["current"] = TRULSKULR
                self._state["trig"]    = "hint:2"
            case 'claxslixr', _:
                self._state["current"] = PRIMBLAL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'claxslixr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'claxslixr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"claxslixr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _primblal(self, hint):
        assert self._state.get("current") == PRIMBLAL, \
            f"glaxglall.primblal: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'primblal', 2:
                self._state["current"] = TRULSKULR
                self._state["trig"]    = "hint:2"
            case 'primblal', _:
                self._state["current"] = CLURVULSPENT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'primblal', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'primblal',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"primblal->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _clurvulspent(self, hint):
        assert self._state.get("current") == CLURVULSPENT, \
            f"glaxglall.clurvulspent: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'clurvulspent', 2:
                self._state["current"] = TRULSKULR
                self._state["trig"]    = "hint:2"
            case 'clurvulspent', _:
                self._state["current"] = TRONBRULDRULX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'clurvulspent', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'clurvulspent',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"clurvulspent->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _tronbruldrulx(self, hint):
        assert self._state.get("current") == TRONBRULDRULX, \
            f"glaxglall.tronbruldrulx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'tronbruldrulx', 2:
                self._state["current"] = TRULSKULR
                self._state["trig"]    = "hint:2"
            case 'tronbruldrulx', 0:
                self._state["current"] = SKANTRENX
                self._state["trig"]    = "hint:0"
            case 'tronbruldrulx', _:
                self._state["current"] = GRAXBRORKRIX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'tronbruldrulx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'tronbruldrulx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"tronbruldrulx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _graxbrorkrix(self, hint):
        assert self._state.get("current") == GRAXBRORKRIX, \
            f"glaxglall.graxbrorkrix: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'graxbrorkrix', 2:
                self._state["current"] = TRULSKULR
                self._state["trig"]    = "hint:2"
            case 'graxbrorkrix', 0:
                self._state["current"] = CLORDRIM
                self._state["trig"]    = "hint:0"
            case 'graxbrorkrix', _:
                self._state["current"] = SKANTRENX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'graxbrorkrix', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'graxbrorkrix',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"graxbrorkrix->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skantrenx(self, hint):
        assert self._state.get("current") == SKANTRENX, \
            f"glaxglall.skantrenx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skantrenx', 2:
                self._state["current"] = TRULSKULR
                self._state["trig"]    = "hint:2"
            case 'skantrenx', 1:
                self._state["current"] = SPARSLALL
                self._state["trig"]    = "hint:1"
            case 'skantrenx', _:
                self._state["current"] = CLORDRIM
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skantrenx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skantrenx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skantrenx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _clordrim(self, hint):
        assert self._state.get("current") == CLORDRIM, \
            f"glaxglall.clordrim: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'clordrim', 2:
                self._state["current"] = TRULSKULR
                self._state["trig"]    = "hint:2"
            case 'clordrim', _:
                self._state["current"] = STELFLAXL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'clordrim', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'clordrim',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"clordrim->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _stelflaxl(self, hint):
        assert self._state.get("current") == STELFLAXL, \
            f"glaxglall.stelflaxl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'stelflaxl', 2:
                self._state["current"] = TRULSKULR
                self._state["trig"]    = "hint:2"
            case 'stelflaxl', 0:
                self._state["current"] = SPARSLALL
                self._state["trig"]    = "hint:0"
            case 'stelflaxl', _:
                self._state["current"] = SKULSTOS
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'stelflaxl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'stelflaxl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"stelflaxl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skulstos(self, hint):
        assert self._state.get("current") == SKULSTOS, \
            f"glaxglall.skulstos: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skulstos', 2:
                self._state["current"] = TRULSKULR
                self._state["trig"]    = "hint:2"
            case 'skulstos', 0:
                self._state["current"] = SPALGLUR
                self._state["trig"]    = "hint:0"
            case 'skulstos', _:
                self._state["current"] = TRAXKREXT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skulstos', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skulstos',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skulstos->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _traxkrext(self, hint):
        assert self._state.get("current") == TRAXKREXT, \
            f"glaxglall.traxkrext: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'traxkrext', 2:
                self._state["current"] = TRULSKULR
                self._state["trig"]    = "hint:2"
            case 'traxkrext', _:
                self._state["current"] = SPALGLUR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'traxkrext', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'traxkrext',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"traxkrext->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _spalglur(self, hint):
        assert self._state.get("current") == SPALGLUR, \
            f"glaxglall.spalglur: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'spalglur', 2:
                self._state["current"] = TRULSKULR
                self._state["trig"]    = "hint:2"
            case 'spalglur', _:
                self._state["current"] = STEXBRUL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'spalglur', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'spalglur',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"spalglur->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _stexbrul(self, hint):
        assert self._state.get("current") == STEXBRUL, \
            f"glaxglall.stexbrul: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'stexbrul', 2:
                self._state["current"] = TRULSKULR
                self._state["trig"]    = "hint:2"
            case 'stexbrul', _:
                self._state["current"] = VURBLIM
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'stexbrul', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'stexbrul',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"stexbrul->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _vurblim(self, hint):
        assert self._state.get("current") == VURBLIM, \
            f"glaxglall.vurblim: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'vurblim', 2:
                self._state["current"] = TRULSKULR
                self._state["trig"]    = "hint:2"
            case 'vurblim', 0:
                self._state["current"] = SPARSLALL
                self._state["trig"]    = "hint:0"
            case 'vurblim', _:
                self._state["current"] = GLELSTOS
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'vurblim', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'vurblim',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"vurblim->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glelstos(self, hint):
        assert self._state.get("current") == GLELSTOS, \
            f"glaxglall.glelstos: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glelstos', 2:
                self._state["current"] = TRULSKULR
                self._state["trig"]    = "hint:2"
            case 'glelstos', _:
                self._state["current"] = GLARFLURX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glelstos', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glelstos',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glelstos->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glarflurx(self, hint):
        assert self._state.get("current") == GLARFLURX, \
            f"glaxglall.glarflurx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glarflurx', 2:
                self._state["current"] = TRULSKULR
                self._state["trig"]    = "hint:2"
            case 'glarflurx', 1:
                self._state["current"] = SPARSLALL
                self._state["trig"]    = "hint:1"
            case 'glarflurx', _:
                self._state["current"] = FLORBLURX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glarflurx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glarflurx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glarflurx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _florblurx(self, hint):
        assert self._state.get("current") == FLORBLURX, \
            f"glaxglall.florblurx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'florblurx', 2:
                self._state["current"] = TRULSKULR
                self._state["trig"]    = "hint:2"
            case 'florblurx', _:
                self._state["current"] = FLOSVEXFLANX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'florblurx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'florblurx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"florblurx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _flosvexflanx(self, hint):
        assert self._state.get("current") == FLOSVEXFLANX, \
            f"glaxglall.flosvexflanx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'flosvexflanx', 2:
                self._state["current"] = TRULSKULR
                self._state["trig"]    = "hint:2"
            case 'flosvexflanx', _:
                self._state["current"] = BRORSKORN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'flosvexflanx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'flosvexflanx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"flosvexflanx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brorskorn(self, hint):
        assert self._state.get("current") == BRORSKORN, \
            f"glaxglall.brorskorn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brorskorn', 2:
                self._state["current"] = TRULSKULR
                self._state["trig"]    = "hint:2"
            case 'brorskorn', _:
                self._state["current"] = SPURSTARBLART
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brorskorn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brorskorn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brorskorn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _spurstarblart(self, hint):
        assert self._state.get("current") == SPURSTARBLART, \
            f"glaxglall.spurstarblart: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'spurstarblart', 2:
                self._state["current"] = TRULSKULR
                self._state["trig"]    = "hint:2"
            case 'spurstarblart', 0:
                self._state["current"] = SPARSLALL
                self._state["trig"]    = "hint:0"
            case 'spurstarblart', _:
                self._state["current"] = KRALSPURR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'spurstarblart', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'spurstarblart',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"spurstarblart->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _kralspurr(self, hint):
        assert self._state.get("current") == KRALSPURR, \
            f"glaxglall.kralspurr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'kralspurr', 2:
                self._state["current"] = TRULSKULR
                self._state["trig"]    = "hint:2"
            case 'kralspurr', _:
                self._state["current"] = VAXBREX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'kralspurr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'kralspurr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"kralspurr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _vaxbrex(self, hint):
        assert self._state.get("current") == VAXBREX, \
            f"glaxglall.vaxbrex: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'vaxbrex', 2:
                self._state["current"] = TRULSKULR
                self._state["trig"]    = "hint:2"
            case 'vaxbrex', 0:
                self._state["current"] = SPARSLALL
                self._state["trig"]    = "hint:0"
            case 'vaxbrex', _:
                self._state["current"] = FLEXCLULSLEXK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'vaxbrex', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'vaxbrex',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"vaxbrex->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _flexclulslexk(self, hint):
        assert self._state.get("current") == FLEXCLULSLEXK, \
            f"glaxglall.flexclulslexk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'flexclulslexk', 2:
                self._state["current"] = TRULSKULR
                self._state["trig"]    = "hint:2"
            case 'flexclulslexk', _:
                self._state["current"] = GLIMSPONSKONL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'flexclulslexk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'flexclulslexk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"flexclulslexk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glimsponskonl(self, hint):
        assert self._state.get("current") == GLIMSPONSKONL, \
            f"glaxglall.glimsponskonl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glimsponskonl', 2:
                self._state["current"] = TRULSKULR
                self._state["trig"]    = "hint:2"
            case 'glimsponskonl', _:
                self._state["current"] = KREXSKARKRURT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glimsponskonl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glimsponskonl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glimsponskonl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _krexskarkrurt(self, hint):
        assert self._state.get("current") == KREXSKARKRURT, \
            f"glaxglall.krexskarkrurt: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'krexskarkrurt', 2:
                self._state["current"] = TRULSKULR
                self._state["trig"]    = "hint:2"
            case 'krexskarkrurt', 1:
                self._state["current"] = VENBRIXGLANK
                self._state["trig"]    = "hint:1"
            case 'krexskarkrurt', _:
                self._state["current"] = SKAXDRIMSLULL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'krexskarkrurt', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'krexskarkrurt',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"krexskarkrurt->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skaxdrimslull(self, hint):
        assert self._state.get("current") == SKAXDRIMSLULL, \
            f"glaxglall.skaxdrimslull: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skaxdrimslull', 2:
                self._state["current"] = TRULSKULR
                self._state["trig"]    = "hint:2"
            case 'skaxdrimslull', _:
                self._state["current"] = VENBRIXGLANK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skaxdrimslull', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skaxdrimslull',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skaxdrimslull->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _venbrixglank(self, hint):
        assert self._state.get("current") == VENBRIXGLANK, \
            f"glaxglall.venbrixglank: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'venbrixglank', 2:
                self._state["current"] = TRULSKULR
                self._state["trig"]    = "hint:2"
            case 'venbrixglank', _:
                self._state["current"] = BROSSPUR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'venbrixglank', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'venbrixglank',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"venbrixglank->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brosspur(self, hint):
        assert self._state.get("current") == BROSSPUR, \
            f"glaxglall.brosspur: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brosspur', 2:
                self._state["current"] = TRULSKULR
                self._state["trig"]    = "hint:2"
            case 'brosspur', 1:
                self._state["current"] = SPARSLALL
                self._state["trig"]    = "hint:1"
            case 'brosspur', _:
                self._state["current"] = PRURSTULT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brosspur', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brosspur',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brosspur->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _prurstult(self, hint):
        assert self._state.get("current") == PRURSTULT, \
            f"glaxglall.prurstult: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'prurstult', 2:
                self._state["current"] = TRULSKULR
                self._state["trig"]    = "hint:2"
            case 'prurstult', _:
                self._state["current"] = SLARSTARK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'prurstult', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'prurstult',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"prurstult->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slarstark(self, hint):
        assert self._state.get("current") == SLARSTARK, \
            f"glaxglall.slarstark: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slarstark', 2:
                self._state["current"] = TRULSKULR
                self._state["trig"]    = "hint:2"
            case 'slarstark', _:
                self._state["current"] = GRIXBRORTRANX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slarstark', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slarstark',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slarstark->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _grixbrortranx(self, hint):
        assert self._state.get("current") == GRIXBRORTRANX, \
            f"glaxglall.grixbrortranx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'grixbrortranx', 2:
                self._state["current"] = TRULSKULR
                self._state["trig"]    = "hint:2"
            case 'grixbrortranx', 0:
                self._state["current"] = SPARSLALL
                self._state["trig"]    = "hint:0"
            case 'grixbrortranx', _:
                self._state["current"] = STENVENR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'grixbrortranx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'grixbrortranx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"grixbrortranx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _stenvenr(self, hint):
        assert self._state.get("current") == STENVENR, \
            f"glaxglall.stenvenr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'stenvenr', 2:
                self._state["current"] = TRULSKULR
                self._state["trig"]    = "hint:2"
            case 'stenvenr', _:
                self._state["current"] = DRIMSTENSKEX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'stenvenr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'stenvenr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"stenvenr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _drimstenskex(self, hint):
        assert self._state.get("current") == DRIMSTENSKEX, \
            f"glaxglall.drimstenskex: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'drimstenskex', 2:
                self._state["current"] = TRULSKULR
                self._state["trig"]    = "hint:2"
            case 'drimstenskex', 1:
                self._state["current"] = STEXKRAN
                self._state["trig"]    = "hint:1"
            case 'drimstenskex', _:
                self._state["current"] = SLOSSKARL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'drimstenskex', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'drimstenskex',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"drimstenskex->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slosskarl(self, hint):
        assert self._state.get("current") == SLOSSKARL, \
            f"glaxglall.slosskarl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slosskarl', 2:
                self._state["current"] = TRULSKULR
                self._state["trig"]    = "hint:2"
            case 'slosskarl', _:
                self._state["current"] = STEXKRAN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slosskarl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slosskarl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slosskarl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _stexkran(self, hint):
        assert self._state.get("current") == STEXKRAN, \
            f"glaxglall.stexkran: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'stexkran', 2:
                self._state["current"] = TRULSKULR
                self._state["trig"]    = "hint:2"
            case 'stexkran', 0:
                self._state["current"] = PREXGRANL
                self._state["trig"]    = "hint:0"
            case 'stexkran', _:
                self._state["current"] = CLONFLAXN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'stexkran', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'stexkran',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"stexkran->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _clonflaxn(self, hint):
        assert self._state.get("current") == CLONFLAXN, \
            f"glaxglall.clonflaxn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'clonflaxn', 2:
                self._state["current"] = TRULSKULR
                self._state["trig"]    = "hint:2"
            case 'clonflaxn', 1:
                self._state["current"] = GRIMGRAXGRAN
                self._state["trig"]    = "hint:1"
            case 'clonflaxn', _:
                self._state["current"] = PREXGRANL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'clonflaxn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'clonflaxn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"clonflaxn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _prexgranl(self, hint):
        assert self._state.get("current") == PREXGRANL, \
            f"glaxglall.prexgranl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'prexgranl', 2:
                self._state["current"] = TRULSKULR
                self._state["trig"]    = "hint:2"
            case 'prexgranl', 0:
                self._state["current"] = SPARSLALL
                self._state["trig"]    = "hint:0"
            case 'prexgranl', _:
                self._state["current"] = GRIMGRAXGRAN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'prexgranl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'prexgranl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"prexgranl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _grimgraxgran(self, hint):
        assert self._state.get("current") == GRIMGRAXGRAN, \
            f"glaxglall.grimgraxgran: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'grimgraxgran', 2:
                self._state["current"] = TRULSKULR
                self._state["trig"]    = "hint:2"
            case 'grimgraxgran', _:
                self._state["current"] = SLARGLARN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'grimgraxgran', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'grimgraxgran',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"grimgraxgran->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slarglarn(self, hint):
        assert self._state.get("current") == SLARGLARN, \
            f"glaxglall.slarglarn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slarglarn', 2:
                self._state["current"] = TRULSKULR
                self._state["trig"]    = "hint:2"
            case 'slarglarn', _:
                self._state["current"] = PRURFLON
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slarglarn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slarglarn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slarglarn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _prurflon(self, hint):
        assert self._state.get("current") == PRURFLON, \
            f"glaxglall.prurflon: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'prurflon', 2:
                self._state["current"] = TRULSKULR
                self._state["trig"]    = "hint:2"
            case 'prurflon', _:
                self._state["current"] = KROSTREN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'prurflon', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'prurflon',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"prurflon->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _krostren(self, hint):
        assert self._state.get("current") == KROSTREN, \
            f"glaxglall.krostren: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'krostren', 2:
                self._state["current"] = TRULSKULR
                self._state["trig"]    = "hint:2"
            case 'krostren', _:
                self._state["current"] = CLONPRAXKROR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'krostren', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'krostren',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"krostren->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _clonpraxkror(self, hint):
        assert self._state.get("current") == CLONPRAXKROR, \
            f"glaxglall.clonpraxkror: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'clonpraxkror', 2:
                self._state["current"] = TRULSKULR
                self._state["trig"]    = "hint:2"
            case 'clonpraxkror', 0:
                self._state["current"] = SPARSLALL
                self._state["trig"]    = "hint:0"
            case 'clonpraxkror', _:
                self._state["current"] = DRIMTRAXT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'clonpraxkror', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'clonpraxkror',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"clonpraxkror->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _drimtraxt(self, hint):
        assert self._state.get("current") == DRIMTRAXT, \
            f"glaxglall.drimtraxt: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'drimtraxt', 2:
                self._state["current"] = TRULSKULR
                self._state["trig"]    = "hint:2"
            case 'drimtraxt', _:
                self._state["current"] = STANKRIXX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'drimtraxt', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'drimtraxt',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"drimtraxt->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _stankrixx(self, hint):
        assert self._state.get("current") == STANKRIXX, \
            f"glaxglall.stankrixx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'stankrixx', 2:
                self._state["current"] = TRULSKULR
                self._state["trig"]    = "hint:2"
            case 'stankrixx', 1:
                self._state["current"] = VELKROSK
                self._state["trig"]    = "hint:1"
            case 'stankrixx', _:
                self._state["current"] = GLOSSLORTREX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'stankrixx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'stankrixx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"stankrixx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glosslortrex(self, hint):
        assert self._state.get("current") == GLOSSLORTREX, \
            f"glaxglall.glosslortrex: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glosslortrex', 2:
                self._state["current"] = TRULSKULR
                self._state["trig"]    = "hint:2"
            case 'glosslortrex', 1:
                self._state["current"] = GLELBLARSLOR
                self._state["trig"]    = "hint:1"
            case 'glosslortrex', _:
                self._state["current"] = VELKROSK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glosslortrex', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glosslortrex',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glosslortrex->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _velkrosk(self, hint):
        assert self._state.get("current") == VELKROSK, \
            f"glaxglall.velkrosk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'velkrosk', 2:
                self._state["current"] = TRULSKULR
                self._state["trig"]    = "hint:2"
            case 'velkrosk', 0:
                self._state["current"] = DRELPRARGLEN
                self._state["trig"]    = "hint:0"
            case 'velkrosk', _:
                self._state["current"] = GLELBLARSLOR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'velkrosk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'velkrosk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"velkrosk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glelblarslor(self, hint):
        assert self._state.get("current") == GLELBLARSLOR, \
            f"glaxglall.glelblarslor: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glelblarslor', 2:
                self._state["current"] = TRULSKULR
                self._state["trig"]    = "hint:2"
            case 'glelblarslor', _:
                self._state["current"] = DRELPRARGLEN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glelblarslor', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glelblarslor',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glelblarslor->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _drelprarglen(self, hint):
        assert self._state.get("current") == DRELPRARGLEN, \
            f"glaxglall.drelprarglen: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'drelprarglen', 2:
                self._state["current"] = TRULSKULR
                self._state["trig"]    = "hint:2"
            case 'drelprarglen', _:
                self._state["current"] = SKARSTIMFLEX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'drelprarglen', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'drelprarglen',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"drelprarglen->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skarstimflex(self, hint):
        assert self._state.get("current") == SKARSTIMFLEX, \
            f"glaxglall.skarstimflex: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skarstimflex', 2:
                self._state["current"] = TRULSKULR
                self._state["trig"]    = "hint:2"
            case 'skarstimflex', 1:
                self._state["current"] = SPARSLALL
                self._state["trig"]    = "hint:1"
            case 'skarstimflex', _:
                self._state["current"] = PRALGREXKRAL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skarstimflex', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skarstimflex',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skarstimflex->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _pralgrexkral(self, hint):
        assert self._state.get("current") == PRALGREXKRAL, \
            f"glaxglall.pralgrexkral: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'pralgrexkral', 2:
                self._state["current"] = TRULSKULR
                self._state["trig"]    = "hint:2"
            case 'pralgrexkral', _:
                self._state["current"] = GLIMGLIXBLOSR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'pralgrexkral', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'pralgrexkral',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"pralgrexkral->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glimglixblosr(self, hint):
        assert self._state.get("current") == GLIMGLIXBLOSR, \
            f"glaxglall.glimglixblosr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glimglixblosr', 2:
                self._state["current"] = TRULSKULR
                self._state["trig"]    = "hint:2"
            case 'glimglixblosr', 1:
                self._state["current"] = SPARSLALL
                self._state["trig"]    = "hint:1"
            case 'glimglixblosr', _:
                self._state["current"] = GREXSTARCLULN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glimglixblosr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glimglixblosr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glimglixblosr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _grexstarcluln(self, hint):
        assert self._state.get("current") == GREXSTARCLULN, \
            f"glaxglall.grexstarcluln: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'grexstarcluln', 2:
                self._state["current"] = TRULSKULR
                self._state["trig"]    = "hint:2"
            case 'grexstarcluln', 1:
                self._state["current"] = SPARSLALL
                self._state["trig"]    = "hint:1"
            case 'grexstarcluln', _:
                self._state["current"] = GLOSSTELSKOR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'grexstarcluln', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'grexstarcluln',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"grexstarcluln->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glosstelskor(self, hint):
        assert self._state.get("current") == GLOSSTELSKOR, \
            f"glaxglall.glosstelskor: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glosstelskor', 2:
                self._state["current"] = TRULSKULR
                self._state["trig"]    = "hint:2"
            case 'glosstelskor', _:
                self._state["current"] = SLIXBROR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glosstelskor', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glosstelskor',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glosstelskor->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slixbror(self, hint):
        assert self._state.get("current") == SLIXBROR, \
            f"glaxglall.slixbror: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slixbror', 2:
                self._state["current"] = TRULSKULR
                self._state["trig"]    = "hint:2"
            case 'slixbror', _:
                self._state["current"] = TRONTRULSPENX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slixbror', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slixbror',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slixbror->{_to}", _xid_val)
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
            _xid_val = _xid(__name__, 'skixkranflimx', "error", "assert_fail")
            _emit(cycle, 1, __name__, 'skixkranflimx',
                   {"hint": hint, "span": span, "caller": caller},
                   dict(ctx), _conds,
                   "entry_blocked->error", _xid_val, assertion=_asrt)
            return 2, cycle + 1

        self._state = {"current": SKIXKRANFLIMX, "ctx": ctx,
                        "span": span, "caller": caller,
                        "trig": "auto", "cycle": cycle}
        _dispatch = {
            SKIXKRANFLIMX: self._skixkranflimx,
            GLOSTRIXT: self._glostrixt,
            DRIMCLIM: self._drimclim,
            GLARDRELBLOSX: self._glardrelblosx,
            SPORSLORSLIXT: self._sporslorslixt,
            PRAXTRIM: self._praxtrim,
            BRIXBLELSKELR: self._brixblelskelr,
            KRONSLULSKIM: self._kronslulskim,
            FLURSTIX: self._flurstix,
            TRURSLEXGRENN: self._trurslexgrenn,
            SKARSPIXGROR: self._skarspixgror,
            KRURTRIXBLENL: self._krurtrixblenl,
            CLAXSLIXR: self._claxslixr,
            PRIMBLAL: self._primblal,
            CLURVULSPENT: self._clurvulspent,
            TRONBRULDRULX: self._tronbruldrulx,
            GRAXBRORKRIX: self._graxbrorkrix,
            SKANTRENX: self._skantrenx,
            CLORDRIM: self._clordrim,
            STELFLAXL: self._stelflaxl,
            SKULSTOS: self._skulstos,
            TRAXKREXT: self._traxkrext,
            SPALGLUR: self._spalglur,
            STEXBRUL: self._stexbrul,
            VURBLIM: self._vurblim,
            GLELSTOS: self._glelstos,
            GLARFLURX: self._glarflurx,
            FLORBLURX: self._florblurx,
            FLOSVEXFLANX: self._flosvexflanx,
            BRORSKORN: self._brorskorn,
            SPURSTARBLART: self._spurstarblart,
            KRALSPURR: self._kralspurr,
            VAXBREX: self._vaxbrex,
            FLEXCLULSLEXK: self._flexclulslexk,
            GLIMSPONSKONL: self._glimsponskonl,
            KREXSKARKRURT: self._krexskarkrurt,
            SKAXDRIMSLULL: self._skaxdrimslull,
            VENBRIXGLANK: self._venbrixglank,
            BROSSPUR: self._brosspur,
            PRURSTULT: self._prurstult,
            SLARSTARK: self._slarstark,
            GRIXBRORTRANX: self._grixbrortranx,
            STENVENR: self._stenvenr,
            DRIMSTENSKEX: self._drimstenskex,
            SLOSSKARL: self._slosskarl,
            STEXKRAN: self._stexkran,
            CLONFLAXN: self._clonflaxn,
            PREXGRANL: self._prexgranl,
            GRIMGRAXGRAN: self._grimgraxgran,
            SLARGLARN: self._slarglarn,
            PRURFLON: self._prurflon,
            KROSTREN: self._krostren,
            CLONPRAXKROR: self._clonpraxkror,
            DRIMTRAXT: self._drimtraxt,
            STANKRIXX: self._stankrixx,
            GLOSSLORTREX: self._glosslortrex,
            VELKROSK: self._velkrosk,
            GLELBLARSLOR: self._glelblarslor,
            DRELPRARGLEN: self._drelprarglen,
            SKARSTIMFLEX: self._skarstimflex,
            PRALGREXKRAL: self._pralgrexkral,
            GLIMGLIXBLOSR: self._glimglixblosr,
            GREXSTARCLULN: self._grexstarcluln,
            GLOSSTELSKOR: self._glosstelskor,
            SLIXBROR: self._slixbror,
        }
        while self._state["current"] not in _R and self._state["cycle"] - cycle < 8000:
            _dispatch[self._state["current"]](hint)
        _ret     = _R.get(self._state["current"], -1)
        _is_err  = self._state["current"] == TRULSKULR
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
    return GlaxglallFSM().invoke(hint=hint, span=span, caller=caller, ctx=ctx, cycle=cycle)
