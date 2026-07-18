from _log import _w as _emit, _xid

STAXDRAX = 'staxdrax'
FLORTRURSLOSX = 'flortrurslosx'
CLENFLALCLENR = 'clenflalclenr'
TRULBRANSLEXR = 'trulbranslexr'
GLORSPAX = 'glorspax'
KRIMFLIMSLAXR = 'krimflimslaxr'
TRALVAR = 'tralvar'
SKANDRANSTOS = 'skandranstos'
GRIMDROSR = 'grimdrosr'
SKANDRONSPALK = 'skandronspalk'
CLIXFLOR = 'clixflor'
KRIXSLALPROSK = 'krixslalprosk'
CLANGLARSPONT = 'clanglarspont'
KRIMSLELX = 'krimslelx'
DRARVOSR = 'drarvosr'
SLELSTULX = 'slelstulx'
SKOSFLAX = 'skosflax'
SKALSPELTROR = 'skalspeltror'
KROSCLALN = 'krosclaln'
BRARSTAX = 'brarstax'
GRALSTULTRON = 'gralstultron'
TROSTRORVAXN = 'trostrorvaxn'
VIMSTANPRAL = 'vimstanpral'
VENKRARSLONT = 'venkrarslont'
GREXSKOSL = 'grexskosl'
FLELKRALKREN = 'flelkralkren'
BRONSKURKRAX = 'bronskurkrax'
SLULDROSPRARR = 'sluldrosprarr'
SPONSLEX = 'sponslex'
KRONGRIMSPEN = 'krongrimspen'
DRANVOSCLORK = 'dranvosclork'
BRALBREN = 'bralbren'
DRORCLUL = 'drorclul'
SLELVIMSTELK = 'slelvimstelk'
BRURGRIM = 'brurgrim'
SLORGREL = 'slorgrel'
KRALSPEXBLIXR = 'kralspexblixr'
BLIXCLORTROSX = 'blixclortrosx'
SPANPRALT = 'spanpralt'
SLANGRURN = 'slangrurn'
GRORPRON = 'grorpron'
BLOSBLIMSKARL = 'blosblimskarl'
GLELBRUL = 'glelbrul'
SPELKRURT = 'spelkrurt'
BRIXVIMT = 'brixvimt'
SKAXSLOSK = 'skaxslosk'
DROSSKORSTELX = 'drosskorstelx'
TRIMVEXCLEL = 'trimvexclel'
PRANVENTRAXT = 'pranventraxt'
BLEXSKONK = 'blexskonk'
BLARDRUR = 'blardrur'
GRELTRIM = 'greltrim'
SLEXBRORT = 'slexbrort'
VARFLIX = 'varflix'
BRAXGLOSSLIXT = 'braxglosslixt'
GLURGLIXR = 'glurglixr'
FLARVUL = 'flarvul'
TRONTREXR = 'trontrexr'
SLIMSLENL = 'slimslenl'
SLANBLIXDRIMR = 'slanblixdrimr'
GLANSKONT = 'glanskont'
VORBRORL = 'vorbrorl'
SPALSLIXSTOR = 'spalslixstor'
PRELPRELDRAX = 'prelpreldrax'
BRONCLOSX = 'bronclosx'
CLAXGRURFLAX = 'claxgrurflax'
FLAXGRONT = 'flaxgront'
GRULCLIMT = 'grulclimt'

_R = {
    CLAXGRURFLAX: 0,
    FLAXGRONT: 1,
    GRULCLIMT: 2,
}

_CTX_READS_KEY = 'flurslex'
_CTX_THRESHOLD = 16

class GrixprarkFSM:
    def __init__(self):
        self._state = {}

    def _staxdrax(self, hint):
        assert self._state.get("current") == STAXDRAX, \
            f"grixprark.staxdrax: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'staxdrax', 2:
                self._state["current"] = GRULCLIMT
                self._state["trig"]    = "hint:2"
            case 'staxdrax', 0:
                self._state["current"] = CLENFLALCLENR
                self._state["trig"]    = "hint:0"
            case 'staxdrax', _:
                self._state["current"] = FLORTRURSLOSX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'staxdrax', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'staxdrax',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"staxdrax->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _flortrurslosx(self, hint):
        assert self._state.get("current") == FLORTRURSLOSX, \
            f"grixprark.flortrurslosx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'flortrurslosx', 2:
                self._state["current"] = GRULCLIMT
                self._state["trig"]    = "hint:2"
            case 'flortrurslosx', 0:
                self._state["current"] = TRULBRANSLEXR
                self._state["trig"]    = "hint:0"
            case 'flortrurslosx', _:
                self._state["current"] = CLENFLALCLENR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'flortrurslosx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'flortrurslosx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"flortrurslosx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _clenflalclenr(self, hint):
        assert self._state.get("current") == CLENFLALCLENR, \
            f"grixprark.clenflalclenr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'clenflalclenr', 2:
                self._state["current"] = GRULCLIMT
                self._state["trig"]    = "hint:2"
            case 'clenflalclenr', 0:
                self._state["current"] = GLORSPAX
                self._state["trig"]    = "hint:0"
            case 'clenflalclenr', _:
                self._state["current"] = TRULBRANSLEXR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'clenflalclenr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'clenflalclenr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"clenflalclenr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _trulbranslexr(self, hint):
        assert self._state.get("current") == TRULBRANSLEXR, \
            f"grixprark.trulbranslexr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'trulbranslexr', 2:
                self._state["current"] = GRULCLIMT
                self._state["trig"]    = "hint:2"
            case 'trulbranslexr', _:
                self._state["current"] = GLORSPAX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'trulbranslexr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'trulbranslexr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"trulbranslexr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glorspax(self, hint):
        assert self._state.get("current") == GLORSPAX, \
            f"grixprark.glorspax: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glorspax', 2:
                self._state["current"] = GRULCLIMT
                self._state["trig"]    = "hint:2"
            case 'glorspax', _:
                self._state["current"] = KRIMFLIMSLAXR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glorspax', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glorspax',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glorspax->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _krimflimslaxr(self, hint):
        assert self._state.get("current") == KRIMFLIMSLAXR, \
            f"grixprark.krimflimslaxr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'krimflimslaxr', 2:
                self._state["current"] = GRULCLIMT
                self._state["trig"]    = "hint:2"
            case 'krimflimslaxr', _:
                self._state["current"] = TRALVAR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'krimflimslaxr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'krimflimslaxr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"krimflimslaxr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _tralvar(self, hint):
        assert self._state.get("current") == TRALVAR, \
            f"grixprark.tralvar: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'tralvar', 2:
                self._state["current"] = GRULCLIMT
                self._state["trig"]    = "hint:2"
            case 'tralvar', 0:
                self._state["current"] = GRIMDROSR
                self._state["trig"]    = "hint:0"
            case 'tralvar', _:
                self._state["current"] = SKANDRANSTOS
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'tralvar', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'tralvar',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"tralvar->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skandranstos(self, hint):
        assert self._state.get("current") == SKANDRANSTOS, \
            f"grixprark.skandranstos: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skandranstos', 2:
                self._state["current"] = GRULCLIMT
                self._state["trig"]    = "hint:2"
            case 'skandranstos', 0:
                self._state["current"] = FLAXGRONT
                self._state["trig"]    = "hint:0"
            case 'skandranstos', _:
                self._state["current"] = GRIMDROSR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skandranstos', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skandranstos',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skandranstos->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _grimdrosr(self, hint):
        assert self._state.get("current") == GRIMDROSR, \
            f"grixprark.grimdrosr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'grimdrosr', 2:
                self._state["current"] = GRULCLIMT
                self._state["trig"]    = "hint:2"
            case 'grimdrosr', 1:
                self._state["current"] = FLAXGRONT
                self._state["trig"]    = "hint:1"
            case 'grimdrosr', _:
                self._state["current"] = SKANDRONSPALK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'grimdrosr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'grimdrosr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"grimdrosr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skandronspalk(self, hint):
        assert self._state.get("current") == SKANDRONSPALK, \
            f"grixprark.skandronspalk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skandronspalk', 2:
                self._state["current"] = GRULCLIMT
                self._state["trig"]    = "hint:2"
            case 'skandronspalk', _:
                self._state["current"] = CLIXFLOR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skandronspalk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skandronspalk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skandronspalk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _clixflor(self, hint):
        assert self._state.get("current") == CLIXFLOR, \
            f"grixprark.clixflor: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'clixflor', 2:
                self._state["current"] = GRULCLIMT
                self._state["trig"]    = "hint:2"
            case 'clixflor', 1:
                self._state["current"] = FLAXGRONT
                self._state["trig"]    = "hint:1"
            case 'clixflor', _:
                self._state["current"] = KRIXSLALPROSK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'clixflor', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'clixflor',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"clixflor->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _krixslalprosk(self, hint):
        assert self._state.get("current") == KRIXSLALPROSK, \
            f"grixprark.krixslalprosk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'krixslalprosk', 2:
                self._state["current"] = GRULCLIMT
                self._state["trig"]    = "hint:2"
            case 'krixslalprosk', 1:
                self._state["current"] = FLAXGRONT
                self._state["trig"]    = "hint:1"
            case 'krixslalprosk', _:
                self._state["current"] = CLANGLARSPONT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'krixslalprosk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'krixslalprosk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"krixslalprosk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _clanglarspont(self, hint):
        assert self._state.get("current") == CLANGLARSPONT, \
            f"grixprark.clanglarspont: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'clanglarspont', 2:
                self._state["current"] = GRULCLIMT
                self._state["trig"]    = "hint:2"
            case 'clanglarspont', 0:
                self._state["current"] = DRARVOSR
                self._state["trig"]    = "hint:0"
            case 'clanglarspont', _:
                self._state["current"] = KRIMSLELX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'clanglarspont', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'clanglarspont',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"clanglarspont->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _krimslelx(self, hint):
        assert self._state.get("current") == KRIMSLELX, \
            f"grixprark.krimslelx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'krimslelx', 2:
                self._state["current"] = GRULCLIMT
                self._state["trig"]    = "hint:2"
            case 'krimslelx', 1:
                self._state["current"] = SLELSTULX
                self._state["trig"]    = "hint:1"
            case 'krimslelx', _:
                self._state["current"] = DRARVOSR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'krimslelx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'krimslelx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"krimslelx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _drarvosr(self, hint):
        assert self._state.get("current") == DRARVOSR, \
            f"grixprark.drarvosr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'drarvosr', 2:
                self._state["current"] = GRULCLIMT
                self._state["trig"]    = "hint:2"
            case 'drarvosr', _:
                self._state["current"] = SLELSTULX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'drarvosr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'drarvosr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"drarvosr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slelstulx(self, hint):
        assert self._state.get("current") == SLELSTULX, \
            f"grixprark.slelstulx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slelstulx', 2:
                self._state["current"] = GRULCLIMT
                self._state["trig"]    = "hint:2"
            case 'slelstulx', 1:
                self._state["current"] = SKALSPELTROR
                self._state["trig"]    = "hint:1"
            case 'slelstulx', _:
                self._state["current"] = SKOSFLAX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slelstulx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slelstulx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slelstulx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skosflax(self, hint):
        assert self._state.get("current") == SKOSFLAX, \
            f"grixprark.skosflax: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skosflax', 2:
                self._state["current"] = GRULCLIMT
                self._state["trig"]    = "hint:2"
            case 'skosflax', _:
                self._state["current"] = SKALSPELTROR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skosflax', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skosflax',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skosflax->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skalspeltror(self, hint):
        assert self._state.get("current") == SKALSPELTROR, \
            f"grixprark.skalspeltror: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skalspeltror', 2:
                self._state["current"] = GRULCLIMT
                self._state["trig"]    = "hint:2"
            case 'skalspeltror', _:
                self._state["current"] = KROSCLALN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skalspeltror', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skalspeltror',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skalspeltror->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _krosclaln(self, hint):
        assert self._state.get("current") == KROSCLALN, \
            f"grixprark.krosclaln: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'krosclaln', 2:
                self._state["current"] = GRULCLIMT
                self._state["trig"]    = "hint:2"
            case 'krosclaln', 1:
                self._state["current"] = GRALSTULTRON
                self._state["trig"]    = "hint:1"
            case 'krosclaln', _:
                self._state["current"] = BRARSTAX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'krosclaln', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'krosclaln',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"krosclaln->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brarstax(self, hint):
        assert self._state.get("current") == BRARSTAX, \
            f"grixprark.brarstax: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brarstax', 2:
                self._state["current"] = GRULCLIMT
                self._state["trig"]    = "hint:2"
            case 'brarstax', _:
                self._state["current"] = GRALSTULTRON
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brarstax', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brarstax',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brarstax->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _gralstultron(self, hint):
        assert self._state.get("current") == GRALSTULTRON, \
            f"grixprark.gralstultron: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'gralstultron', 2:
                self._state["current"] = GRULCLIMT
                self._state["trig"]    = "hint:2"
            case 'gralstultron', 1:
                self._state["current"] = FLAXGRONT
                self._state["trig"]    = "hint:1"
            case 'gralstultron', _:
                self._state["current"] = TROSTRORVAXN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'gralstultron', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'gralstultron',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"gralstultron->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _trostrorvaxn(self, hint):
        assert self._state.get("current") == TROSTRORVAXN, \
            f"grixprark.trostrorvaxn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'trostrorvaxn', 2:
                self._state["current"] = GRULCLIMT
                self._state["trig"]    = "hint:2"
            case 'trostrorvaxn', _:
                self._state["current"] = VIMSTANPRAL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'trostrorvaxn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'trostrorvaxn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"trostrorvaxn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _vimstanpral(self, hint):
        assert self._state.get("current") == VIMSTANPRAL, \
            f"grixprark.vimstanpral: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'vimstanpral', 2:
                self._state["current"] = GRULCLIMT
                self._state["trig"]    = "hint:2"
            case 'vimstanpral', _:
                self._state["current"] = VENKRARSLONT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'vimstanpral', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'vimstanpral',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"vimstanpral->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _venkrarslont(self, hint):
        assert self._state.get("current") == VENKRARSLONT, \
            f"grixprark.venkrarslont: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'venkrarslont', 2:
                self._state["current"] = GRULCLIMT
                self._state["trig"]    = "hint:2"
            case 'venkrarslont', _:
                self._state["current"] = GREXSKOSL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'venkrarslont', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'venkrarslont',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"venkrarslont->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _grexskosl(self, hint):
        assert self._state.get("current") == GREXSKOSL, \
            f"grixprark.grexskosl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'grexskosl', 2:
                self._state["current"] = GRULCLIMT
                self._state["trig"]    = "hint:2"
            case 'grexskosl', _:
                self._state["current"] = FLELKRALKREN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'grexskosl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'grexskosl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"grexskosl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _flelkralkren(self, hint):
        assert self._state.get("current") == FLELKRALKREN, \
            f"grixprark.flelkralkren: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'flelkralkren', 2:
                self._state["current"] = GRULCLIMT
                self._state["trig"]    = "hint:2"
            case 'flelkralkren', _:
                self._state["current"] = BRONSKURKRAX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'flelkralkren', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'flelkralkren',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"flelkralkren->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _bronskurkrax(self, hint):
        assert self._state.get("current") == BRONSKURKRAX, \
            f"grixprark.bronskurkrax: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'bronskurkrax', 2:
                self._state["current"] = GRULCLIMT
                self._state["trig"]    = "hint:2"
            case 'bronskurkrax', _:
                self._state["current"] = SLULDROSPRARR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'bronskurkrax', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'bronskurkrax',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"bronskurkrax->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _sluldrosprarr(self, hint):
        assert self._state.get("current") == SLULDROSPRARR, \
            f"grixprark.sluldrosprarr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'sluldrosprarr', 2:
                self._state["current"] = GRULCLIMT
                self._state["trig"]    = "hint:2"
            case 'sluldrosprarr', _:
                self._state["current"] = SPONSLEX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'sluldrosprarr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'sluldrosprarr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"sluldrosprarr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _sponslex(self, hint):
        assert self._state.get("current") == SPONSLEX, \
            f"grixprark.sponslex: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'sponslex', 2:
                self._state["current"] = GRULCLIMT
                self._state["trig"]    = "hint:2"
            case 'sponslex', 1:
                self._state["current"] = FLAXGRONT
                self._state["trig"]    = "hint:1"
            case 'sponslex', _:
                self._state["current"] = KRONGRIMSPEN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'sponslex', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'sponslex',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"sponslex->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _krongrimspen(self, hint):
        assert self._state.get("current") == KRONGRIMSPEN, \
            f"grixprark.krongrimspen: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'krongrimspen', 2:
                self._state["current"] = GRULCLIMT
                self._state["trig"]    = "hint:2"
            case 'krongrimspen', _:
                self._state["current"] = DRANVOSCLORK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'krongrimspen', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'krongrimspen',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"krongrimspen->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _dranvosclork(self, hint):
        assert self._state.get("current") == DRANVOSCLORK, \
            f"grixprark.dranvosclork: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'dranvosclork', 2:
                self._state["current"] = GRULCLIMT
                self._state["trig"]    = "hint:2"
            case 'dranvosclork', _:
                self._state["current"] = BRALBREN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'dranvosclork', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'dranvosclork',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"dranvosclork->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _bralbren(self, hint):
        assert self._state.get("current") == BRALBREN, \
            f"grixprark.bralbren: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'bralbren', 2:
                self._state["current"] = GRULCLIMT
                self._state["trig"]    = "hint:2"
            case 'bralbren', _:
                self._state["current"] = DRORCLUL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'bralbren', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'bralbren',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"bralbren->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _drorclul(self, hint):
        assert self._state.get("current") == DRORCLUL, \
            f"grixprark.drorclul: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'drorclul', 2:
                self._state["current"] = GRULCLIMT
                self._state["trig"]    = "hint:2"
            case 'drorclul', 1:
                self._state["current"] = FLAXGRONT
                self._state["trig"]    = "hint:1"
            case 'drorclul', _:
                self._state["current"] = SLELVIMSTELK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'drorclul', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'drorclul',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"drorclul->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slelvimstelk(self, hint):
        assert self._state.get("current") == SLELVIMSTELK, \
            f"grixprark.slelvimstelk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slelvimstelk', 2:
                self._state["current"] = GRULCLIMT
                self._state["trig"]    = "hint:2"
            case 'slelvimstelk', _:
                self._state["current"] = BRURGRIM
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slelvimstelk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slelvimstelk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slelvimstelk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brurgrim(self, hint):
        assert self._state.get("current") == BRURGRIM, \
            f"grixprark.brurgrim: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brurgrim', 2:
                self._state["current"] = GRULCLIMT
                self._state["trig"]    = "hint:2"
            case 'brurgrim', _:
                self._state["current"] = SLORGREL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brurgrim', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brurgrim',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brurgrim->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slorgrel(self, hint):
        assert self._state.get("current") == SLORGREL, \
            f"grixprark.slorgrel: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slorgrel', 2:
                self._state["current"] = GRULCLIMT
                self._state["trig"]    = "hint:2"
            case 'slorgrel', 0:
                self._state["current"] = FLAXGRONT
                self._state["trig"]    = "hint:0"
            case 'slorgrel', _:
                self._state["current"] = KRALSPEXBLIXR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slorgrel', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slorgrel',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slorgrel->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _kralspexblixr(self, hint):
        assert self._state.get("current") == KRALSPEXBLIXR, \
            f"grixprark.kralspexblixr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'kralspexblixr', 2:
                self._state["current"] = GRULCLIMT
                self._state["trig"]    = "hint:2"
            case 'kralspexblixr', _:
                self._state["current"] = BLIXCLORTROSX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'kralspexblixr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'kralspexblixr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"kralspexblixr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blixclortrosx(self, hint):
        assert self._state.get("current") == BLIXCLORTROSX, \
            f"grixprark.blixclortrosx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blixclortrosx', 2:
                self._state["current"] = GRULCLIMT
                self._state["trig"]    = "hint:2"
            case 'blixclortrosx', _:
                self._state["current"] = SPANPRALT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blixclortrosx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blixclortrosx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blixclortrosx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _spanpralt(self, hint):
        assert self._state.get("current") == SPANPRALT, \
            f"grixprark.spanpralt: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'spanpralt', 2:
                self._state["current"] = GRULCLIMT
                self._state["trig"]    = "hint:2"
            case 'spanpralt', 0:
                self._state["current"] = FLAXGRONT
                self._state["trig"]    = "hint:0"
            case 'spanpralt', _:
                self._state["current"] = SLANGRURN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'spanpralt', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'spanpralt',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"spanpralt->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slangrurn(self, hint):
        assert self._state.get("current") == SLANGRURN, \
            f"grixprark.slangrurn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slangrurn', 2:
                self._state["current"] = GRULCLIMT
                self._state["trig"]    = "hint:2"
            case 'slangrurn', 1:
                self._state["current"] = BLOSBLIMSKARL
                self._state["trig"]    = "hint:1"
            case 'slangrurn', _:
                self._state["current"] = GRORPRON
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slangrurn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slangrurn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slangrurn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _grorpron(self, hint):
        assert self._state.get("current") == GRORPRON, \
            f"grixprark.grorpron: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'grorpron', 2:
                self._state["current"] = GRULCLIMT
                self._state["trig"]    = "hint:2"
            case 'grorpron', _:
                self._state["current"] = BLOSBLIMSKARL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'grorpron', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'grorpron',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"grorpron->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blosblimskarl(self, hint):
        assert self._state.get("current") == BLOSBLIMSKARL, \
            f"grixprark.blosblimskarl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blosblimskarl', 2:
                self._state["current"] = GRULCLIMT
                self._state["trig"]    = "hint:2"
            case 'blosblimskarl', 1:
                self._state["current"] = SPELKRURT
                self._state["trig"]    = "hint:1"
            case 'blosblimskarl', _:
                self._state["current"] = GLELBRUL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blosblimskarl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blosblimskarl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blosblimskarl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glelbrul(self, hint):
        assert self._state.get("current") == GLELBRUL, \
            f"grixprark.glelbrul: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glelbrul', 2:
                self._state["current"] = GRULCLIMT
                self._state["trig"]    = "hint:2"
            case 'glelbrul', 1:
                self._state["current"] = FLAXGRONT
                self._state["trig"]    = "hint:1"
            case 'glelbrul', _:
                self._state["current"] = SPELKRURT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glelbrul', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glelbrul',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glelbrul->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _spelkrurt(self, hint):
        assert self._state.get("current") == SPELKRURT, \
            f"grixprark.spelkrurt: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'spelkrurt', 2:
                self._state["current"] = GRULCLIMT
                self._state["trig"]    = "hint:2"
            case 'spelkrurt', _:
                self._state["current"] = BRIXVIMT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'spelkrurt', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'spelkrurt',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"spelkrurt->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brixvimt(self, hint):
        assert self._state.get("current") == BRIXVIMT, \
            f"grixprark.brixvimt: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brixvimt', 2:
                self._state["current"] = GRULCLIMT
                self._state["trig"]    = "hint:2"
            case 'brixvimt', 0:
                self._state["current"] = FLAXGRONT
                self._state["trig"]    = "hint:0"
            case 'brixvimt', _:
                self._state["current"] = SKAXSLOSK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brixvimt', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brixvimt',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brixvimt->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skaxslosk(self, hint):
        assert self._state.get("current") == SKAXSLOSK, \
            f"grixprark.skaxslosk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skaxslosk', 2:
                self._state["current"] = GRULCLIMT
                self._state["trig"]    = "hint:2"
            case 'skaxslosk', 0:
                self._state["current"] = FLAXGRONT
                self._state["trig"]    = "hint:0"
            case 'skaxslosk', _:
                self._state["current"] = DROSSKORSTELX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skaxslosk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skaxslosk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skaxslosk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _drosskorstelx(self, hint):
        assert self._state.get("current") == DROSSKORSTELX, \
            f"grixprark.drosskorstelx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'drosskorstelx', 2:
                self._state["current"] = GRULCLIMT
                self._state["trig"]    = "hint:2"
            case 'drosskorstelx', 0:
                self._state["current"] = FLAXGRONT
                self._state["trig"]    = "hint:0"
            case 'drosskorstelx', _:
                self._state["current"] = TRIMVEXCLEL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'drosskorstelx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'drosskorstelx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"drosskorstelx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _trimvexclel(self, hint):
        assert self._state.get("current") == TRIMVEXCLEL, \
            f"grixprark.trimvexclel: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'trimvexclel', 2:
                self._state["current"] = GRULCLIMT
                self._state["trig"]    = "hint:2"
            case 'trimvexclel', 0:
                self._state["current"] = FLAXGRONT
                self._state["trig"]    = "hint:0"
            case 'trimvexclel', _:
                self._state["current"] = PRANVENTRAXT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'trimvexclel', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'trimvexclel',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"trimvexclel->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _pranventraxt(self, hint):
        assert self._state.get("current") == PRANVENTRAXT, \
            f"grixprark.pranventraxt: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'pranventraxt', 2:
                self._state["current"] = GRULCLIMT
                self._state["trig"]    = "hint:2"
            case 'pranventraxt', _:
                self._state["current"] = BLEXSKONK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'pranventraxt', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'pranventraxt',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"pranventraxt->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blexskonk(self, hint):
        assert self._state.get("current") == BLEXSKONK, \
            f"grixprark.blexskonk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blexskonk', 2:
                self._state["current"] = GRULCLIMT
                self._state["trig"]    = "hint:2"
            case 'blexskonk', _:
                self._state["current"] = BLARDRUR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blexskonk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blexskonk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blexskonk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blardrur(self, hint):
        assert self._state.get("current") == BLARDRUR, \
            f"grixprark.blardrur: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blardrur', 2:
                self._state["current"] = GRULCLIMT
                self._state["trig"]    = "hint:2"
            case 'blardrur', _:
                self._state["current"] = GRELTRIM
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blardrur', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blardrur',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blardrur->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _greltrim(self, hint):
        assert self._state.get("current") == GRELTRIM, \
            f"grixprark.greltrim: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'greltrim', 2:
                self._state["current"] = GRULCLIMT
                self._state["trig"]    = "hint:2"
            case 'greltrim', 1:
                self._state["current"] = FLAXGRONT
                self._state["trig"]    = "hint:1"
            case 'greltrim', _:
                self._state["current"] = SLEXBRORT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'greltrim', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'greltrim',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"greltrim->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slexbrort(self, hint):
        assert self._state.get("current") == SLEXBRORT, \
            f"grixprark.slexbrort: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slexbrort', 2:
                self._state["current"] = GRULCLIMT
                self._state["trig"]    = "hint:2"
            case 'slexbrort', 1:
                self._state["current"] = BRAXGLOSSLIXT
                self._state["trig"]    = "hint:1"
            case 'slexbrort', _:
                self._state["current"] = VARFLIX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slexbrort', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slexbrort',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slexbrort->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _varflix(self, hint):
        assert self._state.get("current") == VARFLIX, \
            f"grixprark.varflix: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'varflix', 2:
                self._state["current"] = GRULCLIMT
                self._state["trig"]    = "hint:2"
            case 'varflix', 0:
                self._state["current"] = GLURGLIXR
                self._state["trig"]    = "hint:0"
            case 'varflix', _:
                self._state["current"] = BRAXGLOSSLIXT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'varflix', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'varflix',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"varflix->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _braxglosslixt(self, hint):
        assert self._state.get("current") == BRAXGLOSSLIXT, \
            f"grixprark.braxglosslixt: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'braxglosslixt', 2:
                self._state["current"] = GRULCLIMT
                self._state["trig"]    = "hint:2"
            case 'braxglosslixt', _:
                self._state["current"] = GLURGLIXR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'braxglosslixt', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'braxglosslixt',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"braxglosslixt->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glurglixr(self, hint):
        assert self._state.get("current") == GLURGLIXR, \
            f"grixprark.glurglixr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glurglixr', 2:
                self._state["current"] = GRULCLIMT
                self._state["trig"]    = "hint:2"
            case 'glurglixr', _:
                self._state["current"] = FLARVUL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glurglixr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glurglixr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glurglixr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _flarvul(self, hint):
        assert self._state.get("current") == FLARVUL, \
            f"grixprark.flarvul: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'flarvul', 2:
                self._state["current"] = GRULCLIMT
                self._state["trig"]    = "hint:2"
            case 'flarvul', 0:
                self._state["current"] = SLIMSLENL
                self._state["trig"]    = "hint:0"
            case 'flarvul', _:
                self._state["current"] = TRONTREXR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'flarvul', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'flarvul',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"flarvul->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _trontrexr(self, hint):
        assert self._state.get("current") == TRONTREXR, \
            f"grixprark.trontrexr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'trontrexr', 2:
                self._state["current"] = GRULCLIMT
                self._state["trig"]    = "hint:2"
            case 'trontrexr', _:
                self._state["current"] = SLIMSLENL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'trontrexr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'trontrexr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"trontrexr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slimslenl(self, hint):
        assert self._state.get("current") == SLIMSLENL, \
            f"grixprark.slimslenl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slimslenl', 2:
                self._state["current"] = GRULCLIMT
                self._state["trig"]    = "hint:2"
            case 'slimslenl', _:
                self._state["current"] = SLANBLIXDRIMR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slimslenl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slimslenl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slimslenl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slanblixdrimr(self, hint):
        assert self._state.get("current") == SLANBLIXDRIMR, \
            f"grixprark.slanblixdrimr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slanblixdrimr', 2:
                self._state["current"] = GRULCLIMT
                self._state["trig"]    = "hint:2"
            case 'slanblixdrimr', _:
                self._state["current"] = GLANSKONT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slanblixdrimr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slanblixdrimr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slanblixdrimr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glanskont(self, hint):
        assert self._state.get("current") == GLANSKONT, \
            f"grixprark.glanskont: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glanskont', 2:
                self._state["current"] = GRULCLIMT
                self._state["trig"]    = "hint:2"
            case 'glanskont', 0:
                self._state["current"] = SPALSLIXSTOR
                self._state["trig"]    = "hint:0"
            case 'glanskont', _:
                self._state["current"] = VORBRORL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glanskont', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glanskont',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glanskont->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _vorbrorl(self, hint):
        assert self._state.get("current") == VORBRORL, \
            f"grixprark.vorbrorl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'vorbrorl', 2:
                self._state["current"] = GRULCLIMT
                self._state["trig"]    = "hint:2"
            case 'vorbrorl', _:
                self._state["current"] = SPALSLIXSTOR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'vorbrorl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'vorbrorl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"vorbrorl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _spalslixstor(self, hint):
        assert self._state.get("current") == SPALSLIXSTOR, \
            f"grixprark.spalslixstor: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'spalslixstor', 2:
                self._state["current"] = GRULCLIMT
                self._state["trig"]    = "hint:2"
            case 'spalslixstor', _:
                self._state["current"] = PRELPRELDRAX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'spalslixstor', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'spalslixstor',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"spalslixstor->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _prelpreldrax(self, hint):
        assert self._state.get("current") == PRELPRELDRAX, \
            f"grixprark.prelpreldrax: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'prelpreldrax', 2:
                self._state["current"] = GRULCLIMT
                self._state["trig"]    = "hint:2"
            case 'prelpreldrax', _:
                self._state["current"] = BRONCLOSX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'prelpreldrax', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'prelpreldrax',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"prelpreldrax->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _bronclosx(self, hint):
        assert self._state.get("current") == BRONCLOSX, \
            f"grixprark.bronclosx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'bronclosx', 2:
                self._state["current"] = GRULCLIMT
                self._state["trig"]    = "hint:2"
            case 'bronclosx', 1:
                self._state["current"] = FLAXGRONT
                self._state["trig"]    = "hint:1"
            case 'bronclosx', _:
                self._state["current"] = CLAXGRURFLAX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'bronclosx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'bronclosx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"bronclosx->{_to}", _xid_val)
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
            _xid_val = _xid(__name__, 'staxdrax', "error", "assert_fail")
            _emit(cycle, 1, __name__, 'staxdrax',
                   {"hint": hint, "span": span, "caller": caller},
                   dict(ctx), _conds,
                   "entry_blocked->error", _xid_val, assertion=_asrt)
            return 2, cycle + 1

        self._state = {"current": STAXDRAX, "ctx": ctx,
                        "span": span, "caller": caller,
                        "trig": "auto", "cycle": cycle}
        _dispatch = {
            STAXDRAX: self._staxdrax,
            FLORTRURSLOSX: self._flortrurslosx,
            CLENFLALCLENR: self._clenflalclenr,
            TRULBRANSLEXR: self._trulbranslexr,
            GLORSPAX: self._glorspax,
            KRIMFLIMSLAXR: self._krimflimslaxr,
            TRALVAR: self._tralvar,
            SKANDRANSTOS: self._skandranstos,
            GRIMDROSR: self._grimdrosr,
            SKANDRONSPALK: self._skandronspalk,
            CLIXFLOR: self._clixflor,
            KRIXSLALPROSK: self._krixslalprosk,
            CLANGLARSPONT: self._clanglarspont,
            KRIMSLELX: self._krimslelx,
            DRARVOSR: self._drarvosr,
            SLELSTULX: self._slelstulx,
            SKOSFLAX: self._skosflax,
            SKALSPELTROR: self._skalspeltror,
            KROSCLALN: self._krosclaln,
            BRARSTAX: self._brarstax,
            GRALSTULTRON: self._gralstultron,
            TROSTRORVAXN: self._trostrorvaxn,
            VIMSTANPRAL: self._vimstanpral,
            VENKRARSLONT: self._venkrarslont,
            GREXSKOSL: self._grexskosl,
            FLELKRALKREN: self._flelkralkren,
            BRONSKURKRAX: self._bronskurkrax,
            SLULDROSPRARR: self._sluldrosprarr,
            SPONSLEX: self._sponslex,
            KRONGRIMSPEN: self._krongrimspen,
            DRANVOSCLORK: self._dranvosclork,
            BRALBREN: self._bralbren,
            DRORCLUL: self._drorclul,
            SLELVIMSTELK: self._slelvimstelk,
            BRURGRIM: self._brurgrim,
            SLORGREL: self._slorgrel,
            KRALSPEXBLIXR: self._kralspexblixr,
            BLIXCLORTROSX: self._blixclortrosx,
            SPANPRALT: self._spanpralt,
            SLANGRURN: self._slangrurn,
            GRORPRON: self._grorpron,
            BLOSBLIMSKARL: self._blosblimskarl,
            GLELBRUL: self._glelbrul,
            SPELKRURT: self._spelkrurt,
            BRIXVIMT: self._brixvimt,
            SKAXSLOSK: self._skaxslosk,
            DROSSKORSTELX: self._drosskorstelx,
            TRIMVEXCLEL: self._trimvexclel,
            PRANVENTRAXT: self._pranventraxt,
            BLEXSKONK: self._blexskonk,
            BLARDRUR: self._blardrur,
            GRELTRIM: self._greltrim,
            SLEXBRORT: self._slexbrort,
            VARFLIX: self._varflix,
            BRAXGLOSSLIXT: self._braxglosslixt,
            GLURGLIXR: self._glurglixr,
            FLARVUL: self._flarvul,
            TRONTREXR: self._trontrexr,
            SLIMSLENL: self._slimslenl,
            SLANBLIXDRIMR: self._slanblixdrimr,
            GLANSKONT: self._glanskont,
            VORBRORL: self._vorbrorl,
            SPALSLIXSTOR: self._spalslixstor,
            PRELPRELDRAX: self._prelpreldrax,
            BRONCLOSX: self._bronclosx,
        }
        while self._state["current"] not in _R and self._state["cycle"] - cycle < 8000:
            _dispatch[self._state["current"]](hint)
        _ret     = _R.get(self._state["current"], -1)
        _is_err  = self._state["current"] == GRULCLIMT
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
    return GrixprarkFSM().invoke(hint=hint, span=span, caller=caller, ctx=ctx, cycle=cycle)
