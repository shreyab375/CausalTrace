from _log import _w as _emit, _xid

FLENSPIXDRELK = 'flenspixdrelk'
SPURSKIX = 'spurskix'
PREXSTENK = 'prexstenk'
KRIXKRURVANN = 'krixkrurvann'
FLALGLENSTIM = 'flalglenstim'
KRARSTIML = 'krarstiml'
FLIMPRALX = 'flimpralx'
TRENBLIX = 'trenblix'
GLELGRIX = 'glelgrix'
SPONGROSSPIM = 'spongrosspim'
TRENKRELBRUR = 'trenkrelbrur'
BLANPRIXCLIXX = 'blanprixclixx'
BRONGLOSK = 'bronglosk'
BLULKROSVENL = 'blulkrosvenl'
FLELKRAXK = 'flelkraxk'
VANBLIXSTORL = 'vanblixstorl'
GROSFLIXT = 'grosflixt'
SKAXSLELK = 'skaxslelk'
TRALGLELX = 'tralglelx'
BRIXGRURGRALN = 'brixgrurgraln'
SLONDRELKROR = 'slondrelkror'
FLULCLENR = 'flulclenr'
SLANGLIM = 'slanglim'
GLORGRIXVAL = 'glorgrixval'
SKEXSPART = 'skexspart'
GLALSPELKREXK = 'glalspelkrexk'
BREXBRORGRONK = 'brexbrorgronk'
CLARBRAXSPUL = 'clarbraxspul'
BLIXSLIXX = 'blixslixx'
BLAXTRULSPOR = 'blaxtrulspor'
STEXDRORGLELN = 'stexdrorgleln'
BLIMVARFLIMR = 'blimvarflimr'
TRULGRURBRENT = 'trulgrurbrent'
BRIXSTALT = 'brixstalt'
SKEXFLEXPREL = 'skexflexprel'
DRELDRENX = 'dreldrenx'
BLALGRAXSTON = 'blalgraxston'
BLONSPORSKUR = 'blonsporskur'
VURSTAXSKEN = 'vurstaxsken'
TROSSPURPRANN = 'trosspurprann'
SKULBLIX = 'skulblix'
BRIXFLIM = 'brixflim'
CLOSBRENGLELX = 'closbrenglelx'
GLONTRIXBRAR = 'glontrixbrar'
GRORSPOSK = 'grorsposk'
BRURPROSX = 'brurprosx'
TRALGLULGLUR = 'tralglulglur'
GRIMVIMGLAN = 'grimvimglan'
GRIMPRUR = 'grimprur'
TRIXTRELFLULT = 'trixtrelflult'
SPARPRAXDRORN = 'sparpraxdrorn'
VOSCLIMX = 'vosclimx'
DRULSTIXK = 'drulstixk'
BRANGREXL = 'brangrexl'
TRORDRORFLULT = 'trordrorflult'
SLOSBLORSKIXK = 'slosblorskixk'
KRIMSPAXSPIXK = 'krimspaxspixk'
STIXVORBREL = 'stixvorbrel'
FLENSLIM = 'flenslim'
BRIMVONDRAX = 'brimvondrax'
GRONSKONGLAXX = 'gronskonglaxx'
BLORSLIMCLULK = 'blorslimclulk'
CLIMDRUL = 'climdrul'
BLOSKRAX = 'bloskrax'
PRELCLONCLIX = 'prelclonclix'
GLEXDRENDRURL = 'glexdrendrurl'
BRORSTIXFLANT = 'brorstixflant'
TRENCLULSKIXT = 'trenclulskixt'

_R = {
    GLEXDRENDRURL: 0,
    BRORSTIXFLANT: 1,
    TRENCLULSKIXT: 2,
}

_CTX_WRITES_KEY  = 'flurslex'
_CTX_WRITE_STATE = VANBLIXSTORL

class PrelspalkFSM:
    def __init__(self):
        self._state = {}

    def _flenspixdrelk(self, hint):
        assert self._state.get("current") == FLENSPIXDRELK, \
            f"prelspalk.flenspixdrelk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'flenspixdrelk', 2:
                self._state["current"] = TRENCLULSKIXT
                self._state["trig"]    = "hint:2"
            case 'flenspixdrelk', 0:
                self._state["current"] = BRORSTIXFLANT
                self._state["trig"]    = "hint:0"
            case 'flenspixdrelk', _:
                self._state["current"] = SPURSKIX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'flenspixdrelk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'flenspixdrelk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"flenspixdrelk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _spurskix(self, hint):
        assert self._state.get("current") == SPURSKIX, \
            f"prelspalk.spurskix: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'spurskix', 2:
                self._state["current"] = TRENCLULSKIXT
                self._state["trig"]    = "hint:2"
            case 'spurskix', _:
                self._state["current"] = PREXSTENK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'spurskix', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'spurskix',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"spurskix->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _prexstenk(self, hint):
        assert self._state.get("current") == PREXSTENK, \
            f"prelspalk.prexstenk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'prexstenk', 2:
                self._state["current"] = TRENCLULSKIXT
                self._state["trig"]    = "hint:2"
            case 'prexstenk', 1:
                self._state["current"] = FLALGLENSTIM
                self._state["trig"]    = "hint:1"
            case 'prexstenk', _:
                self._state["current"] = KRIXKRURVANN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'prexstenk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'prexstenk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"prexstenk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _krixkrurvann(self, hint):
        assert self._state.get("current") == KRIXKRURVANN, \
            f"prelspalk.krixkrurvann: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'krixkrurvann', 2:
                self._state["current"] = TRENCLULSKIXT
                self._state["trig"]    = "hint:2"
            case 'krixkrurvann', 0:
                self._state["current"] = BRORSTIXFLANT
                self._state["trig"]    = "hint:0"
            case 'krixkrurvann', _:
                self._state["current"] = FLALGLENSTIM
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'krixkrurvann', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'krixkrurvann',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"krixkrurvann->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _flalglenstim(self, hint):
        assert self._state.get("current") == FLALGLENSTIM, \
            f"prelspalk.flalglenstim: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'flalglenstim', 2:
                self._state["current"] = TRENCLULSKIXT
                self._state["trig"]    = "hint:2"
            case 'flalglenstim', 1:
                self._state["current"] = FLIMPRALX
                self._state["trig"]    = "hint:1"
            case 'flalglenstim', _:
                self._state["current"] = KRARSTIML
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'flalglenstim', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'flalglenstim',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"flalglenstim->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _krarstiml(self, hint):
        assert self._state.get("current") == KRARSTIML, \
            f"prelspalk.krarstiml: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'krarstiml', 2:
                self._state["current"] = TRENCLULSKIXT
                self._state["trig"]    = "hint:2"
            case 'krarstiml', 0:
                self._state["current"] = TRENBLIX
                self._state["trig"]    = "hint:0"
            case 'krarstiml', _:
                self._state["current"] = FLIMPRALX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'krarstiml', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'krarstiml',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"krarstiml->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _flimpralx(self, hint):
        assert self._state.get("current") == FLIMPRALX, \
            f"prelspalk.flimpralx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'flimpralx', 2:
                self._state["current"] = TRENCLULSKIXT
                self._state["trig"]    = "hint:2"
            case 'flimpralx', 0:
                self._state["current"] = BRORSTIXFLANT
                self._state["trig"]    = "hint:0"
            case 'flimpralx', _:
                self._state["current"] = TRENBLIX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'flimpralx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'flimpralx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"flimpralx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _trenblix(self, hint):
        assert self._state.get("current") == TRENBLIX, \
            f"prelspalk.trenblix: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'trenblix', 2:
                self._state["current"] = TRENCLULSKIXT
                self._state["trig"]    = "hint:2"
            case 'trenblix', 0:
                self._state["current"] = BRORSTIXFLANT
                self._state["trig"]    = "hint:0"
            case 'trenblix', _:
                self._state["current"] = GLELGRIX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'trenblix', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'trenblix',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"trenblix->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glelgrix(self, hint):
        assert self._state.get("current") == GLELGRIX, \
            f"prelspalk.glelgrix: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glelgrix', 2:
                self._state["current"] = TRENCLULSKIXT
                self._state["trig"]    = "hint:2"
            case 'glelgrix', 1:
                self._state["current"] = TRENKRELBRUR
                self._state["trig"]    = "hint:1"
            case 'glelgrix', _:
                self._state["current"] = SPONGROSSPIM
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glelgrix', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glelgrix',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glelgrix->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _spongrosspim(self, hint):
        assert self._state.get("current") == SPONGROSSPIM, \
            f"prelspalk.spongrosspim: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'spongrosspim', 2:
                self._state["current"] = TRENCLULSKIXT
                self._state["trig"]    = "hint:2"
            case 'spongrosspim', 0:
                self._state["current"] = BLANPRIXCLIXX
                self._state["trig"]    = "hint:0"
            case 'spongrosspim', _:
                self._state["current"] = TRENKRELBRUR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'spongrosspim', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'spongrosspim',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"spongrosspim->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _trenkrelbrur(self, hint):
        assert self._state.get("current") == TRENKRELBRUR, \
            f"prelspalk.trenkrelbrur: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'trenkrelbrur', 2:
                self._state["current"] = TRENCLULSKIXT
                self._state["trig"]    = "hint:2"
            case 'trenkrelbrur', 0:
                self._state["current"] = BRONGLOSK
                self._state["trig"]    = "hint:0"
            case 'trenkrelbrur', _:
                self._state["current"] = BLANPRIXCLIXX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'trenkrelbrur', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'trenkrelbrur',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"trenkrelbrur->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blanprixclixx(self, hint):
        assert self._state.get("current") == BLANPRIXCLIXX, \
            f"prelspalk.blanprixclixx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blanprixclixx', 2:
                self._state["current"] = TRENCLULSKIXT
                self._state["trig"]    = "hint:2"
            case 'blanprixclixx', 1:
                self._state["current"] = BRORSTIXFLANT
                self._state["trig"]    = "hint:1"
            case 'blanprixclixx', _:
                self._state["current"] = BRONGLOSK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blanprixclixx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blanprixclixx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blanprixclixx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _bronglosk(self, hint):
        assert self._state.get("current") == BRONGLOSK, \
            f"prelspalk.bronglosk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'bronglosk', 2:
                self._state["current"] = TRENCLULSKIXT
                self._state["trig"]    = "hint:2"
            case 'bronglosk', 0:
                self._state["current"] = FLELKRAXK
                self._state["trig"]    = "hint:0"
            case 'bronglosk', _:
                self._state["current"] = BLULKROSVENL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'bronglosk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'bronglosk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"bronglosk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blulkrosvenl(self, hint):
        assert self._state.get("current") == BLULKROSVENL, \
            f"prelspalk.blulkrosvenl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blulkrosvenl', 2:
                self._state["current"] = TRENCLULSKIXT
                self._state["trig"]    = "hint:2"
            case 'blulkrosvenl', _:
                self._state["current"] = FLELKRAXK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blulkrosvenl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blulkrosvenl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blulkrosvenl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _flelkraxk(self, hint):
        assert self._state.get("current") == FLELKRAXK, \
            f"prelspalk.flelkraxk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'flelkraxk', 2:
                self._state["current"] = TRENCLULSKIXT
                self._state["trig"]    = "hint:2"
            case 'flelkraxk', _:
                self._state["current"] = VANBLIXSTORL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'flelkraxk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'flelkraxk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"flelkraxk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _vanblixstorl(self, hint):
        assert self._state.get("current") == VANBLIXSTORL, \
            f"prelspalk.vanblixstorl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        _ctx_val_before = self._state["ctx"].get(_CTX_WRITES_KEY, 0)
        match self._state["current"], hint:
            case 'vanblixstorl', 2:
                self._state["current"] = TRENCLULSKIXT
                self._state["trig"]    = "hint:2"
            case 'vanblixstorl', _:
                self._state["current"] = GROSFLIXT
                self._state["trig"]    = "auto"
        _old = self._state["ctx"].get(_CTX_WRITES_KEY, 0)
        _inc = 2 if hint == 2 else 1
        self._state["ctx"][_CTX_WRITES_KEY] = _old + _inc
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'vanblixstorl', _to, _trig)
        _conds = {"hint_branch": _hint_branch,
                   "ctx_write": True,
                   "ctx_val_before": _ctx_val_before}
        _emit(self._state["cycle"], 1, __name__, 'vanblixstorl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"vanblixstorl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _grosflixt(self, hint):
        assert self._state.get("current") == GROSFLIXT, \
            f"prelspalk.grosflixt: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'grosflixt', 2:
                self._state["current"] = TRENCLULSKIXT
                self._state["trig"]    = "hint:2"
            case 'grosflixt', 0:
                self._state["current"] = TRALGLELX
                self._state["trig"]    = "hint:0"
            case 'grosflixt', _:
                self._state["current"] = SKAXSLELK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'grosflixt', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'grosflixt',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"grosflixt->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skaxslelk(self, hint):
        assert self._state.get("current") == SKAXSLELK, \
            f"prelspalk.skaxslelk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skaxslelk', 2:
                self._state["current"] = TRENCLULSKIXT
                self._state["trig"]    = "hint:2"
            case 'skaxslelk', 1:
                self._state["current"] = BRIXGRURGRALN
                self._state["trig"]    = "hint:1"
            case 'skaxslelk', _:
                self._state["current"] = TRALGLELX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skaxslelk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skaxslelk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skaxslelk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _tralglelx(self, hint):
        assert self._state.get("current") == TRALGLELX, \
            f"prelspalk.tralglelx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'tralglelx', 2:
                self._state["current"] = TRENCLULSKIXT
                self._state["trig"]    = "hint:2"
            case 'tralglelx', _:
                self._state["current"] = BRIXGRURGRALN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'tralglelx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'tralglelx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"tralglelx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brixgrurgraln(self, hint):
        assert self._state.get("current") == BRIXGRURGRALN, \
            f"prelspalk.brixgrurgraln: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brixgrurgraln', 2:
                self._state["current"] = TRENCLULSKIXT
                self._state["trig"]    = "hint:2"
            case 'brixgrurgraln', 0:
                self._state["current"] = FLULCLENR
                self._state["trig"]    = "hint:0"
            case 'brixgrurgraln', _:
                self._state["current"] = SLONDRELKROR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brixgrurgraln', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brixgrurgraln',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brixgrurgraln->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slondrelkror(self, hint):
        assert self._state.get("current") == SLONDRELKROR, \
            f"prelspalk.slondrelkror: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slondrelkror', 2:
                self._state["current"] = TRENCLULSKIXT
                self._state["trig"]    = "hint:2"
            case 'slondrelkror', 0:
                self._state["current"] = SLANGLIM
                self._state["trig"]    = "hint:0"
            case 'slondrelkror', _:
                self._state["current"] = FLULCLENR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slondrelkror', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slondrelkror',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slondrelkror->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _flulclenr(self, hint):
        assert self._state.get("current") == FLULCLENR, \
            f"prelspalk.flulclenr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'flulclenr', 2:
                self._state["current"] = TRENCLULSKIXT
                self._state["trig"]    = "hint:2"
            case 'flulclenr', _:
                self._state["current"] = SLANGLIM
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'flulclenr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'flulclenr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"flulclenr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slanglim(self, hint):
        assert self._state.get("current") == SLANGLIM, \
            f"prelspalk.slanglim: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slanglim', 2:
                self._state["current"] = TRENCLULSKIXT
                self._state["trig"]    = "hint:2"
            case 'slanglim', 0:
                self._state["current"] = BRORSTIXFLANT
                self._state["trig"]    = "hint:0"
            case 'slanglim', _:
                self._state["current"] = GLORGRIXVAL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slanglim', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slanglim',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slanglim->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glorgrixval(self, hint):
        assert self._state.get("current") == GLORGRIXVAL, \
            f"prelspalk.glorgrixval: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glorgrixval', 2:
                self._state["current"] = TRENCLULSKIXT
                self._state["trig"]    = "hint:2"
            case 'glorgrixval', 0:
                self._state["current"] = GLALSPELKREXK
                self._state["trig"]    = "hint:0"
            case 'glorgrixval', _:
                self._state["current"] = SKEXSPART
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glorgrixval', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glorgrixval',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glorgrixval->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skexspart(self, hint):
        assert self._state.get("current") == SKEXSPART, \
            f"prelspalk.skexspart: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skexspart', 2:
                self._state["current"] = TRENCLULSKIXT
                self._state["trig"]    = "hint:2"
            case 'skexspart', _:
                self._state["current"] = GLALSPELKREXK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skexspart', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skexspart',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skexspart->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glalspelkrexk(self, hint):
        assert self._state.get("current") == GLALSPELKREXK, \
            f"prelspalk.glalspelkrexk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glalspelkrexk', 2:
                self._state["current"] = TRENCLULSKIXT
                self._state["trig"]    = "hint:2"
            case 'glalspelkrexk', 1:
                self._state["current"] = CLARBRAXSPUL
                self._state["trig"]    = "hint:1"
            case 'glalspelkrexk', _:
                self._state["current"] = BREXBRORGRONK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glalspelkrexk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glalspelkrexk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glalspelkrexk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brexbrorgronk(self, hint):
        assert self._state.get("current") == BREXBRORGRONK, \
            f"prelspalk.brexbrorgronk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brexbrorgronk', 2:
                self._state["current"] = TRENCLULSKIXT
                self._state["trig"]    = "hint:2"
            case 'brexbrorgronk', 0:
                self._state["current"] = BRORSTIXFLANT
                self._state["trig"]    = "hint:0"
            case 'brexbrorgronk', _:
                self._state["current"] = CLARBRAXSPUL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brexbrorgronk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brexbrorgronk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brexbrorgronk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _clarbraxspul(self, hint):
        assert self._state.get("current") == CLARBRAXSPUL, \
            f"prelspalk.clarbraxspul: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'clarbraxspul', 2:
                self._state["current"] = TRENCLULSKIXT
                self._state["trig"]    = "hint:2"
            case 'clarbraxspul', 0:
                self._state["current"] = BRORSTIXFLANT
                self._state["trig"]    = "hint:0"
            case 'clarbraxspul', _:
                self._state["current"] = BLIXSLIXX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'clarbraxspul', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'clarbraxspul',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"clarbraxspul->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blixslixx(self, hint):
        assert self._state.get("current") == BLIXSLIXX, \
            f"prelspalk.blixslixx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blixslixx', 2:
                self._state["current"] = TRENCLULSKIXT
                self._state["trig"]    = "hint:2"
            case 'blixslixx', _:
                self._state["current"] = BLAXTRULSPOR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blixslixx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blixslixx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blixslixx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blaxtrulspor(self, hint):
        assert self._state.get("current") == BLAXTRULSPOR, \
            f"prelspalk.blaxtrulspor: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blaxtrulspor', 2:
                self._state["current"] = TRENCLULSKIXT
                self._state["trig"]    = "hint:2"
            case 'blaxtrulspor', 0:
                self._state["current"] = BRORSTIXFLANT
                self._state["trig"]    = "hint:0"
            case 'blaxtrulspor', _:
                self._state["current"] = STEXDRORGLELN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blaxtrulspor', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blaxtrulspor',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blaxtrulspor->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _stexdrorgleln(self, hint):
        assert self._state.get("current") == STEXDRORGLELN, \
            f"prelspalk.stexdrorgleln: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'stexdrorgleln', 2:
                self._state["current"] = TRENCLULSKIXT
                self._state["trig"]    = "hint:2"
            case 'stexdrorgleln', 1:
                self._state["current"] = BRORSTIXFLANT
                self._state["trig"]    = "hint:1"
            case 'stexdrorgleln', _:
                self._state["current"] = BLIMVARFLIMR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'stexdrorgleln', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'stexdrorgleln',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"stexdrorgleln->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blimvarflimr(self, hint):
        assert self._state.get("current") == BLIMVARFLIMR, \
            f"prelspalk.blimvarflimr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blimvarflimr', 2:
                self._state["current"] = TRENCLULSKIXT
                self._state["trig"]    = "hint:2"
            case 'blimvarflimr', 0:
                self._state["current"] = BRORSTIXFLANT
                self._state["trig"]    = "hint:0"
            case 'blimvarflimr', _:
                self._state["current"] = TRULGRURBRENT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blimvarflimr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blimvarflimr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blimvarflimr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _trulgrurbrent(self, hint):
        assert self._state.get("current") == TRULGRURBRENT, \
            f"prelspalk.trulgrurbrent: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'trulgrurbrent', 2:
                self._state["current"] = TRENCLULSKIXT
                self._state["trig"]    = "hint:2"
            case 'trulgrurbrent', 1:
                self._state["current"] = SKEXFLEXPREL
                self._state["trig"]    = "hint:1"
            case 'trulgrurbrent', _:
                self._state["current"] = BRIXSTALT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'trulgrurbrent', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'trulgrurbrent',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"trulgrurbrent->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brixstalt(self, hint):
        assert self._state.get("current") == BRIXSTALT, \
            f"prelspalk.brixstalt: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brixstalt', 2:
                self._state["current"] = TRENCLULSKIXT
                self._state["trig"]    = "hint:2"
            case 'brixstalt', _:
                self._state["current"] = SKEXFLEXPREL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brixstalt', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brixstalt',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brixstalt->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skexflexprel(self, hint):
        assert self._state.get("current") == SKEXFLEXPREL, \
            f"prelspalk.skexflexprel: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skexflexprel', 2:
                self._state["current"] = TRENCLULSKIXT
                self._state["trig"]    = "hint:2"
            case 'skexflexprel', _:
                self._state["current"] = DRELDRENX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skexflexprel', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skexflexprel',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skexflexprel->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _dreldrenx(self, hint):
        assert self._state.get("current") == DRELDRENX, \
            f"prelspalk.dreldrenx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'dreldrenx', 2:
                self._state["current"] = TRENCLULSKIXT
                self._state["trig"]    = "hint:2"
            case 'dreldrenx', _:
                self._state["current"] = BLALGRAXSTON
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'dreldrenx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'dreldrenx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"dreldrenx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blalgraxston(self, hint):
        assert self._state.get("current") == BLALGRAXSTON, \
            f"prelspalk.blalgraxston: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blalgraxston', 2:
                self._state["current"] = TRENCLULSKIXT
                self._state["trig"]    = "hint:2"
            case 'blalgraxston', _:
                self._state["current"] = BLONSPORSKUR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blalgraxston', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blalgraxston',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blalgraxston->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blonsporskur(self, hint):
        assert self._state.get("current") == BLONSPORSKUR, \
            f"prelspalk.blonsporskur: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blonsporskur', 2:
                self._state["current"] = TRENCLULSKIXT
                self._state["trig"]    = "hint:2"
            case 'blonsporskur', 0:
                self._state["current"] = BRORSTIXFLANT
                self._state["trig"]    = "hint:0"
            case 'blonsporskur', _:
                self._state["current"] = VURSTAXSKEN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blonsporskur', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blonsporskur',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blonsporskur->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _vurstaxsken(self, hint):
        assert self._state.get("current") == VURSTAXSKEN, \
            f"prelspalk.vurstaxsken: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'vurstaxsken', 2:
                self._state["current"] = TRENCLULSKIXT
                self._state["trig"]    = "hint:2"
            case 'vurstaxsken', _:
                self._state["current"] = TROSSPURPRANN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'vurstaxsken', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'vurstaxsken',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"vurstaxsken->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _trosspurprann(self, hint):
        assert self._state.get("current") == TROSSPURPRANN, \
            f"prelspalk.trosspurprann: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'trosspurprann', 2:
                self._state["current"] = TRENCLULSKIXT
                self._state["trig"]    = "hint:2"
            case 'trosspurprann', _:
                self._state["current"] = SKULBLIX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'trosspurprann', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'trosspurprann',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"trosspurprann->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skulblix(self, hint):
        assert self._state.get("current") == SKULBLIX, \
            f"prelspalk.skulblix: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skulblix', 2:
                self._state["current"] = TRENCLULSKIXT
                self._state["trig"]    = "hint:2"
            case 'skulblix', _:
                self._state["current"] = BRIXFLIM
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skulblix', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skulblix',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skulblix->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brixflim(self, hint):
        assert self._state.get("current") == BRIXFLIM, \
            f"prelspalk.brixflim: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brixflim', 2:
                self._state["current"] = TRENCLULSKIXT
                self._state["trig"]    = "hint:2"
            case 'brixflim', _:
                self._state["current"] = CLOSBRENGLELX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brixflim', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brixflim',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brixflim->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _closbrenglelx(self, hint):
        assert self._state.get("current") == CLOSBRENGLELX, \
            f"prelspalk.closbrenglelx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'closbrenglelx', 2:
                self._state["current"] = TRENCLULSKIXT
                self._state["trig"]    = "hint:2"
            case 'closbrenglelx', _:
                self._state["current"] = GLONTRIXBRAR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'closbrenglelx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'closbrenglelx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"closbrenglelx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glontrixbrar(self, hint):
        assert self._state.get("current") == GLONTRIXBRAR, \
            f"prelspalk.glontrixbrar: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glontrixbrar', 2:
                self._state["current"] = TRENCLULSKIXT
                self._state["trig"]    = "hint:2"
            case 'glontrixbrar', 1:
                self._state["current"] = BRORSTIXFLANT
                self._state["trig"]    = "hint:1"
            case 'glontrixbrar', _:
                self._state["current"] = GRORSPOSK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glontrixbrar', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glontrixbrar',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glontrixbrar->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _grorsposk(self, hint):
        assert self._state.get("current") == GRORSPOSK, \
            f"prelspalk.grorsposk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'grorsposk', 2:
                self._state["current"] = TRENCLULSKIXT
                self._state["trig"]    = "hint:2"
            case 'grorsposk', 0:
                self._state["current"] = BRORSTIXFLANT
                self._state["trig"]    = "hint:0"
            case 'grorsposk', _:
                self._state["current"] = BRURPROSX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'grorsposk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'grorsposk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"grorsposk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brurprosx(self, hint):
        assert self._state.get("current") == BRURPROSX, \
            f"prelspalk.brurprosx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brurprosx', 2:
                self._state["current"] = TRENCLULSKIXT
                self._state["trig"]    = "hint:2"
            case 'brurprosx', 0:
                self._state["current"] = GRIMVIMGLAN
                self._state["trig"]    = "hint:0"
            case 'brurprosx', _:
                self._state["current"] = TRALGLULGLUR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brurprosx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brurprosx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brurprosx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _tralglulglur(self, hint):
        assert self._state.get("current") == TRALGLULGLUR, \
            f"prelspalk.tralglulglur: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'tralglulglur', 2:
                self._state["current"] = TRENCLULSKIXT
                self._state["trig"]    = "hint:2"
            case 'tralglulglur', 0:
                self._state["current"] = BRORSTIXFLANT
                self._state["trig"]    = "hint:0"
            case 'tralglulglur', _:
                self._state["current"] = GRIMVIMGLAN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'tralglulglur', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'tralglulglur',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"tralglulglur->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _grimvimglan(self, hint):
        assert self._state.get("current") == GRIMVIMGLAN, \
            f"prelspalk.grimvimglan: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'grimvimglan', 2:
                self._state["current"] = TRENCLULSKIXT
                self._state["trig"]    = "hint:2"
            case 'grimvimglan', 1:
                self._state["current"] = TRIXTRELFLULT
                self._state["trig"]    = "hint:1"
            case 'grimvimglan', _:
                self._state["current"] = GRIMPRUR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'grimvimglan', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'grimvimglan',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"grimvimglan->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _grimprur(self, hint):
        assert self._state.get("current") == GRIMPRUR, \
            f"prelspalk.grimprur: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'grimprur', 2:
                self._state["current"] = TRENCLULSKIXT
                self._state["trig"]    = "hint:2"
            case 'grimprur', _:
                self._state["current"] = TRIXTRELFLULT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'grimprur', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'grimprur',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"grimprur->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _trixtrelflult(self, hint):
        assert self._state.get("current") == TRIXTRELFLULT, \
            f"prelspalk.trixtrelflult: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'trixtrelflult', 2:
                self._state["current"] = TRENCLULSKIXT
                self._state["trig"]    = "hint:2"
            case 'trixtrelflult', 1:
                self._state["current"] = BRORSTIXFLANT
                self._state["trig"]    = "hint:1"
            case 'trixtrelflult', _:
                self._state["current"] = SPARPRAXDRORN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'trixtrelflult', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'trixtrelflult',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"trixtrelflult->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _sparpraxdrorn(self, hint):
        assert self._state.get("current") == SPARPRAXDRORN, \
            f"prelspalk.sparpraxdrorn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'sparpraxdrorn', 2:
                self._state["current"] = TRENCLULSKIXT
                self._state["trig"]    = "hint:2"
            case 'sparpraxdrorn', 0:
                self._state["current"] = BRORSTIXFLANT
                self._state["trig"]    = "hint:0"
            case 'sparpraxdrorn', _:
                self._state["current"] = VOSCLIMX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'sparpraxdrorn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'sparpraxdrorn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"sparpraxdrorn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _vosclimx(self, hint):
        assert self._state.get("current") == VOSCLIMX, \
            f"prelspalk.vosclimx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'vosclimx', 2:
                self._state["current"] = TRENCLULSKIXT
                self._state["trig"]    = "hint:2"
            case 'vosclimx', 0:
                self._state["current"] = BRANGREXL
                self._state["trig"]    = "hint:0"
            case 'vosclimx', _:
                self._state["current"] = DRULSTIXK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'vosclimx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'vosclimx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"vosclimx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _drulstixk(self, hint):
        assert self._state.get("current") == DRULSTIXK, \
            f"prelspalk.drulstixk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'drulstixk', 2:
                self._state["current"] = TRENCLULSKIXT
                self._state["trig"]    = "hint:2"
            case 'drulstixk', _:
                self._state["current"] = BRANGREXL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'drulstixk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'drulstixk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"drulstixk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brangrexl(self, hint):
        assert self._state.get("current") == BRANGREXL, \
            f"prelspalk.brangrexl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brangrexl', 2:
                self._state["current"] = TRENCLULSKIXT
                self._state["trig"]    = "hint:2"
            case 'brangrexl', _:
                self._state["current"] = TRORDRORFLULT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brangrexl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brangrexl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brangrexl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _trordrorflult(self, hint):
        assert self._state.get("current") == TRORDRORFLULT, \
            f"prelspalk.trordrorflult: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'trordrorflult', 2:
                self._state["current"] = TRENCLULSKIXT
                self._state["trig"]    = "hint:2"
            case 'trordrorflult', _:
                self._state["current"] = SLOSBLORSKIXK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'trordrorflult', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'trordrorflult',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"trordrorflult->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slosblorskixk(self, hint):
        assert self._state.get("current") == SLOSBLORSKIXK, \
            f"prelspalk.slosblorskixk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slosblorskixk', 2:
                self._state["current"] = TRENCLULSKIXT
                self._state["trig"]    = "hint:2"
            case 'slosblorskixk', _:
                self._state["current"] = KRIMSPAXSPIXK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slosblorskixk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slosblorskixk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slosblorskixk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _krimspaxspixk(self, hint):
        assert self._state.get("current") == KRIMSPAXSPIXK, \
            f"prelspalk.krimspaxspixk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'krimspaxspixk', 2:
                self._state["current"] = TRENCLULSKIXT
                self._state["trig"]    = "hint:2"
            case 'krimspaxspixk', 1:
                self._state["current"] = BRORSTIXFLANT
                self._state["trig"]    = "hint:1"
            case 'krimspaxspixk', _:
                self._state["current"] = STIXVORBREL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'krimspaxspixk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'krimspaxspixk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"krimspaxspixk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _stixvorbrel(self, hint):
        assert self._state.get("current") == STIXVORBREL, \
            f"prelspalk.stixvorbrel: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'stixvorbrel', 2:
                self._state["current"] = TRENCLULSKIXT
                self._state["trig"]    = "hint:2"
            case 'stixvorbrel', _:
                self._state["current"] = FLENSLIM
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'stixvorbrel', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'stixvorbrel',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"stixvorbrel->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _flenslim(self, hint):
        assert self._state.get("current") == FLENSLIM, \
            f"prelspalk.flenslim: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'flenslim', 2:
                self._state["current"] = TRENCLULSKIXT
                self._state["trig"]    = "hint:2"
            case 'flenslim', _:
                self._state["current"] = BRIMVONDRAX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'flenslim', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'flenslim',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"flenslim->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brimvondrax(self, hint):
        assert self._state.get("current") == BRIMVONDRAX, \
            f"prelspalk.brimvondrax: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brimvondrax', 2:
                self._state["current"] = TRENCLULSKIXT
                self._state["trig"]    = "hint:2"
            case 'brimvondrax', _:
                self._state["current"] = GRONSKONGLAXX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brimvondrax', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brimvondrax',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brimvondrax->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _gronskonglaxx(self, hint):
        assert self._state.get("current") == GRONSKONGLAXX, \
            f"prelspalk.gronskonglaxx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'gronskonglaxx', 2:
                self._state["current"] = TRENCLULSKIXT
                self._state["trig"]    = "hint:2"
            case 'gronskonglaxx', _:
                self._state["current"] = BLORSLIMCLULK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'gronskonglaxx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'gronskonglaxx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"gronskonglaxx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blorslimclulk(self, hint):
        assert self._state.get("current") == BLORSLIMCLULK, \
            f"prelspalk.blorslimclulk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blorslimclulk', 2:
                self._state["current"] = TRENCLULSKIXT
                self._state["trig"]    = "hint:2"
            case 'blorslimclulk', _:
                self._state["current"] = CLIMDRUL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blorslimclulk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blorslimclulk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blorslimclulk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _climdrul(self, hint):
        assert self._state.get("current") == CLIMDRUL, \
            f"prelspalk.climdrul: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'climdrul', 2:
                self._state["current"] = TRENCLULSKIXT
                self._state["trig"]    = "hint:2"
            case 'climdrul', 0:
                self._state["current"] = PRELCLONCLIX
                self._state["trig"]    = "hint:0"
            case 'climdrul', _:
                self._state["current"] = BLOSKRAX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'climdrul', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'climdrul',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"climdrul->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _bloskrax(self, hint):
        assert self._state.get("current") == BLOSKRAX, \
            f"prelspalk.bloskrax: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'bloskrax', 2:
                self._state["current"] = TRENCLULSKIXT
                self._state["trig"]    = "hint:2"
            case 'bloskrax', _:
                self._state["current"] = PRELCLONCLIX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'bloskrax', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'bloskrax',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"bloskrax->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _prelclonclix(self, hint):
        assert self._state.get("current") == PRELCLONCLIX, \
            f"prelspalk.prelclonclix: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'prelclonclix', 2:
                self._state["current"] = TRENCLULSKIXT
                self._state["trig"]    = "hint:2"
            case 'prelclonclix', 0:
                self._state["current"] = BRORSTIXFLANT
                self._state["trig"]    = "hint:0"
            case 'prelclonclix', _:
                self._state["current"] = GLEXDRENDRURL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'prelclonclix', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'prelclonclix',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"prelclonclix->{_to}", _xid_val)
        self._state["cycle"] += 1

    def invoke(self, hint=None, span=None, caller=None, ctx=None, cycle=0):
        if ctx is None: ctx = {}

        self._state = {"current": FLENSPIXDRELK, "ctx": ctx,
                        "span": span, "caller": caller,
                        "trig": "auto", "cycle": cycle}
        _dispatch = {
            FLENSPIXDRELK: self._flenspixdrelk,
            SPURSKIX: self._spurskix,
            PREXSTENK: self._prexstenk,
            KRIXKRURVANN: self._krixkrurvann,
            FLALGLENSTIM: self._flalglenstim,
            KRARSTIML: self._krarstiml,
            FLIMPRALX: self._flimpralx,
            TRENBLIX: self._trenblix,
            GLELGRIX: self._glelgrix,
            SPONGROSSPIM: self._spongrosspim,
            TRENKRELBRUR: self._trenkrelbrur,
            BLANPRIXCLIXX: self._blanprixclixx,
            BRONGLOSK: self._bronglosk,
            BLULKROSVENL: self._blulkrosvenl,
            FLELKRAXK: self._flelkraxk,
            VANBLIXSTORL: self._vanblixstorl,
            GROSFLIXT: self._grosflixt,
            SKAXSLELK: self._skaxslelk,
            TRALGLELX: self._tralglelx,
            BRIXGRURGRALN: self._brixgrurgraln,
            SLONDRELKROR: self._slondrelkror,
            FLULCLENR: self._flulclenr,
            SLANGLIM: self._slanglim,
            GLORGRIXVAL: self._glorgrixval,
            SKEXSPART: self._skexspart,
            GLALSPELKREXK: self._glalspelkrexk,
            BREXBRORGRONK: self._brexbrorgronk,
            CLARBRAXSPUL: self._clarbraxspul,
            BLIXSLIXX: self._blixslixx,
            BLAXTRULSPOR: self._blaxtrulspor,
            STEXDRORGLELN: self._stexdrorgleln,
            BLIMVARFLIMR: self._blimvarflimr,
            TRULGRURBRENT: self._trulgrurbrent,
            BRIXSTALT: self._brixstalt,
            SKEXFLEXPREL: self._skexflexprel,
            DRELDRENX: self._dreldrenx,
            BLALGRAXSTON: self._blalgraxston,
            BLONSPORSKUR: self._blonsporskur,
            VURSTAXSKEN: self._vurstaxsken,
            TROSSPURPRANN: self._trosspurprann,
            SKULBLIX: self._skulblix,
            BRIXFLIM: self._brixflim,
            CLOSBRENGLELX: self._closbrenglelx,
            GLONTRIXBRAR: self._glontrixbrar,
            GRORSPOSK: self._grorsposk,
            BRURPROSX: self._brurprosx,
            TRALGLULGLUR: self._tralglulglur,
            GRIMVIMGLAN: self._grimvimglan,
            GRIMPRUR: self._grimprur,
            TRIXTRELFLULT: self._trixtrelflult,
            SPARPRAXDRORN: self._sparpraxdrorn,
            VOSCLIMX: self._vosclimx,
            DRULSTIXK: self._drulstixk,
            BRANGREXL: self._brangrexl,
            TRORDRORFLULT: self._trordrorflult,
            SLOSBLORSKIXK: self._slosblorskixk,
            KRIMSPAXSPIXK: self._krimspaxspixk,
            STIXVORBREL: self._stixvorbrel,
            FLENSLIM: self._flenslim,
            BRIMVONDRAX: self._brimvondrax,
            GRONSKONGLAXX: self._gronskonglaxx,
            BLORSLIMCLULK: self._blorslimclulk,
            CLIMDRUL: self._climdrul,
            BLOSKRAX: self._bloskrax,
            PRELCLONCLIX: self._prelclonclix,
        }
        while self._state["current"] not in _R and self._state["cycle"] - cycle < 8000:
            _dispatch[self._state["current"]](hint)
        _ret     = _R.get(self._state["current"], -1)
        _is_err  = self._state["current"] == TRENCLULSKIXT
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
    return PrelspalkFSM().invoke(hint=hint, span=span, caller=caller, ctx=ctx, cycle=cycle)
