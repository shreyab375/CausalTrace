from _log import _w as _emit, _xid

SPURSTANR = 'spurstanr'
SPARBLIX = 'sparblix'
BRULBRELSPIMN = 'brulbrelspimn'
SPALFLOSSKIXX = 'spalflosskixx'
PRENVOR = 'prenvor'
GRELVELTRORL = 'grelveltrorl'
BRONSPEN = 'bronspen'
GLAXGREN = 'glaxgren'
GLULSKEXR = 'glulskexr'
DRONSKAXR = 'dronskaxr'
CLIXSPANK = 'clixspank'
BRONCLIM = 'bronclim'
TRIMSKENSTEX = 'trimskenstex'
SLORSPIMBREX = 'slorspimbrex'
BRURKRIMBLONX = 'brurkrimblonx'
DRANBRAL = 'dranbral'
GLIMTRULL = 'glimtrull'
VALBLONT = 'valblont'
STEXFLENGLANL = 'stexflenglanl'
TRONSPIMVOSL = 'tronspimvosl'
SLALBRARGLAN = 'slalbrarglan'
KRALBROSFLENR = 'kralbrosflenr'
SKEXSTIM = 'skexstim'
FLEXVIXSPALL = 'flexvixspall'
KRAXSKANR = 'kraxskanr'
SPIMTROR = 'spimtror'
CLOSGRONVAXR = 'closgronvaxr'
GRARSKAXL = 'grarskaxl'
DRENGLAN = 'drenglan'
BREXVURN = 'brexvurn'
BLENSLAR = 'blenslar'
GLENKRURSKEL = 'glenkrurskel'
BLONVARN = 'blonvarn'
VAXSLAN = 'vaxslan'
GRARSLANK = 'grarslank'
VIMGLAXPRIXX = 'vimglaxprixx'
STEXGRURBRALX = 'stexgrurbralx'
STELVIM = 'stelvim'
BLEXGREXX = 'blexgrexx'
SPIXKRELSTIM = 'spixkrelstim'
VORVARSLALR = 'vorvarslalr'
DRULTROR = 'drultror'
SPENSTENSKIX = 'spenstenskix'
SLURGLAR = 'slurglar'
SKURSLONR = 'skurslonr'
PRALCLURBRARX = 'pralclurbrarx'
SKIMSTENK = 'skimstenk'
GLOSSLENBRARR = 'glosslenbrarr'
GRARBROSL = 'grarbrosl'
FLELTROS = 'fleltros'
GREXPREL = 'grexprel'
TRIMTRIXSPIXR = 'trimtrixspixr'
DRENBLOSCLIMR = 'drenblosclimr'
FLONBLORPRALK = 'flonblorpralk'
DRIMSPARGREXR = 'drimspargrexr'
STULDRIMN = 'stuldrimn'
GRARPRALVELX = 'grarpralvelx'
GLORPRORL = 'glorprorl'
SPIMBRIXBLAL = 'spimbrixblal'
SPURSLALSTUL = 'spurslalstul'
DRIMVIMFLUL = 'drimvimflul'
VENSLEXVAN = 'venslexvan'
DROSSTOSVIXN = 'drosstosvixn'
PRENCLULTRULX = 'prenclultrulx'
BRORBLEXL = 'brorblexl'
KRAXSKALKRORK = 'kraxskalkrork'
KRONSLAR = 'kronslar'
DRORPRURR = 'drorprurr'

_R = {
    KRAXSKALKRORK: 0,
    KRONSLAR: 1,
    DRORPRURR: 2,
}

_CTX_WRITES_KEY  = 'flurslex'
_CTX_WRITE_STATE = CLIXSPANK

class SkalsposxFSM:
    def __init__(self):
        self._state = {}

    def _spurstanr(self, hint):
        assert self._state.get("current") == SPURSTANR, \
            f"skalsposx.spurstanr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'spurstanr', 2:
                self._state["current"] = DRORPRURR
                self._state["trig"]    = "hint:2"
            case 'spurstanr', _:
                self._state["current"] = SPARBLIX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'spurstanr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'spurstanr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"spurstanr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _sparblix(self, hint):
        assert self._state.get("current") == SPARBLIX, \
            f"skalsposx.sparblix: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'sparblix', 2:
                self._state["current"] = DRORPRURR
                self._state["trig"]    = "hint:2"
            case 'sparblix', _:
                self._state["current"] = BRULBRELSPIMN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'sparblix', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'sparblix',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"sparblix->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brulbrelspimn(self, hint):
        assert self._state.get("current") == BRULBRELSPIMN, \
            f"skalsposx.brulbrelspimn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brulbrelspimn', 2:
                self._state["current"] = DRORPRURR
                self._state["trig"]    = "hint:2"
            case 'brulbrelspimn', _:
                self._state["current"] = SPALFLOSSKIXX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brulbrelspimn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brulbrelspimn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brulbrelspimn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _spalflosskixx(self, hint):
        assert self._state.get("current") == SPALFLOSSKIXX, \
            f"skalsposx.spalflosskixx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'spalflosskixx', 2:
                self._state["current"] = DRORPRURR
                self._state["trig"]    = "hint:2"
            case 'spalflosskixx', _:
                self._state["current"] = PRENVOR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'spalflosskixx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'spalflosskixx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"spalflosskixx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _prenvor(self, hint):
        assert self._state.get("current") == PRENVOR, \
            f"skalsposx.prenvor: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'prenvor', 2:
                self._state["current"] = DRORPRURR
                self._state["trig"]    = "hint:2"
            case 'prenvor', 1:
                self._state["current"] = KRONSLAR
                self._state["trig"]    = "hint:1"
            case 'prenvor', _:
                self._state["current"] = GRELVELTRORL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'prenvor', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'prenvor',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"prenvor->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _grelveltrorl(self, hint):
        assert self._state.get("current") == GRELVELTRORL, \
            f"skalsposx.grelveltrorl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'grelveltrorl', 2:
                self._state["current"] = DRORPRURR
                self._state["trig"]    = "hint:2"
            case 'grelveltrorl', 0:
                self._state["current"] = GLAXGREN
                self._state["trig"]    = "hint:0"
            case 'grelveltrorl', _:
                self._state["current"] = BRONSPEN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'grelveltrorl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'grelveltrorl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"grelveltrorl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _bronspen(self, hint):
        assert self._state.get("current") == BRONSPEN, \
            f"skalsposx.bronspen: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'bronspen', 2:
                self._state["current"] = DRORPRURR
                self._state["trig"]    = "hint:2"
            case 'bronspen', 0:
                self._state["current"] = KRONSLAR
                self._state["trig"]    = "hint:0"
            case 'bronspen', _:
                self._state["current"] = GLAXGREN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'bronspen', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'bronspen',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"bronspen->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glaxgren(self, hint):
        assert self._state.get("current") == GLAXGREN, \
            f"skalsposx.glaxgren: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glaxgren', 2:
                self._state["current"] = DRORPRURR
                self._state["trig"]    = "hint:2"
            case 'glaxgren', _:
                self._state["current"] = GLULSKEXR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glaxgren', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glaxgren',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glaxgren->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glulskexr(self, hint):
        assert self._state.get("current") == GLULSKEXR, \
            f"skalsposx.glulskexr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glulskexr', 2:
                self._state["current"] = DRORPRURR
                self._state["trig"]    = "hint:2"
            case 'glulskexr', 1:
                self._state["current"] = KRONSLAR
                self._state["trig"]    = "hint:1"
            case 'glulskexr', _:
                self._state["current"] = DRONSKAXR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glulskexr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glulskexr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glulskexr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _dronskaxr(self, hint):
        assert self._state.get("current") == DRONSKAXR, \
            f"skalsposx.dronskaxr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'dronskaxr', 2:
                self._state["current"] = DRORPRURR
                self._state["trig"]    = "hint:2"
            case 'dronskaxr', _:
                self._state["current"] = CLIXSPANK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'dronskaxr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'dronskaxr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"dronskaxr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _clixspank(self, hint):
        assert self._state.get("current") == CLIXSPANK, \
            f"skalsposx.clixspank: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        _ctx_val_before = self._state["ctx"].get(_CTX_WRITES_KEY, 0)
        match self._state["current"], hint:
            case 'clixspank', 2:
                self._state["current"] = DRORPRURR
                self._state["trig"]    = "hint:2"
            case 'clixspank', _:
                self._state["current"] = BRONCLIM
                self._state["trig"]    = "auto"
        _old = self._state["ctx"].get(_CTX_WRITES_KEY, 0)
        _inc = 2 if hint == 2 else 1
        self._state["ctx"][_CTX_WRITES_KEY] = _old + _inc
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'clixspank', _to, _trig)
        _conds = {"hint_branch": _hint_branch,
                   "ctx_write": True,
                   "ctx_val_before": _ctx_val_before}
        _emit(self._state["cycle"], 1, __name__, 'clixspank',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"clixspank->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _bronclim(self, hint):
        assert self._state.get("current") == BRONCLIM, \
            f"skalsposx.bronclim: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'bronclim', 2:
                self._state["current"] = DRORPRURR
                self._state["trig"]    = "hint:2"
            case 'bronclim', 0:
                self._state["current"] = KRONSLAR
                self._state["trig"]    = "hint:0"
            case 'bronclim', _:
                self._state["current"] = TRIMSKENSTEX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'bronclim', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'bronclim',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"bronclim->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _trimskenstex(self, hint):
        assert self._state.get("current") == TRIMSKENSTEX, \
            f"skalsposx.trimskenstex: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'trimskenstex', 2:
                self._state["current"] = DRORPRURR
                self._state["trig"]    = "hint:2"
            case 'trimskenstex', _:
                self._state["current"] = SLORSPIMBREX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'trimskenstex', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'trimskenstex',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"trimskenstex->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slorspimbrex(self, hint):
        assert self._state.get("current") == SLORSPIMBREX, \
            f"skalsposx.slorspimbrex: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slorspimbrex', 2:
                self._state["current"] = DRORPRURR
                self._state["trig"]    = "hint:2"
            case 'slorspimbrex', 1:
                self._state["current"] = DRANBRAL
                self._state["trig"]    = "hint:1"
            case 'slorspimbrex', _:
                self._state["current"] = BRURKRIMBLONX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slorspimbrex', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slorspimbrex',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slorspimbrex->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brurkrimblonx(self, hint):
        assert self._state.get("current") == BRURKRIMBLONX, \
            f"skalsposx.brurkrimblonx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brurkrimblonx', 2:
                self._state["current"] = DRORPRURR
                self._state["trig"]    = "hint:2"
            case 'brurkrimblonx', 1:
                self._state["current"] = KRONSLAR
                self._state["trig"]    = "hint:1"
            case 'brurkrimblonx', _:
                self._state["current"] = DRANBRAL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brurkrimblonx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brurkrimblonx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brurkrimblonx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _dranbral(self, hint):
        assert self._state.get("current") == DRANBRAL, \
            f"skalsposx.dranbral: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'dranbral', 2:
                self._state["current"] = DRORPRURR
                self._state["trig"]    = "hint:2"
            case 'dranbral', _:
                self._state["current"] = GLIMTRULL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'dranbral', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'dranbral',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"dranbral->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glimtrull(self, hint):
        assert self._state.get("current") == GLIMTRULL, \
            f"skalsposx.glimtrull: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glimtrull', 2:
                self._state["current"] = DRORPRURR
                self._state["trig"]    = "hint:2"
            case 'glimtrull', _:
                self._state["current"] = VALBLONT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glimtrull', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glimtrull',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glimtrull->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _valblont(self, hint):
        assert self._state.get("current") == VALBLONT, \
            f"skalsposx.valblont: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'valblont', 2:
                self._state["current"] = DRORPRURR
                self._state["trig"]    = "hint:2"
            case 'valblont', _:
                self._state["current"] = STEXFLENGLANL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'valblont', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'valblont',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"valblont->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _stexflenglanl(self, hint):
        assert self._state.get("current") == STEXFLENGLANL, \
            f"skalsposx.stexflenglanl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'stexflenglanl', 2:
                self._state["current"] = DRORPRURR
                self._state["trig"]    = "hint:2"
            case 'stexflenglanl', 0:
                self._state["current"] = KRONSLAR
                self._state["trig"]    = "hint:0"
            case 'stexflenglanl', _:
                self._state["current"] = TRONSPIMVOSL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'stexflenglanl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'stexflenglanl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"stexflenglanl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _tronspimvosl(self, hint):
        assert self._state.get("current") == TRONSPIMVOSL, \
            f"skalsposx.tronspimvosl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'tronspimvosl', 2:
                self._state["current"] = DRORPRURR
                self._state["trig"]    = "hint:2"
            case 'tronspimvosl', _:
                self._state["current"] = SLALBRARGLAN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'tronspimvosl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'tronspimvosl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"tronspimvosl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slalbrarglan(self, hint):
        assert self._state.get("current") == SLALBRARGLAN, \
            f"skalsposx.slalbrarglan: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slalbrarglan', 2:
                self._state["current"] = DRORPRURR
                self._state["trig"]    = "hint:2"
            case 'slalbrarglan', _:
                self._state["current"] = KRALBROSFLENR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slalbrarglan', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slalbrarglan',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slalbrarglan->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _kralbrosflenr(self, hint):
        assert self._state.get("current") == KRALBROSFLENR, \
            f"skalsposx.kralbrosflenr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'kralbrosflenr', 2:
                self._state["current"] = DRORPRURR
                self._state["trig"]    = "hint:2"
            case 'kralbrosflenr', _:
                self._state["current"] = SKEXSTIM
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'kralbrosflenr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'kralbrosflenr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"kralbrosflenr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skexstim(self, hint):
        assert self._state.get("current") == SKEXSTIM, \
            f"skalsposx.skexstim: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skexstim', 2:
                self._state["current"] = DRORPRURR
                self._state["trig"]    = "hint:2"
            case 'skexstim', 1:
                self._state["current"] = KRONSLAR
                self._state["trig"]    = "hint:1"
            case 'skexstim', _:
                self._state["current"] = FLEXVIXSPALL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skexstim', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skexstim',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skexstim->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _flexvixspall(self, hint):
        assert self._state.get("current") == FLEXVIXSPALL, \
            f"skalsposx.flexvixspall: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'flexvixspall', 2:
                self._state["current"] = DRORPRURR
                self._state["trig"]    = "hint:2"
            case 'flexvixspall', _:
                self._state["current"] = KRAXSKANR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'flexvixspall', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'flexvixspall',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"flexvixspall->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _kraxskanr(self, hint):
        assert self._state.get("current") == KRAXSKANR, \
            f"skalsposx.kraxskanr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'kraxskanr', 2:
                self._state["current"] = DRORPRURR
                self._state["trig"]    = "hint:2"
            case 'kraxskanr', 1:
                self._state["current"] = KRONSLAR
                self._state["trig"]    = "hint:1"
            case 'kraxskanr', _:
                self._state["current"] = SPIMTROR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'kraxskanr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'kraxskanr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"kraxskanr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _spimtror(self, hint):
        assert self._state.get("current") == SPIMTROR, \
            f"skalsposx.spimtror: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'spimtror', 2:
                self._state["current"] = DRORPRURR
                self._state["trig"]    = "hint:2"
            case 'spimtror', 0:
                self._state["current"] = KRONSLAR
                self._state["trig"]    = "hint:0"
            case 'spimtror', _:
                self._state["current"] = CLOSGRONVAXR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'spimtror', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'spimtror',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"spimtror->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _closgronvaxr(self, hint):
        assert self._state.get("current") == CLOSGRONVAXR, \
            f"skalsposx.closgronvaxr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'closgronvaxr', 2:
                self._state["current"] = DRORPRURR
                self._state["trig"]    = "hint:2"
            case 'closgronvaxr', _:
                self._state["current"] = GRARSKAXL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'closgronvaxr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'closgronvaxr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"closgronvaxr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _grarskaxl(self, hint):
        assert self._state.get("current") == GRARSKAXL, \
            f"skalsposx.grarskaxl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'grarskaxl', 2:
                self._state["current"] = DRORPRURR
                self._state["trig"]    = "hint:2"
            case 'grarskaxl', _:
                self._state["current"] = DRENGLAN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'grarskaxl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'grarskaxl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"grarskaxl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _drenglan(self, hint):
        assert self._state.get("current") == DRENGLAN, \
            f"skalsposx.drenglan: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'drenglan', 2:
                self._state["current"] = DRORPRURR
                self._state["trig"]    = "hint:2"
            case 'drenglan', 1:
                self._state["current"] = BLENSLAR
                self._state["trig"]    = "hint:1"
            case 'drenglan', _:
                self._state["current"] = BREXVURN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'drenglan', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'drenglan',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"drenglan->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brexvurn(self, hint):
        assert self._state.get("current") == BREXVURN, \
            f"skalsposx.brexvurn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brexvurn', 2:
                self._state["current"] = DRORPRURR
                self._state["trig"]    = "hint:2"
            case 'brexvurn', _:
                self._state["current"] = BLENSLAR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brexvurn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brexvurn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brexvurn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blenslar(self, hint):
        assert self._state.get("current") == BLENSLAR, \
            f"skalsposx.blenslar: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blenslar', 2:
                self._state["current"] = DRORPRURR
                self._state["trig"]    = "hint:2"
            case 'blenslar', _:
                self._state["current"] = GLENKRURSKEL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blenslar', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blenslar',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blenslar->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glenkrurskel(self, hint):
        assert self._state.get("current") == GLENKRURSKEL, \
            f"skalsposx.glenkrurskel: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glenkrurskel', 2:
                self._state["current"] = DRORPRURR
                self._state["trig"]    = "hint:2"
            case 'glenkrurskel', 0:
                self._state["current"] = KRONSLAR
                self._state["trig"]    = "hint:0"
            case 'glenkrurskel', _:
                self._state["current"] = BLONVARN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glenkrurskel', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glenkrurskel',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glenkrurskel->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blonvarn(self, hint):
        assert self._state.get("current") == BLONVARN, \
            f"skalsposx.blonvarn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blonvarn', 2:
                self._state["current"] = DRORPRURR
                self._state["trig"]    = "hint:2"
            case 'blonvarn', 0:
                self._state["current"] = GRARSLANK
                self._state["trig"]    = "hint:0"
            case 'blonvarn', _:
                self._state["current"] = VAXSLAN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blonvarn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blonvarn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blonvarn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _vaxslan(self, hint):
        assert self._state.get("current") == VAXSLAN, \
            f"skalsposx.vaxslan: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'vaxslan', 2:
                self._state["current"] = DRORPRURR
                self._state["trig"]    = "hint:2"
            case 'vaxslan', _:
                self._state["current"] = GRARSLANK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'vaxslan', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'vaxslan',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"vaxslan->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _grarslank(self, hint):
        assert self._state.get("current") == GRARSLANK, \
            f"skalsposx.grarslank: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'grarslank', 2:
                self._state["current"] = DRORPRURR
                self._state["trig"]    = "hint:2"
            case 'grarslank', 0:
                self._state["current"] = KRONSLAR
                self._state["trig"]    = "hint:0"
            case 'grarslank', _:
                self._state["current"] = VIMGLAXPRIXX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'grarslank', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'grarslank',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"grarslank->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _vimglaxprixx(self, hint):
        assert self._state.get("current") == VIMGLAXPRIXX, \
            f"skalsposx.vimglaxprixx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'vimglaxprixx', 2:
                self._state["current"] = DRORPRURR
                self._state["trig"]    = "hint:2"
            case 'vimglaxprixx', 1:
                self._state["current"] = STELVIM
                self._state["trig"]    = "hint:1"
            case 'vimglaxprixx', _:
                self._state["current"] = STEXGRURBRALX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'vimglaxprixx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'vimglaxprixx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"vimglaxprixx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _stexgrurbralx(self, hint):
        assert self._state.get("current") == STEXGRURBRALX, \
            f"skalsposx.stexgrurbralx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'stexgrurbralx', 2:
                self._state["current"] = DRORPRURR
                self._state["trig"]    = "hint:2"
            case 'stexgrurbralx', _:
                self._state["current"] = STELVIM
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'stexgrurbralx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'stexgrurbralx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"stexgrurbralx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _stelvim(self, hint):
        assert self._state.get("current") == STELVIM, \
            f"skalsposx.stelvim: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'stelvim', 2:
                self._state["current"] = DRORPRURR
                self._state["trig"]    = "hint:2"
            case 'stelvim', _:
                self._state["current"] = BLEXGREXX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'stelvim', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'stelvim',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"stelvim->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blexgrexx(self, hint):
        assert self._state.get("current") == BLEXGREXX, \
            f"skalsposx.blexgrexx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blexgrexx', 2:
                self._state["current"] = DRORPRURR
                self._state["trig"]    = "hint:2"
            case 'blexgrexx', _:
                self._state["current"] = SPIXKRELSTIM
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blexgrexx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blexgrexx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blexgrexx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _spixkrelstim(self, hint):
        assert self._state.get("current") == SPIXKRELSTIM, \
            f"skalsposx.spixkrelstim: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'spixkrelstim', 2:
                self._state["current"] = DRORPRURR
                self._state["trig"]    = "hint:2"
            case 'spixkrelstim', _:
                self._state["current"] = VORVARSLALR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'spixkrelstim', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'spixkrelstim',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"spixkrelstim->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _vorvarslalr(self, hint):
        assert self._state.get("current") == VORVARSLALR, \
            f"skalsposx.vorvarslalr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'vorvarslalr', 2:
                self._state["current"] = DRORPRURR
                self._state["trig"]    = "hint:2"
            case 'vorvarslalr', _:
                self._state["current"] = DRULTROR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'vorvarslalr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'vorvarslalr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"vorvarslalr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _drultror(self, hint):
        assert self._state.get("current") == DRULTROR, \
            f"skalsposx.drultror: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'drultror', 2:
                self._state["current"] = DRORPRURR
                self._state["trig"]    = "hint:2"
            case 'drultror', 0:
                self._state["current"] = KRONSLAR
                self._state["trig"]    = "hint:0"
            case 'drultror', _:
                self._state["current"] = SPENSTENSKIX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'drultror', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'drultror',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"drultror->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _spenstenskix(self, hint):
        assert self._state.get("current") == SPENSTENSKIX, \
            f"skalsposx.spenstenskix: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'spenstenskix', 2:
                self._state["current"] = DRORPRURR
                self._state["trig"]    = "hint:2"
            case 'spenstenskix', _:
                self._state["current"] = SLURGLAR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'spenstenskix', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'spenstenskix',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"spenstenskix->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slurglar(self, hint):
        assert self._state.get("current") == SLURGLAR, \
            f"skalsposx.slurglar: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slurglar', 2:
                self._state["current"] = DRORPRURR
                self._state["trig"]    = "hint:2"
            case 'slurglar', 0:
                self._state["current"] = PRALCLURBRARX
                self._state["trig"]    = "hint:0"
            case 'slurglar', _:
                self._state["current"] = SKURSLONR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slurglar', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slurglar',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slurglar->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skurslonr(self, hint):
        assert self._state.get("current") == SKURSLONR, \
            f"skalsposx.skurslonr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skurslonr', 2:
                self._state["current"] = DRORPRURR
                self._state["trig"]    = "hint:2"
            case 'skurslonr', 0:
                self._state["current"] = SKIMSTENK
                self._state["trig"]    = "hint:0"
            case 'skurslonr', _:
                self._state["current"] = PRALCLURBRARX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skurslonr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skurslonr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skurslonr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _pralclurbrarx(self, hint):
        assert self._state.get("current") == PRALCLURBRARX, \
            f"skalsposx.pralclurbrarx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'pralclurbrarx', 2:
                self._state["current"] = DRORPRURR
                self._state["trig"]    = "hint:2"
            case 'pralclurbrarx', _:
                self._state["current"] = SKIMSTENK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'pralclurbrarx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'pralclurbrarx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"pralclurbrarx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skimstenk(self, hint):
        assert self._state.get("current") == SKIMSTENK, \
            f"skalsposx.skimstenk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skimstenk', 2:
                self._state["current"] = DRORPRURR
                self._state["trig"]    = "hint:2"
            case 'skimstenk', _:
                self._state["current"] = GLOSSLENBRARR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skimstenk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skimstenk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skimstenk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glosslenbrarr(self, hint):
        assert self._state.get("current") == GLOSSLENBRARR, \
            f"skalsposx.glosslenbrarr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glosslenbrarr', 2:
                self._state["current"] = DRORPRURR
                self._state["trig"]    = "hint:2"
            case 'glosslenbrarr', _:
                self._state["current"] = GRARBROSL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glosslenbrarr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glosslenbrarr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glosslenbrarr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _grarbrosl(self, hint):
        assert self._state.get("current") == GRARBROSL, \
            f"skalsposx.grarbrosl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'grarbrosl', 2:
                self._state["current"] = DRORPRURR
                self._state["trig"]    = "hint:2"
            case 'grarbrosl', _:
                self._state["current"] = FLELTROS
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'grarbrosl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'grarbrosl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"grarbrosl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _fleltros(self, hint):
        assert self._state.get("current") == FLELTROS, \
            f"skalsposx.fleltros: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'fleltros', 2:
                self._state["current"] = DRORPRURR
                self._state["trig"]    = "hint:2"
            case 'fleltros', 1:
                self._state["current"] = TRIMTRIXSPIXR
                self._state["trig"]    = "hint:1"
            case 'fleltros', _:
                self._state["current"] = GREXPREL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'fleltros', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'fleltros',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"fleltros->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _grexprel(self, hint):
        assert self._state.get("current") == GREXPREL, \
            f"skalsposx.grexprel: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'grexprel', 2:
                self._state["current"] = DRORPRURR
                self._state["trig"]    = "hint:2"
            case 'grexprel', _:
                self._state["current"] = TRIMTRIXSPIXR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'grexprel', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'grexprel',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"grexprel->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _trimtrixspixr(self, hint):
        assert self._state.get("current") == TRIMTRIXSPIXR, \
            f"skalsposx.trimtrixspixr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'trimtrixspixr', 2:
                self._state["current"] = DRORPRURR
                self._state["trig"]    = "hint:2"
            case 'trimtrixspixr', _:
                self._state["current"] = DRENBLOSCLIMR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'trimtrixspixr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'trimtrixspixr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"trimtrixspixr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _drenblosclimr(self, hint):
        assert self._state.get("current") == DRENBLOSCLIMR, \
            f"skalsposx.drenblosclimr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'drenblosclimr', 2:
                self._state["current"] = DRORPRURR
                self._state["trig"]    = "hint:2"
            case 'drenblosclimr', 1:
                self._state["current"] = DRIMSPARGREXR
                self._state["trig"]    = "hint:1"
            case 'drenblosclimr', _:
                self._state["current"] = FLONBLORPRALK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'drenblosclimr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'drenblosclimr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"drenblosclimr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _flonblorpralk(self, hint):
        assert self._state.get("current") == FLONBLORPRALK, \
            f"skalsposx.flonblorpralk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'flonblorpralk', 2:
                self._state["current"] = DRORPRURR
                self._state["trig"]    = "hint:2"
            case 'flonblorpralk', _:
                self._state["current"] = DRIMSPARGREXR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'flonblorpralk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'flonblorpralk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"flonblorpralk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _drimspargrexr(self, hint):
        assert self._state.get("current") == DRIMSPARGREXR, \
            f"skalsposx.drimspargrexr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'drimspargrexr', 2:
                self._state["current"] = DRORPRURR
                self._state["trig"]    = "hint:2"
            case 'drimspargrexr', _:
                self._state["current"] = STULDRIMN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'drimspargrexr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'drimspargrexr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"drimspargrexr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _stuldrimn(self, hint):
        assert self._state.get("current") == STULDRIMN, \
            f"skalsposx.stuldrimn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'stuldrimn', 2:
                self._state["current"] = DRORPRURR
                self._state["trig"]    = "hint:2"
            case 'stuldrimn', 0:
                self._state["current"] = KRONSLAR
                self._state["trig"]    = "hint:0"
            case 'stuldrimn', _:
                self._state["current"] = GRARPRALVELX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'stuldrimn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'stuldrimn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"stuldrimn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _grarpralvelx(self, hint):
        assert self._state.get("current") == GRARPRALVELX, \
            f"skalsposx.grarpralvelx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'grarpralvelx', 2:
                self._state["current"] = DRORPRURR
                self._state["trig"]    = "hint:2"
            case 'grarpralvelx', 1:
                self._state["current"] = KRONSLAR
                self._state["trig"]    = "hint:1"
            case 'grarpralvelx', _:
                self._state["current"] = GLORPRORL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'grarpralvelx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'grarpralvelx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"grarpralvelx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glorprorl(self, hint):
        assert self._state.get("current") == GLORPRORL, \
            f"skalsposx.glorprorl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glorprorl', 2:
                self._state["current"] = DRORPRURR
                self._state["trig"]    = "hint:2"
            case 'glorprorl', _:
                self._state["current"] = SPIMBRIXBLAL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glorprorl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glorprorl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glorprorl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _spimbrixblal(self, hint):
        assert self._state.get("current") == SPIMBRIXBLAL, \
            f"skalsposx.spimbrixblal: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'spimbrixblal', 2:
                self._state["current"] = DRORPRURR
                self._state["trig"]    = "hint:2"
            case 'spimbrixblal', _:
                self._state["current"] = SPURSLALSTUL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'spimbrixblal', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'spimbrixblal',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"spimbrixblal->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _spurslalstul(self, hint):
        assert self._state.get("current") == SPURSLALSTUL, \
            f"skalsposx.spurslalstul: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'spurslalstul', 2:
                self._state["current"] = DRORPRURR
                self._state["trig"]    = "hint:2"
            case 'spurslalstul', _:
                self._state["current"] = DRIMVIMFLUL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'spurslalstul', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'spurslalstul',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"spurslalstul->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _drimvimflul(self, hint):
        assert self._state.get("current") == DRIMVIMFLUL, \
            f"skalsposx.drimvimflul: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'drimvimflul', 2:
                self._state["current"] = DRORPRURR
                self._state["trig"]    = "hint:2"
            case 'drimvimflul', 1:
                self._state["current"] = KRONSLAR
                self._state["trig"]    = "hint:1"
            case 'drimvimflul', _:
                self._state["current"] = VENSLEXVAN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'drimvimflul', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'drimvimflul',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"drimvimflul->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _venslexvan(self, hint):
        assert self._state.get("current") == VENSLEXVAN, \
            f"skalsposx.venslexvan: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'venslexvan', 2:
                self._state["current"] = DRORPRURR
                self._state["trig"]    = "hint:2"
            case 'venslexvan', 1:
                self._state["current"] = PRENCLULTRULX
                self._state["trig"]    = "hint:1"
            case 'venslexvan', _:
                self._state["current"] = DROSSTOSVIXN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'venslexvan', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'venslexvan',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"venslexvan->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _drosstosvixn(self, hint):
        assert self._state.get("current") == DROSSTOSVIXN, \
            f"skalsposx.drosstosvixn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'drosstosvixn', 2:
                self._state["current"] = DRORPRURR
                self._state["trig"]    = "hint:2"
            case 'drosstosvixn', 1:
                self._state["current"] = KRONSLAR
                self._state["trig"]    = "hint:1"
            case 'drosstosvixn', _:
                self._state["current"] = PRENCLULTRULX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'drosstosvixn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'drosstosvixn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"drosstosvixn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _prenclultrulx(self, hint):
        assert self._state.get("current") == PRENCLULTRULX, \
            f"skalsposx.prenclultrulx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'prenclultrulx', 2:
                self._state["current"] = DRORPRURR
                self._state["trig"]    = "hint:2"
            case 'prenclultrulx', _:
                self._state["current"] = BRORBLEXL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'prenclultrulx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'prenclultrulx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"prenclultrulx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brorblexl(self, hint):
        assert self._state.get("current") == BRORBLEXL, \
            f"skalsposx.brorblexl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brorblexl', 2:
                self._state["current"] = DRORPRURR
                self._state["trig"]    = "hint:2"
            case 'brorblexl', _:
                self._state["current"] = KRAXSKALKRORK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brorblexl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brorblexl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brorblexl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def invoke(self, hint=None, span=None, caller=None, ctx=None, cycle=0):
        if ctx is None: ctx = {}

        self._state = {"current": SPURSTANR, "ctx": ctx,
                        "span": span, "caller": caller,
                        "trig": "auto", "cycle": cycle}
        _dispatch = {
            SPURSTANR: self._spurstanr,
            SPARBLIX: self._sparblix,
            BRULBRELSPIMN: self._brulbrelspimn,
            SPALFLOSSKIXX: self._spalflosskixx,
            PRENVOR: self._prenvor,
            GRELVELTRORL: self._grelveltrorl,
            BRONSPEN: self._bronspen,
            GLAXGREN: self._glaxgren,
            GLULSKEXR: self._glulskexr,
            DRONSKAXR: self._dronskaxr,
            CLIXSPANK: self._clixspank,
            BRONCLIM: self._bronclim,
            TRIMSKENSTEX: self._trimskenstex,
            SLORSPIMBREX: self._slorspimbrex,
            BRURKRIMBLONX: self._brurkrimblonx,
            DRANBRAL: self._dranbral,
            GLIMTRULL: self._glimtrull,
            VALBLONT: self._valblont,
            STEXFLENGLANL: self._stexflenglanl,
            TRONSPIMVOSL: self._tronspimvosl,
            SLALBRARGLAN: self._slalbrarglan,
            KRALBROSFLENR: self._kralbrosflenr,
            SKEXSTIM: self._skexstim,
            FLEXVIXSPALL: self._flexvixspall,
            KRAXSKANR: self._kraxskanr,
            SPIMTROR: self._spimtror,
            CLOSGRONVAXR: self._closgronvaxr,
            GRARSKAXL: self._grarskaxl,
            DRENGLAN: self._drenglan,
            BREXVURN: self._brexvurn,
            BLENSLAR: self._blenslar,
            GLENKRURSKEL: self._glenkrurskel,
            BLONVARN: self._blonvarn,
            VAXSLAN: self._vaxslan,
            GRARSLANK: self._grarslank,
            VIMGLAXPRIXX: self._vimglaxprixx,
            STEXGRURBRALX: self._stexgrurbralx,
            STELVIM: self._stelvim,
            BLEXGREXX: self._blexgrexx,
            SPIXKRELSTIM: self._spixkrelstim,
            VORVARSLALR: self._vorvarslalr,
            DRULTROR: self._drultror,
            SPENSTENSKIX: self._spenstenskix,
            SLURGLAR: self._slurglar,
            SKURSLONR: self._skurslonr,
            PRALCLURBRARX: self._pralclurbrarx,
            SKIMSTENK: self._skimstenk,
            GLOSSLENBRARR: self._glosslenbrarr,
            GRARBROSL: self._grarbrosl,
            FLELTROS: self._fleltros,
            GREXPREL: self._grexprel,
            TRIMTRIXSPIXR: self._trimtrixspixr,
            DRENBLOSCLIMR: self._drenblosclimr,
            FLONBLORPRALK: self._flonblorpralk,
            DRIMSPARGREXR: self._drimspargrexr,
            STULDRIMN: self._stuldrimn,
            GRARPRALVELX: self._grarpralvelx,
            GLORPRORL: self._glorprorl,
            SPIMBRIXBLAL: self._spimbrixblal,
            SPURSLALSTUL: self._spurslalstul,
            DRIMVIMFLUL: self._drimvimflul,
            VENSLEXVAN: self._venslexvan,
            DROSSTOSVIXN: self._drosstosvixn,
            PRENCLULTRULX: self._prenclultrulx,
            BRORBLEXL: self._brorblexl,
        }
        while self._state["current"] not in _R and self._state["cycle"] - cycle < 8000:
            _dispatch[self._state["current"]](hint)
        _ret     = _R.get(self._state["current"], -1)
        _is_err  = self._state["current"] == DRORPRURR
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
    return SkalsposxFSM().invoke(hint=hint, span=span, caller=caller, ctx=ctx, cycle=cycle)
