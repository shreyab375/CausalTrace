from _log import _w as _emit, _xid

GLEXSTOR = 'glexstor'
CLANSLAR = 'clanslar'
DRURSPIM = 'drurspim'
SKEXVEXK = 'skexvexk'
SKIXSLENL = 'skixslenl'
GLEXBRONSKELL = 'glexbronskell'
SKORDROSBLAR = 'skordrosblar'
BLOSGLARN = 'blosglarn'
DRAXGRON = 'draxgron'
PRALBLORGLURX = 'pralblorglurx'
GLULTRUL = 'glultrul'
VARKRURVON = 'varkrurvon'
DRENGRUL = 'drengrul'
TRANTRURK = 'trantrurk'
SLIMVAL = 'slimval'
TRULSLALCLEX = 'trulslalclex'
SLENVOSSTEX = 'slenvosstex'
CLULBRALN = 'clulbraln'
CLENSLURGLALX = 'clenslurglalx'
DRANFLENTRON = 'dranflentron'
FLEXSTIXN = 'flexstixn'
FLENGLALKRANN = 'flenglalkrann'
BLOSGLAXCLUL = 'blosglaxclul'
CLANSKENN = 'clanskenn'
DRANGLALDRARK = 'dranglaldrark'
BRENBLUR = 'brenblur'
GRAXSTAL = 'graxstal'
CLULFLONL = 'clulflonl'
SKURGRARK = 'skurgrark'
SKULDRELVUL = 'skuldrelvul'
BLARDRENPREXN = 'blardrenprexn'
SKAXSPARPRUL = 'skaxsparprul'
CLULSKORKREXK = 'clulskorkrexk'
KRONFLOSFLEL = 'kronflosflel'
BRANCLORFLEN = 'branclorflen'
SPOSTRELN = 'spostreln'
VEXKRELGRAX = 'vexkrelgrax'
STARVURKROR = 'starvurkror'
VAXSLAXBLOR = 'vaxslaxblor'
VELFLENDROSR = 'velflendrosr'
SPARSLENGLULK = 'sparslenglulk'
GLORFLALR = 'glorflalr'
KROSCLENDRUR = 'krosclendrur'
TRIXSLULGREXK = 'trixslulgrexk'
CLAXPRELSKOR = 'claxprelskor'
FLALDRALFLELN = 'flaldralfleln'
SPEXBLURT = 'spexblurt'
PREXKRANX = 'prexkranx'
SKONSKIMN = 'skonskimn'
TRIMVARSKANX = 'trimvarskanx'
VOSFLENTRAXT = 'vosflentraxt'
STORKRAX = 'storkrax'
STULPRORL = 'stulprorl'
VONVAXL = 'vonvaxl'
TRENSTUL = 'trenstul'
VIXBLUR = 'vixblur'
BREXGLEXT = 'brexglext'
VENBREXTRELR = 'venbrextrelr'
SLANSTEX = 'slanstex'
BLURFLAL = 'blurflal'
SPULBRELSKALX = 'spulbrelskalx'
FLORGLIXFLUL = 'florglixflul'
VANSKARSKIMX = 'vanskarskimx'
VARSTIMK = 'varstimk'
GROSPRIXSPOST = 'grosprixspost'
CLEXSPELR = 'clexspelr'
BLIMFLURGRAL = 'blimflurgral'
GLONBRAXBLAL = 'glonbraxblal'

_R = {
    CLEXSPELR: 0,
    BLIMFLURGRAL: 1,
    GLONBRAXBLAL: 2,
}

_CTX_WRITES_KEY  = 'flurslex'
_CTX_WRITE_STATE = SLIMVAL

class BlalstonFSM:
    def __init__(self):
        self._state = {}

    def _glexstor(self, hint):
        assert self._state.get("current") == GLEXSTOR, \
            f"blalston.glexstor: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glexstor', 2:
                self._state["current"] = GLONBRAXBLAL
                self._state["trig"]    = "hint:2"
            case 'glexstor', 1:
                self._state["current"] = BLIMFLURGRAL
                self._state["trig"]    = "hint:1"
            case 'glexstor', _:
                self._state["current"] = CLANSLAR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glexstor', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glexstor',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glexstor->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _clanslar(self, hint):
        assert self._state.get("current") == CLANSLAR, \
            f"blalston.clanslar: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'clanslar', 2:
                self._state["current"] = GLONBRAXBLAL
                self._state["trig"]    = "hint:2"
            case 'clanslar', 0:
                self._state["current"] = SKEXVEXK
                self._state["trig"]    = "hint:0"
            case 'clanslar', _:
                self._state["current"] = DRURSPIM
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'clanslar', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'clanslar',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"clanslar->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _drurspim(self, hint):
        assert self._state.get("current") == DRURSPIM, \
            f"blalston.drurspim: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'drurspim', 2:
                self._state["current"] = GLONBRAXBLAL
                self._state["trig"]    = "hint:2"
            case 'drurspim', _:
                self._state["current"] = SKEXVEXK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'drurspim', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'drurspim',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"drurspim->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skexvexk(self, hint):
        assert self._state.get("current") == SKEXVEXK, \
            f"blalston.skexvexk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skexvexk', 2:
                self._state["current"] = GLONBRAXBLAL
                self._state["trig"]    = "hint:2"
            case 'skexvexk', 0:
                self._state["current"] = GLEXBRONSKELL
                self._state["trig"]    = "hint:0"
            case 'skexvexk', _:
                self._state["current"] = SKIXSLENL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skexvexk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skexvexk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skexvexk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skixslenl(self, hint):
        assert self._state.get("current") == SKIXSLENL, \
            f"blalston.skixslenl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skixslenl', 2:
                self._state["current"] = GLONBRAXBLAL
                self._state["trig"]    = "hint:2"
            case 'skixslenl', 1:
                self._state["current"] = BLIMFLURGRAL
                self._state["trig"]    = "hint:1"
            case 'skixslenl', _:
                self._state["current"] = GLEXBRONSKELL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skixslenl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skixslenl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skixslenl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glexbronskell(self, hint):
        assert self._state.get("current") == GLEXBRONSKELL, \
            f"blalston.glexbronskell: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glexbronskell', 2:
                self._state["current"] = GLONBRAXBLAL
                self._state["trig"]    = "hint:2"
            case 'glexbronskell', _:
                self._state["current"] = SKORDROSBLAR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glexbronskell', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glexbronskell',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glexbronskell->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skordrosblar(self, hint):
        assert self._state.get("current") == SKORDROSBLAR, \
            f"blalston.skordrosblar: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skordrosblar', 2:
                self._state["current"] = GLONBRAXBLAL
                self._state["trig"]    = "hint:2"
            case 'skordrosblar', _:
                self._state["current"] = BLOSGLARN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skordrosblar', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skordrosblar',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skordrosblar->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blosglarn(self, hint):
        assert self._state.get("current") == BLOSGLARN, \
            f"blalston.blosglarn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blosglarn', 2:
                self._state["current"] = GLONBRAXBLAL
                self._state["trig"]    = "hint:2"
            case 'blosglarn', _:
                self._state["current"] = DRAXGRON
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blosglarn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blosglarn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blosglarn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _draxgron(self, hint):
        assert self._state.get("current") == DRAXGRON, \
            f"blalston.draxgron: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'draxgron', 2:
                self._state["current"] = GLONBRAXBLAL
                self._state["trig"]    = "hint:2"
            case 'draxgron', 0:
                self._state["current"] = BLIMFLURGRAL
                self._state["trig"]    = "hint:0"
            case 'draxgron', _:
                self._state["current"] = PRALBLORGLURX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'draxgron', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'draxgron',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"draxgron->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _pralblorglurx(self, hint):
        assert self._state.get("current") == PRALBLORGLURX, \
            f"blalston.pralblorglurx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'pralblorglurx', 2:
                self._state["current"] = GLONBRAXBLAL
                self._state["trig"]    = "hint:2"
            case 'pralblorglurx', _:
                self._state["current"] = GLULTRUL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'pralblorglurx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'pralblorglurx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"pralblorglurx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glultrul(self, hint):
        assert self._state.get("current") == GLULTRUL, \
            f"blalston.glultrul: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glultrul', 2:
                self._state["current"] = GLONBRAXBLAL
                self._state["trig"]    = "hint:2"
            case 'glultrul', 1:
                self._state["current"] = BLIMFLURGRAL
                self._state["trig"]    = "hint:1"
            case 'glultrul', _:
                self._state["current"] = VARKRURVON
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glultrul', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glultrul',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glultrul->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _varkrurvon(self, hint):
        assert self._state.get("current") == VARKRURVON, \
            f"blalston.varkrurvon: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'varkrurvon', 2:
                self._state["current"] = GLONBRAXBLAL
                self._state["trig"]    = "hint:2"
            case 'varkrurvon', 0:
                self._state["current"] = TRANTRURK
                self._state["trig"]    = "hint:0"
            case 'varkrurvon', _:
                self._state["current"] = DRENGRUL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'varkrurvon', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'varkrurvon',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"varkrurvon->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _drengrul(self, hint):
        assert self._state.get("current") == DRENGRUL, \
            f"blalston.drengrul: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'drengrul', 2:
                self._state["current"] = GLONBRAXBLAL
                self._state["trig"]    = "hint:2"
            case 'drengrul', 0:
                self._state["current"] = BLIMFLURGRAL
                self._state["trig"]    = "hint:0"
            case 'drengrul', _:
                self._state["current"] = TRANTRURK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'drengrul', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'drengrul',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"drengrul->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _trantrurk(self, hint):
        assert self._state.get("current") == TRANTRURK, \
            f"blalston.trantrurk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'trantrurk', 2:
                self._state["current"] = GLONBRAXBLAL
                self._state["trig"]    = "hint:2"
            case 'trantrurk', 0:
                self._state["current"] = BLIMFLURGRAL
                self._state["trig"]    = "hint:0"
            case 'trantrurk', _:
                self._state["current"] = SLIMVAL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'trantrurk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'trantrurk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"trantrurk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slimval(self, hint):
        assert self._state.get("current") == SLIMVAL, \
            f"blalston.slimval: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        _ctx_val_before = self._state["ctx"].get(_CTX_WRITES_KEY, 0)
        match self._state["current"], hint:
            case 'slimval', 2:
                self._state["current"] = GLONBRAXBLAL
                self._state["trig"]    = "hint:2"
            case 'slimval', _:
                self._state["current"] = TRULSLALCLEX
                self._state["trig"]    = "auto"
        _old = self._state["ctx"].get(_CTX_WRITES_KEY, 0)
        _inc = 2 if hint == 2 else 1
        self._state["ctx"][_CTX_WRITES_KEY] = _old + _inc
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slimval', _to, _trig)
        _conds = {"hint_branch": _hint_branch,
                   "ctx_write": True,
                   "ctx_val_before": _ctx_val_before}
        _emit(self._state["cycle"], 1, __name__, 'slimval',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slimval->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _trulslalclex(self, hint):
        assert self._state.get("current") == TRULSLALCLEX, \
            f"blalston.trulslalclex: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'trulslalclex', 2:
                self._state["current"] = GLONBRAXBLAL
                self._state["trig"]    = "hint:2"
            case 'trulslalclex', _:
                self._state["current"] = SLENVOSSTEX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'trulslalclex', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'trulslalclex',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"trulslalclex->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slenvosstex(self, hint):
        assert self._state.get("current") == SLENVOSSTEX, \
            f"blalston.slenvosstex: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slenvosstex', 2:
                self._state["current"] = GLONBRAXBLAL
                self._state["trig"]    = "hint:2"
            case 'slenvosstex', 1:
                self._state["current"] = CLENSLURGLALX
                self._state["trig"]    = "hint:1"
            case 'slenvosstex', _:
                self._state["current"] = CLULBRALN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slenvosstex', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slenvosstex',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slenvosstex->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _clulbraln(self, hint):
        assert self._state.get("current") == CLULBRALN, \
            f"blalston.clulbraln: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'clulbraln', 2:
                self._state["current"] = GLONBRAXBLAL
                self._state["trig"]    = "hint:2"
            case 'clulbraln', 1:
                self._state["current"] = BLIMFLURGRAL
                self._state["trig"]    = "hint:1"
            case 'clulbraln', _:
                self._state["current"] = CLENSLURGLALX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'clulbraln', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'clulbraln',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"clulbraln->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _clenslurglalx(self, hint):
        assert self._state.get("current") == CLENSLURGLALX, \
            f"blalston.clenslurglalx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'clenslurglalx', 2:
                self._state["current"] = GLONBRAXBLAL
                self._state["trig"]    = "hint:2"
            case 'clenslurglalx', 1:
                self._state["current"] = FLEXSTIXN
                self._state["trig"]    = "hint:1"
            case 'clenslurglalx', _:
                self._state["current"] = DRANFLENTRON
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'clenslurglalx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'clenslurglalx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"clenslurglalx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _dranflentron(self, hint):
        assert self._state.get("current") == DRANFLENTRON, \
            f"blalston.dranflentron: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'dranflentron', 2:
                self._state["current"] = GLONBRAXBLAL
                self._state["trig"]    = "hint:2"
            case 'dranflentron', 1:
                self._state["current"] = FLENGLALKRANN
                self._state["trig"]    = "hint:1"
            case 'dranflentron', _:
                self._state["current"] = FLEXSTIXN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'dranflentron', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'dranflentron',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"dranflentron->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _flexstixn(self, hint):
        assert self._state.get("current") == FLEXSTIXN, \
            f"blalston.flexstixn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'flexstixn', 2:
                self._state["current"] = GLONBRAXBLAL
                self._state["trig"]    = "hint:2"
            case 'flexstixn', _:
                self._state["current"] = FLENGLALKRANN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'flexstixn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'flexstixn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"flexstixn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _flenglalkrann(self, hint):
        assert self._state.get("current") == FLENGLALKRANN, \
            f"blalston.flenglalkrann: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'flenglalkrann', 2:
                self._state["current"] = GLONBRAXBLAL
                self._state["trig"]    = "hint:2"
            case 'flenglalkrann', _:
                self._state["current"] = BLOSGLAXCLUL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'flenglalkrann', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'flenglalkrann',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"flenglalkrann->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blosglaxclul(self, hint):
        assert self._state.get("current") == BLOSGLAXCLUL, \
            f"blalston.blosglaxclul: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blosglaxclul', 2:
                self._state["current"] = GLONBRAXBLAL
                self._state["trig"]    = "hint:2"
            case 'blosglaxclul', 0:
                self._state["current"] = DRANGLALDRARK
                self._state["trig"]    = "hint:0"
            case 'blosglaxclul', _:
                self._state["current"] = CLANSKENN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blosglaxclul', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blosglaxclul',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blosglaxclul->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _clanskenn(self, hint):
        assert self._state.get("current") == CLANSKENN, \
            f"blalston.clanskenn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'clanskenn', 2:
                self._state["current"] = GLONBRAXBLAL
                self._state["trig"]    = "hint:2"
            case 'clanskenn', 0:
                self._state["current"] = BRENBLUR
                self._state["trig"]    = "hint:0"
            case 'clanskenn', _:
                self._state["current"] = DRANGLALDRARK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'clanskenn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'clanskenn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"clanskenn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _dranglaldrark(self, hint):
        assert self._state.get("current") == DRANGLALDRARK, \
            f"blalston.dranglaldrark: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'dranglaldrark', 2:
                self._state["current"] = GLONBRAXBLAL
                self._state["trig"]    = "hint:2"
            case 'dranglaldrark', 0:
                self._state["current"] = BLIMFLURGRAL
                self._state["trig"]    = "hint:0"
            case 'dranglaldrark', _:
                self._state["current"] = BRENBLUR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'dranglaldrark', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'dranglaldrark',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"dranglaldrark->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brenblur(self, hint):
        assert self._state.get("current") == BRENBLUR, \
            f"blalston.brenblur: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brenblur', 2:
                self._state["current"] = GLONBRAXBLAL
                self._state["trig"]    = "hint:2"
            case 'brenblur', 0:
                self._state["current"] = BLIMFLURGRAL
                self._state["trig"]    = "hint:0"
            case 'brenblur', _:
                self._state["current"] = GRAXSTAL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brenblur', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brenblur',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brenblur->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _graxstal(self, hint):
        assert self._state.get("current") == GRAXSTAL, \
            f"blalston.graxstal: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'graxstal', 2:
                self._state["current"] = GLONBRAXBLAL
                self._state["trig"]    = "hint:2"
            case 'graxstal', _:
                self._state["current"] = CLULFLONL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'graxstal', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'graxstal',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"graxstal->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _clulflonl(self, hint):
        assert self._state.get("current") == CLULFLONL, \
            f"blalston.clulflonl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'clulflonl', 2:
                self._state["current"] = GLONBRAXBLAL
                self._state["trig"]    = "hint:2"
            case 'clulflonl', _:
                self._state["current"] = SKURGRARK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'clulflonl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'clulflonl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"clulflonl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skurgrark(self, hint):
        assert self._state.get("current") == SKURGRARK, \
            f"blalston.skurgrark: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skurgrark', 2:
                self._state["current"] = GLONBRAXBLAL
                self._state["trig"]    = "hint:2"
            case 'skurgrark', 1:
                self._state["current"] = BLARDRENPREXN
                self._state["trig"]    = "hint:1"
            case 'skurgrark', _:
                self._state["current"] = SKULDRELVUL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skurgrark', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skurgrark',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skurgrark->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skuldrelvul(self, hint):
        assert self._state.get("current") == SKULDRELVUL, \
            f"blalston.skuldrelvul: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skuldrelvul', 2:
                self._state["current"] = GLONBRAXBLAL
                self._state["trig"]    = "hint:2"
            case 'skuldrelvul', _:
                self._state["current"] = BLARDRENPREXN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skuldrelvul', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skuldrelvul',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skuldrelvul->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blardrenprexn(self, hint):
        assert self._state.get("current") == BLARDRENPREXN, \
            f"blalston.blardrenprexn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blardrenprexn', 2:
                self._state["current"] = GLONBRAXBLAL
                self._state["trig"]    = "hint:2"
            case 'blardrenprexn', 1:
                self._state["current"] = BLIMFLURGRAL
                self._state["trig"]    = "hint:1"
            case 'blardrenprexn', _:
                self._state["current"] = SKAXSPARPRUL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blardrenprexn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blardrenprexn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blardrenprexn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skaxsparprul(self, hint):
        assert self._state.get("current") == SKAXSPARPRUL, \
            f"blalston.skaxsparprul: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skaxsparprul', 2:
                self._state["current"] = GLONBRAXBLAL
                self._state["trig"]    = "hint:2"
            case 'skaxsparprul', 1:
                self._state["current"] = BLIMFLURGRAL
                self._state["trig"]    = "hint:1"
            case 'skaxsparprul', _:
                self._state["current"] = CLULSKORKREXK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skaxsparprul', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skaxsparprul',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skaxsparprul->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _clulskorkrexk(self, hint):
        assert self._state.get("current") == CLULSKORKREXK, \
            f"blalston.clulskorkrexk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'clulskorkrexk', 2:
                self._state["current"] = GLONBRAXBLAL
                self._state["trig"]    = "hint:2"
            case 'clulskorkrexk', 0:
                self._state["current"] = BRANCLORFLEN
                self._state["trig"]    = "hint:0"
            case 'clulskorkrexk', _:
                self._state["current"] = KRONFLOSFLEL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'clulskorkrexk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'clulskorkrexk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"clulskorkrexk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _kronflosflel(self, hint):
        assert self._state.get("current") == KRONFLOSFLEL, \
            f"blalston.kronflosflel: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'kronflosflel', 2:
                self._state["current"] = GLONBRAXBLAL
                self._state["trig"]    = "hint:2"
            case 'kronflosflel', 1:
                self._state["current"] = BLIMFLURGRAL
                self._state["trig"]    = "hint:1"
            case 'kronflosflel', _:
                self._state["current"] = BRANCLORFLEN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'kronflosflel', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'kronflosflel',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"kronflosflel->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _branclorflen(self, hint):
        assert self._state.get("current") == BRANCLORFLEN, \
            f"blalston.branclorflen: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'branclorflen', 2:
                self._state["current"] = GLONBRAXBLAL
                self._state["trig"]    = "hint:2"
            case 'branclorflen', 1:
                self._state["current"] = VEXKRELGRAX
                self._state["trig"]    = "hint:1"
            case 'branclorflen', _:
                self._state["current"] = SPOSTRELN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'branclorflen', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'branclorflen',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"branclorflen->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _spostreln(self, hint):
        assert self._state.get("current") == SPOSTRELN, \
            f"blalston.spostreln: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'spostreln', 2:
                self._state["current"] = GLONBRAXBLAL
                self._state["trig"]    = "hint:2"
            case 'spostreln', 0:
                self._state["current"] = STARVURKROR
                self._state["trig"]    = "hint:0"
            case 'spostreln', _:
                self._state["current"] = VEXKRELGRAX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'spostreln', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'spostreln',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"spostreln->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _vexkrelgrax(self, hint):
        assert self._state.get("current") == VEXKRELGRAX, \
            f"blalston.vexkrelgrax: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'vexkrelgrax', 2:
                self._state["current"] = GLONBRAXBLAL
                self._state["trig"]    = "hint:2"
            case 'vexkrelgrax', _:
                self._state["current"] = STARVURKROR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'vexkrelgrax', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'vexkrelgrax',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"vexkrelgrax->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _starvurkror(self, hint):
        assert self._state.get("current") == STARVURKROR, \
            f"blalston.starvurkror: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'starvurkror', 2:
                self._state["current"] = GLONBRAXBLAL
                self._state["trig"]    = "hint:2"
            case 'starvurkror', 0:
                self._state["current"] = VELFLENDROSR
                self._state["trig"]    = "hint:0"
            case 'starvurkror', _:
                self._state["current"] = VAXSLAXBLOR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'starvurkror', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'starvurkror',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"starvurkror->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _vaxslaxblor(self, hint):
        assert self._state.get("current") == VAXSLAXBLOR, \
            f"blalston.vaxslaxblor: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'vaxslaxblor', 2:
                self._state["current"] = GLONBRAXBLAL
                self._state["trig"]    = "hint:2"
            case 'vaxslaxblor', 1:
                self._state["current"] = BLIMFLURGRAL
                self._state["trig"]    = "hint:1"
            case 'vaxslaxblor', _:
                self._state["current"] = VELFLENDROSR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'vaxslaxblor', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'vaxslaxblor',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"vaxslaxblor->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _velflendrosr(self, hint):
        assert self._state.get("current") == VELFLENDROSR, \
            f"blalston.velflendrosr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'velflendrosr', 2:
                self._state["current"] = GLONBRAXBLAL
                self._state["trig"]    = "hint:2"
            case 'velflendrosr', 0:
                self._state["current"] = GLORFLALR
                self._state["trig"]    = "hint:0"
            case 'velflendrosr', _:
                self._state["current"] = SPARSLENGLULK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'velflendrosr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'velflendrosr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"velflendrosr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _sparslenglulk(self, hint):
        assert self._state.get("current") == SPARSLENGLULK, \
            f"blalston.sparslenglulk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'sparslenglulk', 2:
                self._state["current"] = GLONBRAXBLAL
                self._state["trig"]    = "hint:2"
            case 'sparslenglulk', 0:
                self._state["current"] = BLIMFLURGRAL
                self._state["trig"]    = "hint:0"
            case 'sparslenglulk', _:
                self._state["current"] = GLORFLALR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'sparslenglulk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'sparslenglulk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"sparslenglulk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glorflalr(self, hint):
        assert self._state.get("current") == GLORFLALR, \
            f"blalston.glorflalr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glorflalr', 2:
                self._state["current"] = GLONBRAXBLAL
                self._state["trig"]    = "hint:2"
            case 'glorflalr', _:
                self._state["current"] = KROSCLENDRUR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glorflalr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glorflalr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glorflalr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _krosclendrur(self, hint):
        assert self._state.get("current") == KROSCLENDRUR, \
            f"blalston.krosclendrur: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'krosclendrur', 2:
                self._state["current"] = GLONBRAXBLAL
                self._state["trig"]    = "hint:2"
            case 'krosclendrur', 1:
                self._state["current"] = CLAXPRELSKOR
                self._state["trig"]    = "hint:1"
            case 'krosclendrur', _:
                self._state["current"] = TRIXSLULGREXK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'krosclendrur', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'krosclendrur',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"krosclendrur->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _trixslulgrexk(self, hint):
        assert self._state.get("current") == TRIXSLULGREXK, \
            f"blalston.trixslulgrexk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'trixslulgrexk', 2:
                self._state["current"] = GLONBRAXBLAL
                self._state["trig"]    = "hint:2"
            case 'trixslulgrexk', _:
                self._state["current"] = CLAXPRELSKOR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'trixslulgrexk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'trixslulgrexk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"trixslulgrexk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _claxprelskor(self, hint):
        assert self._state.get("current") == CLAXPRELSKOR, \
            f"blalston.claxprelskor: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'claxprelskor', 2:
                self._state["current"] = GLONBRAXBLAL
                self._state["trig"]    = "hint:2"
            case 'claxprelskor', _:
                self._state["current"] = FLALDRALFLELN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'claxprelskor', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'claxprelskor',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"claxprelskor->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _flaldralfleln(self, hint):
        assert self._state.get("current") == FLALDRALFLELN, \
            f"blalston.flaldralfleln: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'flaldralfleln', 2:
                self._state["current"] = GLONBRAXBLAL
                self._state["trig"]    = "hint:2"
            case 'flaldralfleln', _:
                self._state["current"] = SPEXBLURT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'flaldralfleln', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'flaldralfleln',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"flaldralfleln->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _spexblurt(self, hint):
        assert self._state.get("current") == SPEXBLURT, \
            f"blalston.spexblurt: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'spexblurt', 2:
                self._state["current"] = GLONBRAXBLAL
                self._state["trig"]    = "hint:2"
            case 'spexblurt', _:
                self._state["current"] = PREXKRANX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'spexblurt', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'spexblurt',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"spexblurt->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _prexkranx(self, hint):
        assert self._state.get("current") == PREXKRANX, \
            f"blalston.prexkranx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'prexkranx', 2:
                self._state["current"] = GLONBRAXBLAL
                self._state["trig"]    = "hint:2"
            case 'prexkranx', 0:
                self._state["current"] = BLIMFLURGRAL
                self._state["trig"]    = "hint:0"
            case 'prexkranx', _:
                self._state["current"] = SKONSKIMN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'prexkranx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'prexkranx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"prexkranx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skonskimn(self, hint):
        assert self._state.get("current") == SKONSKIMN, \
            f"blalston.skonskimn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skonskimn', 2:
                self._state["current"] = GLONBRAXBLAL
                self._state["trig"]    = "hint:2"
            case 'skonskimn', _:
                self._state["current"] = TRIMVARSKANX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skonskimn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skonskimn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skonskimn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _trimvarskanx(self, hint):
        assert self._state.get("current") == TRIMVARSKANX, \
            f"blalston.trimvarskanx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'trimvarskanx', 2:
                self._state["current"] = GLONBRAXBLAL
                self._state["trig"]    = "hint:2"
            case 'trimvarskanx', _:
                self._state["current"] = VOSFLENTRAXT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'trimvarskanx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'trimvarskanx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"trimvarskanx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _vosflentraxt(self, hint):
        assert self._state.get("current") == VOSFLENTRAXT, \
            f"blalston.vosflentraxt: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'vosflentraxt', 2:
                self._state["current"] = GLONBRAXBLAL
                self._state["trig"]    = "hint:2"
            case 'vosflentraxt', _:
                self._state["current"] = STORKRAX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'vosflentraxt', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'vosflentraxt',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"vosflentraxt->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _storkrax(self, hint):
        assert self._state.get("current") == STORKRAX, \
            f"blalston.storkrax: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'storkrax', 2:
                self._state["current"] = GLONBRAXBLAL
                self._state["trig"]    = "hint:2"
            case 'storkrax', 0:
                self._state["current"] = VONVAXL
                self._state["trig"]    = "hint:0"
            case 'storkrax', _:
                self._state["current"] = STULPRORL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'storkrax', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'storkrax',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"storkrax->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _stulprorl(self, hint):
        assert self._state.get("current") == STULPRORL, \
            f"blalston.stulprorl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'stulprorl', 2:
                self._state["current"] = GLONBRAXBLAL
                self._state["trig"]    = "hint:2"
            case 'stulprorl', 0:
                self._state["current"] = TRENSTUL
                self._state["trig"]    = "hint:0"
            case 'stulprorl', _:
                self._state["current"] = VONVAXL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'stulprorl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'stulprorl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"stulprorl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _vonvaxl(self, hint):
        assert self._state.get("current") == VONVAXL, \
            f"blalston.vonvaxl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'vonvaxl', 2:
                self._state["current"] = GLONBRAXBLAL
                self._state["trig"]    = "hint:2"
            case 'vonvaxl', 1:
                self._state["current"] = VIXBLUR
                self._state["trig"]    = "hint:1"
            case 'vonvaxl', _:
                self._state["current"] = TRENSTUL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'vonvaxl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'vonvaxl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"vonvaxl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _trenstul(self, hint):
        assert self._state.get("current") == TRENSTUL, \
            f"blalston.trenstul: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'trenstul', 2:
                self._state["current"] = GLONBRAXBLAL
                self._state["trig"]    = "hint:2"
            case 'trenstul', 1:
                self._state["current"] = BREXGLEXT
                self._state["trig"]    = "hint:1"
            case 'trenstul', _:
                self._state["current"] = VIXBLUR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'trenstul', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'trenstul',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"trenstul->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _vixblur(self, hint):
        assert self._state.get("current") == VIXBLUR, \
            f"blalston.vixblur: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'vixblur', 2:
                self._state["current"] = GLONBRAXBLAL
                self._state["trig"]    = "hint:2"
            case 'vixblur', 0:
                self._state["current"] = VENBREXTRELR
                self._state["trig"]    = "hint:0"
            case 'vixblur', _:
                self._state["current"] = BREXGLEXT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'vixblur', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'vixblur',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"vixblur->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brexglext(self, hint):
        assert self._state.get("current") == BREXGLEXT, \
            f"blalston.brexglext: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brexglext', 2:
                self._state["current"] = GLONBRAXBLAL
                self._state["trig"]    = "hint:2"
            case 'brexglext', 1:
                self._state["current"] = BLIMFLURGRAL
                self._state["trig"]    = "hint:1"
            case 'brexglext', _:
                self._state["current"] = VENBREXTRELR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brexglext', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brexglext',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brexglext->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _venbrextrelr(self, hint):
        assert self._state.get("current") == VENBREXTRELR, \
            f"blalston.venbrextrelr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'venbrextrelr', 2:
                self._state["current"] = GLONBRAXBLAL
                self._state["trig"]    = "hint:2"
            case 'venbrextrelr', 1:
                self._state["current"] = BLURFLAL
                self._state["trig"]    = "hint:1"
            case 'venbrextrelr', _:
                self._state["current"] = SLANSTEX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'venbrextrelr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'venbrextrelr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"venbrextrelr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slanstex(self, hint):
        assert self._state.get("current") == SLANSTEX, \
            f"blalston.slanstex: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slanstex', 2:
                self._state["current"] = GLONBRAXBLAL
                self._state["trig"]    = "hint:2"
            case 'slanstex', _:
                self._state["current"] = BLURFLAL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slanstex', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slanstex',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slanstex->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blurflal(self, hint):
        assert self._state.get("current") == BLURFLAL, \
            f"blalston.blurflal: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blurflal', 2:
                self._state["current"] = GLONBRAXBLAL
                self._state["trig"]    = "hint:2"
            case 'blurflal', _:
                self._state["current"] = SPULBRELSKALX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blurflal', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blurflal',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blurflal->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _spulbrelskalx(self, hint):
        assert self._state.get("current") == SPULBRELSKALX, \
            f"blalston.spulbrelskalx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'spulbrelskalx', 2:
                self._state["current"] = GLONBRAXBLAL
                self._state["trig"]    = "hint:2"
            case 'spulbrelskalx', _:
                self._state["current"] = FLORGLIXFLUL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'spulbrelskalx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'spulbrelskalx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"spulbrelskalx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _florglixflul(self, hint):
        assert self._state.get("current") == FLORGLIXFLUL, \
            f"blalston.florglixflul: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'florglixflul', 2:
                self._state["current"] = GLONBRAXBLAL
                self._state["trig"]    = "hint:2"
            case 'florglixflul', 1:
                self._state["current"] = BLIMFLURGRAL
                self._state["trig"]    = "hint:1"
            case 'florglixflul', _:
                self._state["current"] = VANSKARSKIMX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'florglixflul', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'florglixflul',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"florglixflul->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _vanskarskimx(self, hint):
        assert self._state.get("current") == VANSKARSKIMX, \
            f"blalston.vanskarskimx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'vanskarskimx', 2:
                self._state["current"] = GLONBRAXBLAL
                self._state["trig"]    = "hint:2"
            case 'vanskarskimx', _:
                self._state["current"] = VARSTIMK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'vanskarskimx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'vanskarskimx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"vanskarskimx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _varstimk(self, hint):
        assert self._state.get("current") == VARSTIMK, \
            f"blalston.varstimk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'varstimk', 2:
                self._state["current"] = GLONBRAXBLAL
                self._state["trig"]    = "hint:2"
            case 'varstimk', _:
                self._state["current"] = GROSPRIXSPOST
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'varstimk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'varstimk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"varstimk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _grosprixspost(self, hint):
        assert self._state.get("current") == GROSPRIXSPOST, \
            f"blalston.grosprixspost: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'grosprixspost', 2:
                self._state["current"] = GLONBRAXBLAL
                self._state["trig"]    = "hint:2"
            case 'grosprixspost', 0:
                self._state["current"] = BLIMFLURGRAL
                self._state["trig"]    = "hint:0"
            case 'grosprixspost', _:
                self._state["current"] = CLEXSPELR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'grosprixspost', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'grosprixspost',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"grosprixspost->{_to}", _xid_val)
        self._state["cycle"] += 1

    def invoke(self, hint=None, span=None, caller=None, ctx=None, cycle=0):
        if ctx is None: ctx = {}

        self._state = {"current": GLEXSTOR, "ctx": ctx,
                        "span": span, "caller": caller,
                        "trig": "auto", "cycle": cycle}
        _dispatch = {
            GLEXSTOR: self._glexstor,
            CLANSLAR: self._clanslar,
            DRURSPIM: self._drurspim,
            SKEXVEXK: self._skexvexk,
            SKIXSLENL: self._skixslenl,
            GLEXBRONSKELL: self._glexbronskell,
            SKORDROSBLAR: self._skordrosblar,
            BLOSGLARN: self._blosglarn,
            DRAXGRON: self._draxgron,
            PRALBLORGLURX: self._pralblorglurx,
            GLULTRUL: self._glultrul,
            VARKRURVON: self._varkrurvon,
            DRENGRUL: self._drengrul,
            TRANTRURK: self._trantrurk,
            SLIMVAL: self._slimval,
            TRULSLALCLEX: self._trulslalclex,
            SLENVOSSTEX: self._slenvosstex,
            CLULBRALN: self._clulbraln,
            CLENSLURGLALX: self._clenslurglalx,
            DRANFLENTRON: self._dranflentron,
            FLEXSTIXN: self._flexstixn,
            FLENGLALKRANN: self._flenglalkrann,
            BLOSGLAXCLUL: self._blosglaxclul,
            CLANSKENN: self._clanskenn,
            DRANGLALDRARK: self._dranglaldrark,
            BRENBLUR: self._brenblur,
            GRAXSTAL: self._graxstal,
            CLULFLONL: self._clulflonl,
            SKURGRARK: self._skurgrark,
            SKULDRELVUL: self._skuldrelvul,
            BLARDRENPREXN: self._blardrenprexn,
            SKAXSPARPRUL: self._skaxsparprul,
            CLULSKORKREXK: self._clulskorkrexk,
            KRONFLOSFLEL: self._kronflosflel,
            BRANCLORFLEN: self._branclorflen,
            SPOSTRELN: self._spostreln,
            VEXKRELGRAX: self._vexkrelgrax,
            STARVURKROR: self._starvurkror,
            VAXSLAXBLOR: self._vaxslaxblor,
            VELFLENDROSR: self._velflendrosr,
            SPARSLENGLULK: self._sparslenglulk,
            GLORFLALR: self._glorflalr,
            KROSCLENDRUR: self._krosclendrur,
            TRIXSLULGREXK: self._trixslulgrexk,
            CLAXPRELSKOR: self._claxprelskor,
            FLALDRALFLELN: self._flaldralfleln,
            SPEXBLURT: self._spexblurt,
            PREXKRANX: self._prexkranx,
            SKONSKIMN: self._skonskimn,
            TRIMVARSKANX: self._trimvarskanx,
            VOSFLENTRAXT: self._vosflentraxt,
            STORKRAX: self._storkrax,
            STULPRORL: self._stulprorl,
            VONVAXL: self._vonvaxl,
            TRENSTUL: self._trenstul,
            VIXBLUR: self._vixblur,
            BREXGLEXT: self._brexglext,
            VENBREXTRELR: self._venbrextrelr,
            SLANSTEX: self._slanstex,
            BLURFLAL: self._blurflal,
            SPULBRELSKALX: self._spulbrelskalx,
            FLORGLIXFLUL: self._florglixflul,
            VANSKARSKIMX: self._vanskarskimx,
            VARSTIMK: self._varstimk,
            GROSPRIXSPOST: self._grosprixspost,
        }
        while self._state["current"] not in _R and self._state["cycle"] - cycle < 8000:
            _dispatch[self._state["current"]](hint)
        _ret     = _R.get(self._state["current"], -1)
        _is_err  = self._state["current"] == GLONBRAXBLAL
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
    return BlalstonFSM().invoke(hint=hint, span=span, caller=caller, ctx=ctx, cycle=cycle)
