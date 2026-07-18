from _log import _w as _emit, _xid

SLANSTARTRON = 'slanstartron'
DRANGRIX = 'drangrix'
CLENDRAXTRALT = 'clendraxtralt'
STORSTAR = 'storstar'
DRALCLAL = 'dralclal'
KRANDRELCLIXN = 'krandrelclixn'
STANCLIMBREL = 'stanclimbrel'
BLELTRALT = 'bleltralt'
TROSBRULKRAN = 'trosbrulkran'
PRELGLAX = 'prelglax'
BLURSTANPRAX = 'blurstanprax'
BLONBRURK = 'blonbrurk'
SKIMSKOSK = 'skimskosk'
GLIXCLOSCLANT = 'glixclosclant'
BROSBREXKREN = 'brosbrexkren'
CLEXFLORGRON = 'clexflorgron'
KRIMTRENBREN = 'krimtrenbren'
SKALGLAR = 'skalglar'
GRULDRIMSTORL = 'gruldrimstorl'
BRURFLOSPROR = 'brurflospror'
FLOSPRORSPENK = 'flosprorspenk'
SKURSPOR = 'skurspor'
SKONTREL = 'skontrel'
FLEXVEXT = 'flexvext'
SLEXPRORCLIX = 'slexprorclix'
BRELGRONSKURR = 'brelgronskurr'
BLIMGRONTRON = 'blimgrontron'
BLALPRARK = 'blalprark'
CLANSLUR = 'clanslur'
BRORSLEL = 'brorslel'
BLURTRAXSKIXT = 'blurtraxskixt'
VANVAXX = 'vanvaxx'
DRAXBRELL = 'draxbrell'
VONSPAXGRULL = 'vonspaxgrull'
SPIMSLARPRIM = 'spimslarprim'
VARGRENVAX = 'vargrenvax'
GLEXGLELTRON = 'glexgleltron'
PRARVULVAR = 'prarvulvar'
BRAXFLELK = 'braxflelk'
BRULCLENR = 'brulclenr'
GRAXFLUR = 'graxflur'
BLIMTRELVALK = 'blimtrelvalk'
SLEXBRELR = 'slexbrelr'
CLIMTRURSLEX = 'climtrurslex'
STIMDRONX = 'stimdronx'
STOSKRANSTIMT = 'stoskranstimt'
SKELBLART = 'skelblart'
GLONGLALSLOR = 'glonglalslor'
STORBLEN = 'storblen'
BLONBRURCLELX = 'blonbrurclelx'
CLIMSPANL = 'climspanl'
VONFLONGRALR = 'vonflongralr'
VAXTREXCLULT = 'vaxtrexclult'
SLALGRARTREX = 'slalgrartrex'
DRANKREL = 'drankrel'
BRALFLEN = 'bralflen'
DRURPRORSPULT = 'drurprorspult'
BLORSTOR = 'blorstor'
VENVEXGLANK = 'venvexglank'
SPEXVAXSLURX = 'spexvaxslurx'
GLIXBLALBRART = 'glixblalbrart'
TREXPRALT = 'trexpralt'
PRORSKEXT = 'prorskext'
FLELSPORBLAL = 'flelsporblal'
BLOSSTULVURL = 'blosstulvurl'
VIXPRONSLENN = 'vixpronslenn'
CLORBRIM = 'clorbrim'
PROSGLALKRIX = 'prosglalkrix'

_R = {
    VIXPRONSLENN: 0,
    CLORBRIM: 1,
    PROSGLALKRIX: 2,
}

_CTX_READS_KEY = 'flurslex'
_CTX_THRESHOLD = 16

class SkanpronnFSM:
    def __init__(self):
        self._state = {}

    def _slanstartron(self, hint):
        assert self._state.get("current") == SLANSTARTRON, \
            f"skanpronn.slanstartron: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slanstartron', 2:
                self._state["current"] = PROSGLALKRIX
                self._state["trig"]    = "hint:2"
            case 'slanstartron', 0:
                self._state["current"] = CLORBRIM
                self._state["trig"]    = "hint:0"
            case 'slanstartron', _:
                self._state["current"] = DRANGRIX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slanstartron', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slanstartron',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slanstartron->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _drangrix(self, hint):
        assert self._state.get("current") == DRANGRIX, \
            f"skanpronn.drangrix: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'drangrix', 2:
                self._state["current"] = PROSGLALKRIX
                self._state["trig"]    = "hint:2"
            case 'drangrix', _:
                self._state["current"] = CLENDRAXTRALT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'drangrix', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'drangrix',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"drangrix->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _clendraxtralt(self, hint):
        assert self._state.get("current") == CLENDRAXTRALT, \
            f"skanpronn.clendraxtralt: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'clendraxtralt', 2:
                self._state["current"] = PROSGLALKRIX
                self._state["trig"]    = "hint:2"
            case 'clendraxtralt', 0:
                self._state["current"] = DRALCLAL
                self._state["trig"]    = "hint:0"
            case 'clendraxtralt', _:
                self._state["current"] = STORSTAR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'clendraxtralt', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'clendraxtralt',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"clendraxtralt->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _storstar(self, hint):
        assert self._state.get("current") == STORSTAR, \
            f"skanpronn.storstar: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'storstar', 2:
                self._state["current"] = PROSGLALKRIX
                self._state["trig"]    = "hint:2"
            case 'storstar', _:
                self._state["current"] = DRALCLAL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'storstar', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'storstar',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"storstar->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _dralclal(self, hint):
        assert self._state.get("current") == DRALCLAL, \
            f"skanpronn.dralclal: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'dralclal', 2:
                self._state["current"] = PROSGLALKRIX
                self._state["trig"]    = "hint:2"
            case 'dralclal', 1:
                self._state["current"] = CLORBRIM
                self._state["trig"]    = "hint:1"
            case 'dralclal', _:
                self._state["current"] = KRANDRELCLIXN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'dralclal', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'dralclal',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"dralclal->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _krandrelclixn(self, hint):
        assert self._state.get("current") == KRANDRELCLIXN, \
            f"skanpronn.krandrelclixn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'krandrelclixn', 2:
                self._state["current"] = PROSGLALKRIX
                self._state["trig"]    = "hint:2"
            case 'krandrelclixn', 1:
                self._state["current"] = CLORBRIM
                self._state["trig"]    = "hint:1"
            case 'krandrelclixn', _:
                self._state["current"] = STANCLIMBREL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'krandrelclixn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'krandrelclixn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"krandrelclixn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _stanclimbrel(self, hint):
        assert self._state.get("current") == STANCLIMBREL, \
            f"skanpronn.stanclimbrel: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'stanclimbrel', 2:
                self._state["current"] = PROSGLALKRIX
                self._state["trig"]    = "hint:2"
            case 'stanclimbrel', _:
                self._state["current"] = BLELTRALT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'stanclimbrel', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'stanclimbrel',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"stanclimbrel->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _bleltralt(self, hint):
        assert self._state.get("current") == BLELTRALT, \
            f"skanpronn.bleltralt: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'bleltralt', 2:
                self._state["current"] = PROSGLALKRIX
                self._state["trig"]    = "hint:2"
            case 'bleltralt', _:
                self._state["current"] = TROSBRULKRAN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'bleltralt', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'bleltralt',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"bleltralt->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _trosbrulkran(self, hint):
        assert self._state.get("current") == TROSBRULKRAN, \
            f"skanpronn.trosbrulkran: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'trosbrulkran', 2:
                self._state["current"] = PROSGLALKRIX
                self._state["trig"]    = "hint:2"
            case 'trosbrulkran', _:
                self._state["current"] = PRELGLAX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'trosbrulkran', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'trosbrulkran',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"trosbrulkran->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _prelglax(self, hint):
        assert self._state.get("current") == PRELGLAX, \
            f"skanpronn.prelglax: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'prelglax', 2:
                self._state["current"] = PROSGLALKRIX
                self._state["trig"]    = "hint:2"
            case 'prelglax', _:
                self._state["current"] = BLURSTANPRAX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'prelglax', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'prelglax',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"prelglax->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blurstanprax(self, hint):
        assert self._state.get("current") == BLURSTANPRAX, \
            f"skanpronn.blurstanprax: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blurstanprax', 2:
                self._state["current"] = PROSGLALKRIX
                self._state["trig"]    = "hint:2"
            case 'blurstanprax', 1:
                self._state["current"] = CLORBRIM
                self._state["trig"]    = "hint:1"
            case 'blurstanprax', _:
                self._state["current"] = BLONBRURK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blurstanprax', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blurstanprax',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blurstanprax->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blonbrurk(self, hint):
        assert self._state.get("current") == BLONBRURK, \
            f"skanpronn.blonbrurk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blonbrurk', 2:
                self._state["current"] = PROSGLALKRIX
                self._state["trig"]    = "hint:2"
            case 'blonbrurk', _:
                self._state["current"] = SKIMSKOSK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blonbrurk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blonbrurk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blonbrurk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skimskosk(self, hint):
        assert self._state.get("current") == SKIMSKOSK, \
            f"skanpronn.skimskosk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skimskosk', 2:
                self._state["current"] = PROSGLALKRIX
                self._state["trig"]    = "hint:2"
            case 'skimskosk', _:
                self._state["current"] = GLIXCLOSCLANT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skimskosk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skimskosk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skimskosk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glixclosclant(self, hint):
        assert self._state.get("current") == GLIXCLOSCLANT, \
            f"skanpronn.glixclosclant: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glixclosclant', 2:
                self._state["current"] = PROSGLALKRIX
                self._state["trig"]    = "hint:2"
            case 'glixclosclant', _:
                self._state["current"] = BROSBREXKREN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glixclosclant', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glixclosclant',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glixclosclant->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brosbrexkren(self, hint):
        assert self._state.get("current") == BROSBREXKREN, \
            f"skanpronn.brosbrexkren: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brosbrexkren', 2:
                self._state["current"] = PROSGLALKRIX
                self._state["trig"]    = "hint:2"
            case 'brosbrexkren', _:
                self._state["current"] = CLEXFLORGRON
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brosbrexkren', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brosbrexkren',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brosbrexkren->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _clexflorgron(self, hint):
        assert self._state.get("current") == CLEXFLORGRON, \
            f"skanpronn.clexflorgron: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'clexflorgron', 2:
                self._state["current"] = PROSGLALKRIX
                self._state["trig"]    = "hint:2"
            case 'clexflorgron', _:
                self._state["current"] = KRIMTRENBREN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'clexflorgron', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'clexflorgron',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"clexflorgron->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _krimtrenbren(self, hint):
        assert self._state.get("current") == KRIMTRENBREN, \
            f"skanpronn.krimtrenbren: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'krimtrenbren', 2:
                self._state["current"] = PROSGLALKRIX
                self._state["trig"]    = "hint:2"
            case 'krimtrenbren', _:
                self._state["current"] = SKALGLAR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'krimtrenbren', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'krimtrenbren',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"krimtrenbren->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skalglar(self, hint):
        assert self._state.get("current") == SKALGLAR, \
            f"skanpronn.skalglar: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skalglar', 2:
                self._state["current"] = PROSGLALKRIX
                self._state["trig"]    = "hint:2"
            case 'skalglar', _:
                self._state["current"] = GRULDRIMSTORL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skalglar', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skalglar',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skalglar->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _gruldrimstorl(self, hint):
        assert self._state.get("current") == GRULDRIMSTORL, \
            f"skanpronn.gruldrimstorl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'gruldrimstorl', 2:
                self._state["current"] = PROSGLALKRIX
                self._state["trig"]    = "hint:2"
            case 'gruldrimstorl', 1:
                self._state["current"] = FLOSPRORSPENK
                self._state["trig"]    = "hint:1"
            case 'gruldrimstorl', _:
                self._state["current"] = BRURFLOSPROR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'gruldrimstorl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'gruldrimstorl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"gruldrimstorl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brurflospror(self, hint):
        assert self._state.get("current") == BRURFLOSPROR, \
            f"skanpronn.brurflospror: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brurflospror', 2:
                self._state["current"] = PROSGLALKRIX
                self._state["trig"]    = "hint:2"
            case 'brurflospror', _:
                self._state["current"] = FLOSPRORSPENK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brurflospror', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brurflospror',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brurflospror->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _flosprorspenk(self, hint):
        assert self._state.get("current") == FLOSPRORSPENK, \
            f"skanpronn.flosprorspenk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'flosprorspenk', 2:
                self._state["current"] = PROSGLALKRIX
                self._state["trig"]    = "hint:2"
            case 'flosprorspenk', _:
                self._state["current"] = SKURSPOR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'flosprorspenk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'flosprorspenk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"flosprorspenk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skurspor(self, hint):
        assert self._state.get("current") == SKURSPOR, \
            f"skanpronn.skurspor: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skurspor', 2:
                self._state["current"] = PROSGLALKRIX
                self._state["trig"]    = "hint:2"
            case 'skurspor', _:
                self._state["current"] = SKONTREL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skurspor', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skurspor',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skurspor->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skontrel(self, hint):
        assert self._state.get("current") == SKONTREL, \
            f"skanpronn.skontrel: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skontrel', 2:
                self._state["current"] = PROSGLALKRIX
                self._state["trig"]    = "hint:2"
            case 'skontrel', _:
                self._state["current"] = FLEXVEXT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skontrel', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skontrel',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skontrel->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _flexvext(self, hint):
        assert self._state.get("current") == FLEXVEXT, \
            f"skanpronn.flexvext: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'flexvext', 2:
                self._state["current"] = PROSGLALKRIX
                self._state["trig"]    = "hint:2"
            case 'flexvext', 1:
                self._state["current"] = CLORBRIM
                self._state["trig"]    = "hint:1"
            case 'flexvext', _:
                self._state["current"] = SLEXPRORCLIX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'flexvext', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'flexvext',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"flexvext->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slexprorclix(self, hint):
        assert self._state.get("current") == SLEXPRORCLIX, \
            f"skanpronn.slexprorclix: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slexprorclix', 2:
                self._state["current"] = PROSGLALKRIX
                self._state["trig"]    = "hint:2"
            case 'slexprorclix', _:
                self._state["current"] = BRELGRONSKURR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slexprorclix', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slexprorclix',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slexprorclix->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brelgronskurr(self, hint):
        assert self._state.get("current") == BRELGRONSKURR, \
            f"skanpronn.brelgronskurr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brelgronskurr', 2:
                self._state["current"] = PROSGLALKRIX
                self._state["trig"]    = "hint:2"
            case 'brelgronskurr', _:
                self._state["current"] = BLIMGRONTRON
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brelgronskurr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brelgronskurr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brelgronskurr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blimgrontron(self, hint):
        assert self._state.get("current") == BLIMGRONTRON, \
            f"skanpronn.blimgrontron: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blimgrontron', 2:
                self._state["current"] = PROSGLALKRIX
                self._state["trig"]    = "hint:2"
            case 'blimgrontron', 1:
                self._state["current"] = CLANSLUR
                self._state["trig"]    = "hint:1"
            case 'blimgrontron', _:
                self._state["current"] = BLALPRARK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blimgrontron', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blimgrontron',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blimgrontron->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blalprark(self, hint):
        assert self._state.get("current") == BLALPRARK, \
            f"skanpronn.blalprark: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blalprark', 2:
                self._state["current"] = PROSGLALKRIX
                self._state["trig"]    = "hint:2"
            case 'blalprark', _:
                self._state["current"] = CLANSLUR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blalprark', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blalprark',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blalprark->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _clanslur(self, hint):
        assert self._state.get("current") == CLANSLUR, \
            f"skanpronn.clanslur: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'clanslur', 2:
                self._state["current"] = PROSGLALKRIX
                self._state["trig"]    = "hint:2"
            case 'clanslur', 1:
                self._state["current"] = BLURTRAXSKIXT
                self._state["trig"]    = "hint:1"
            case 'clanslur', _:
                self._state["current"] = BRORSLEL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'clanslur', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'clanslur',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"clanslur->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brorslel(self, hint):
        assert self._state.get("current") == BRORSLEL, \
            f"skanpronn.brorslel: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brorslel', 2:
                self._state["current"] = PROSGLALKRIX
                self._state["trig"]    = "hint:2"
            case 'brorslel', _:
                self._state["current"] = BLURTRAXSKIXT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brorslel', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brorslel',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brorslel->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blurtraxskixt(self, hint):
        assert self._state.get("current") == BLURTRAXSKIXT, \
            f"skanpronn.blurtraxskixt: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blurtraxskixt', 2:
                self._state["current"] = PROSGLALKRIX
                self._state["trig"]    = "hint:2"
            case 'blurtraxskixt', _:
                self._state["current"] = VANVAXX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blurtraxskixt', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blurtraxskixt',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blurtraxskixt->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _vanvaxx(self, hint):
        assert self._state.get("current") == VANVAXX, \
            f"skanpronn.vanvaxx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'vanvaxx', 2:
                self._state["current"] = PROSGLALKRIX
                self._state["trig"]    = "hint:2"
            case 'vanvaxx', 1:
                self._state["current"] = CLORBRIM
                self._state["trig"]    = "hint:1"
            case 'vanvaxx', _:
                self._state["current"] = DRAXBRELL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'vanvaxx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'vanvaxx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"vanvaxx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _draxbrell(self, hint):
        assert self._state.get("current") == DRAXBRELL, \
            f"skanpronn.draxbrell: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'draxbrell', 2:
                self._state["current"] = PROSGLALKRIX
                self._state["trig"]    = "hint:2"
            case 'draxbrell', _:
                self._state["current"] = VONSPAXGRULL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'draxbrell', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'draxbrell',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"draxbrell->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _vonspaxgrull(self, hint):
        assert self._state.get("current") == VONSPAXGRULL, \
            f"skanpronn.vonspaxgrull: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'vonspaxgrull', 2:
                self._state["current"] = PROSGLALKRIX
                self._state["trig"]    = "hint:2"
            case 'vonspaxgrull', 0:
                self._state["current"] = CLORBRIM
                self._state["trig"]    = "hint:0"
            case 'vonspaxgrull', _:
                self._state["current"] = SPIMSLARPRIM
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'vonspaxgrull', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'vonspaxgrull',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"vonspaxgrull->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _spimslarprim(self, hint):
        assert self._state.get("current") == SPIMSLARPRIM, \
            f"skanpronn.spimslarprim: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'spimslarprim', 2:
                self._state["current"] = PROSGLALKRIX
                self._state["trig"]    = "hint:2"
            case 'spimslarprim', 1:
                self._state["current"] = CLORBRIM
                self._state["trig"]    = "hint:1"
            case 'spimslarprim', _:
                self._state["current"] = VARGRENVAX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'spimslarprim', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'spimslarprim',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"spimslarprim->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _vargrenvax(self, hint):
        assert self._state.get("current") == VARGRENVAX, \
            f"skanpronn.vargrenvax: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'vargrenvax', 2:
                self._state["current"] = PROSGLALKRIX
                self._state["trig"]    = "hint:2"
            case 'vargrenvax', 1:
                self._state["current"] = PRARVULVAR
                self._state["trig"]    = "hint:1"
            case 'vargrenvax', _:
                self._state["current"] = GLEXGLELTRON
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'vargrenvax', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'vargrenvax',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"vargrenvax->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glexgleltron(self, hint):
        assert self._state.get("current") == GLEXGLELTRON, \
            f"skanpronn.glexgleltron: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glexgleltron', 2:
                self._state["current"] = PROSGLALKRIX
                self._state["trig"]    = "hint:2"
            case 'glexgleltron', 1:
                self._state["current"] = BRAXFLELK
                self._state["trig"]    = "hint:1"
            case 'glexgleltron', _:
                self._state["current"] = PRARVULVAR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glexgleltron', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glexgleltron',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glexgleltron->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _prarvulvar(self, hint):
        assert self._state.get("current") == PRARVULVAR, \
            f"skanpronn.prarvulvar: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'prarvulvar', 2:
                self._state["current"] = PROSGLALKRIX
                self._state["trig"]    = "hint:2"
            case 'prarvulvar', 1:
                self._state["current"] = BRULCLENR
                self._state["trig"]    = "hint:1"
            case 'prarvulvar', _:
                self._state["current"] = BRAXFLELK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'prarvulvar', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'prarvulvar',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"prarvulvar->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _braxflelk(self, hint):
        assert self._state.get("current") == BRAXFLELK, \
            f"skanpronn.braxflelk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'braxflelk', 2:
                self._state["current"] = PROSGLALKRIX
                self._state["trig"]    = "hint:2"
            case 'braxflelk', _:
                self._state["current"] = BRULCLENR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'braxflelk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'braxflelk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"braxflelk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brulclenr(self, hint):
        assert self._state.get("current") == BRULCLENR, \
            f"skanpronn.brulclenr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brulclenr', 2:
                self._state["current"] = PROSGLALKRIX
                self._state["trig"]    = "hint:2"
            case 'brulclenr', _:
                self._state["current"] = GRAXFLUR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brulclenr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brulclenr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brulclenr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _graxflur(self, hint):
        assert self._state.get("current") == GRAXFLUR, \
            f"skanpronn.graxflur: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'graxflur', 2:
                self._state["current"] = PROSGLALKRIX
                self._state["trig"]    = "hint:2"
            case 'graxflur', 1:
                self._state["current"] = CLORBRIM
                self._state["trig"]    = "hint:1"
            case 'graxflur', _:
                self._state["current"] = BLIMTRELVALK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'graxflur', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'graxflur',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"graxflur->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blimtrelvalk(self, hint):
        assert self._state.get("current") == BLIMTRELVALK, \
            f"skanpronn.blimtrelvalk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blimtrelvalk', 2:
                self._state["current"] = PROSGLALKRIX
                self._state["trig"]    = "hint:2"
            case 'blimtrelvalk', _:
                self._state["current"] = SLEXBRELR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blimtrelvalk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blimtrelvalk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blimtrelvalk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slexbrelr(self, hint):
        assert self._state.get("current") == SLEXBRELR, \
            f"skanpronn.slexbrelr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slexbrelr', 2:
                self._state["current"] = PROSGLALKRIX
                self._state["trig"]    = "hint:2"
            case 'slexbrelr', _:
                self._state["current"] = CLIMTRURSLEX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slexbrelr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slexbrelr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slexbrelr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _climtrurslex(self, hint):
        assert self._state.get("current") == CLIMTRURSLEX, \
            f"skanpronn.climtrurslex: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'climtrurslex', 2:
                self._state["current"] = PROSGLALKRIX
                self._state["trig"]    = "hint:2"
            case 'climtrurslex', 1:
                self._state["current"] = STOSKRANSTIMT
                self._state["trig"]    = "hint:1"
            case 'climtrurslex', _:
                self._state["current"] = STIMDRONX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'climtrurslex', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'climtrurslex',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"climtrurslex->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _stimdronx(self, hint):
        assert self._state.get("current") == STIMDRONX, \
            f"skanpronn.stimdronx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'stimdronx', 2:
                self._state["current"] = PROSGLALKRIX
                self._state["trig"]    = "hint:2"
            case 'stimdronx', 0:
                self._state["current"] = CLORBRIM
                self._state["trig"]    = "hint:0"
            case 'stimdronx', _:
                self._state["current"] = STOSKRANSTIMT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'stimdronx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'stimdronx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"stimdronx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _stoskranstimt(self, hint):
        assert self._state.get("current") == STOSKRANSTIMT, \
            f"skanpronn.stoskranstimt: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'stoskranstimt', 2:
                self._state["current"] = PROSGLALKRIX
                self._state["trig"]    = "hint:2"
            case 'stoskranstimt', 1:
                self._state["current"] = CLORBRIM
                self._state["trig"]    = "hint:1"
            case 'stoskranstimt', _:
                self._state["current"] = SKELBLART
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'stoskranstimt', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'stoskranstimt',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"stoskranstimt->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skelblart(self, hint):
        assert self._state.get("current") == SKELBLART, \
            f"skanpronn.skelblart: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skelblart', 2:
                self._state["current"] = PROSGLALKRIX
                self._state["trig"]    = "hint:2"
            case 'skelblart', 0:
                self._state["current"] = CLORBRIM
                self._state["trig"]    = "hint:0"
            case 'skelblart', _:
                self._state["current"] = GLONGLALSLOR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skelblart', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skelblart',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skelblart->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glonglalslor(self, hint):
        assert self._state.get("current") == GLONGLALSLOR, \
            f"skanpronn.glonglalslor: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glonglalslor', 2:
                self._state["current"] = PROSGLALKRIX
                self._state["trig"]    = "hint:2"
            case 'glonglalslor', _:
                self._state["current"] = STORBLEN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glonglalslor', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glonglalslor',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glonglalslor->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _storblen(self, hint):
        assert self._state.get("current") == STORBLEN, \
            f"skanpronn.storblen: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'storblen', 2:
                self._state["current"] = PROSGLALKRIX
                self._state["trig"]    = "hint:2"
            case 'storblen', 1:
                self._state["current"] = CLORBRIM
                self._state["trig"]    = "hint:1"
            case 'storblen', _:
                self._state["current"] = BLONBRURCLELX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'storblen', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'storblen',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"storblen->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blonbrurclelx(self, hint):
        assert self._state.get("current") == BLONBRURCLELX, \
            f"skanpronn.blonbrurclelx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blonbrurclelx', 2:
                self._state["current"] = PROSGLALKRIX
                self._state["trig"]    = "hint:2"
            case 'blonbrurclelx', 0:
                self._state["current"] = CLORBRIM
                self._state["trig"]    = "hint:0"
            case 'blonbrurclelx', _:
                self._state["current"] = CLIMSPANL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blonbrurclelx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blonbrurclelx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blonbrurclelx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _climspanl(self, hint):
        assert self._state.get("current") == CLIMSPANL, \
            f"skanpronn.climspanl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'climspanl', 2:
                self._state["current"] = PROSGLALKRIX
                self._state["trig"]    = "hint:2"
            case 'climspanl', _:
                self._state["current"] = VONFLONGRALR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'climspanl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'climspanl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"climspanl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _vonflongralr(self, hint):
        assert self._state.get("current") == VONFLONGRALR, \
            f"skanpronn.vonflongralr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'vonflongralr', 2:
                self._state["current"] = PROSGLALKRIX
                self._state["trig"]    = "hint:2"
            case 'vonflongralr', 0:
                self._state["current"] = CLORBRIM
                self._state["trig"]    = "hint:0"
            case 'vonflongralr', _:
                self._state["current"] = VAXTREXCLULT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'vonflongralr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'vonflongralr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"vonflongralr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _vaxtrexclult(self, hint):
        assert self._state.get("current") == VAXTREXCLULT, \
            f"skanpronn.vaxtrexclult: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'vaxtrexclult', 2:
                self._state["current"] = PROSGLALKRIX
                self._state["trig"]    = "hint:2"
            case 'vaxtrexclult', 1:
                self._state["current"] = DRANKREL
                self._state["trig"]    = "hint:1"
            case 'vaxtrexclult', _:
                self._state["current"] = SLALGRARTREX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'vaxtrexclult', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'vaxtrexclult',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"vaxtrexclult->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slalgrartrex(self, hint):
        assert self._state.get("current") == SLALGRARTREX, \
            f"skanpronn.slalgrartrex: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slalgrartrex', 2:
                self._state["current"] = PROSGLALKRIX
                self._state["trig"]    = "hint:2"
            case 'slalgrartrex', 0:
                self._state["current"] = CLORBRIM
                self._state["trig"]    = "hint:0"
            case 'slalgrartrex', _:
                self._state["current"] = DRANKREL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slalgrartrex', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slalgrartrex',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slalgrartrex->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _drankrel(self, hint):
        assert self._state.get("current") == DRANKREL, \
            f"skanpronn.drankrel: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'drankrel', 2:
                self._state["current"] = PROSGLALKRIX
                self._state["trig"]    = "hint:2"
            case 'drankrel', _:
                self._state["current"] = BRALFLEN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'drankrel', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'drankrel',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"drankrel->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _bralflen(self, hint):
        assert self._state.get("current") == BRALFLEN, \
            f"skanpronn.bralflen: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'bralflen', 2:
                self._state["current"] = PROSGLALKRIX
                self._state["trig"]    = "hint:2"
            case 'bralflen', _:
                self._state["current"] = DRURPRORSPULT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'bralflen', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'bralflen',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"bralflen->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _drurprorspult(self, hint):
        assert self._state.get("current") == DRURPRORSPULT, \
            f"skanpronn.drurprorspult: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'drurprorspult', 2:
                self._state["current"] = PROSGLALKRIX
                self._state["trig"]    = "hint:2"
            case 'drurprorspult', 0:
                self._state["current"] = CLORBRIM
                self._state["trig"]    = "hint:0"
            case 'drurprorspult', _:
                self._state["current"] = BLORSTOR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'drurprorspult', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'drurprorspult',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"drurprorspult->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blorstor(self, hint):
        assert self._state.get("current") == BLORSTOR, \
            f"skanpronn.blorstor: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blorstor', 2:
                self._state["current"] = PROSGLALKRIX
                self._state["trig"]    = "hint:2"
            case 'blorstor', 1:
                self._state["current"] = SPEXVAXSLURX
                self._state["trig"]    = "hint:1"
            case 'blorstor', _:
                self._state["current"] = VENVEXGLANK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blorstor', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blorstor',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blorstor->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _venvexglank(self, hint):
        assert self._state.get("current") == VENVEXGLANK, \
            f"skanpronn.venvexglank: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'venvexglank', 2:
                self._state["current"] = PROSGLALKRIX
                self._state["trig"]    = "hint:2"
            case 'venvexglank', _:
                self._state["current"] = SPEXVAXSLURX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'venvexglank', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'venvexglank',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"venvexglank->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _spexvaxslurx(self, hint):
        assert self._state.get("current") == SPEXVAXSLURX, \
            f"skanpronn.spexvaxslurx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'spexvaxslurx', 2:
                self._state["current"] = PROSGLALKRIX
                self._state["trig"]    = "hint:2"
            case 'spexvaxslurx', _:
                self._state["current"] = GLIXBLALBRART
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'spexvaxslurx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'spexvaxslurx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"spexvaxslurx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glixblalbrart(self, hint):
        assert self._state.get("current") == GLIXBLALBRART, \
            f"skanpronn.glixblalbrart: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glixblalbrart', 2:
                self._state["current"] = PROSGLALKRIX
                self._state["trig"]    = "hint:2"
            case 'glixblalbrart', _:
                self._state["current"] = TREXPRALT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glixblalbrart', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glixblalbrart',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glixblalbrart->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _trexpralt(self, hint):
        assert self._state.get("current") == TREXPRALT, \
            f"skanpronn.trexpralt: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'trexpralt', 2:
                self._state["current"] = PROSGLALKRIX
                self._state["trig"]    = "hint:2"
            case 'trexpralt', 0:
                self._state["current"] = FLELSPORBLAL
                self._state["trig"]    = "hint:0"
            case 'trexpralt', _:
                self._state["current"] = PRORSKEXT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'trexpralt', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'trexpralt',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"trexpralt->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _prorskext(self, hint):
        assert self._state.get("current") == PRORSKEXT, \
            f"skanpronn.prorskext: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'prorskext', 2:
                self._state["current"] = PROSGLALKRIX
                self._state["trig"]    = "hint:2"
            case 'prorskext', 1:
                self._state["current"] = CLORBRIM
                self._state["trig"]    = "hint:1"
            case 'prorskext', _:
                self._state["current"] = FLELSPORBLAL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'prorskext', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'prorskext',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"prorskext->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _flelsporblal(self, hint):
        assert self._state.get("current") == FLELSPORBLAL, \
            f"skanpronn.flelsporblal: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'flelsporblal', 2:
                self._state["current"] = PROSGLALKRIX
                self._state["trig"]    = "hint:2"
            case 'flelsporblal', 0:
                self._state["current"] = CLORBRIM
                self._state["trig"]    = "hint:0"
            case 'flelsporblal', _:
                self._state["current"] = BLOSSTULVURL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'flelsporblal', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'flelsporblal',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"flelsporblal->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blosstulvurl(self, hint):
        assert self._state.get("current") == BLOSSTULVURL, \
            f"skanpronn.blosstulvurl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blosstulvurl', 2:
                self._state["current"] = PROSGLALKRIX
                self._state["trig"]    = "hint:2"
            case 'blosstulvurl', 1:
                self._state["current"] = CLORBRIM
                self._state["trig"]    = "hint:1"
            case 'blosstulvurl', _:
                self._state["current"] = VIXPRONSLENN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blosstulvurl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blosstulvurl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blosstulvurl->{_to}", _xid_val)
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
            _xid_val = _xid(__name__, 'slanstartron', "error", "assert_fail")
            _emit(cycle, 1, __name__, 'slanstartron',
                   {"hint": hint, "span": span, "caller": caller},
                   dict(ctx), _conds,
                   "entry_blocked->error", _xid_val, assertion=_asrt)
            return 2, cycle + 1

        self._state = {"current": SLANSTARTRON, "ctx": ctx,
                        "span": span, "caller": caller,
                        "trig": "auto", "cycle": cycle}
        _dispatch = {
            SLANSTARTRON: self._slanstartron,
            DRANGRIX: self._drangrix,
            CLENDRAXTRALT: self._clendraxtralt,
            STORSTAR: self._storstar,
            DRALCLAL: self._dralclal,
            KRANDRELCLIXN: self._krandrelclixn,
            STANCLIMBREL: self._stanclimbrel,
            BLELTRALT: self._bleltralt,
            TROSBRULKRAN: self._trosbrulkran,
            PRELGLAX: self._prelglax,
            BLURSTANPRAX: self._blurstanprax,
            BLONBRURK: self._blonbrurk,
            SKIMSKOSK: self._skimskosk,
            GLIXCLOSCLANT: self._glixclosclant,
            BROSBREXKREN: self._brosbrexkren,
            CLEXFLORGRON: self._clexflorgron,
            KRIMTRENBREN: self._krimtrenbren,
            SKALGLAR: self._skalglar,
            GRULDRIMSTORL: self._gruldrimstorl,
            BRURFLOSPROR: self._brurflospror,
            FLOSPRORSPENK: self._flosprorspenk,
            SKURSPOR: self._skurspor,
            SKONTREL: self._skontrel,
            FLEXVEXT: self._flexvext,
            SLEXPRORCLIX: self._slexprorclix,
            BRELGRONSKURR: self._brelgronskurr,
            BLIMGRONTRON: self._blimgrontron,
            BLALPRARK: self._blalprark,
            CLANSLUR: self._clanslur,
            BRORSLEL: self._brorslel,
            BLURTRAXSKIXT: self._blurtraxskixt,
            VANVAXX: self._vanvaxx,
            DRAXBRELL: self._draxbrell,
            VONSPAXGRULL: self._vonspaxgrull,
            SPIMSLARPRIM: self._spimslarprim,
            VARGRENVAX: self._vargrenvax,
            GLEXGLELTRON: self._glexgleltron,
            PRARVULVAR: self._prarvulvar,
            BRAXFLELK: self._braxflelk,
            BRULCLENR: self._brulclenr,
            GRAXFLUR: self._graxflur,
            BLIMTRELVALK: self._blimtrelvalk,
            SLEXBRELR: self._slexbrelr,
            CLIMTRURSLEX: self._climtrurslex,
            STIMDRONX: self._stimdronx,
            STOSKRANSTIMT: self._stoskranstimt,
            SKELBLART: self._skelblart,
            GLONGLALSLOR: self._glonglalslor,
            STORBLEN: self._storblen,
            BLONBRURCLELX: self._blonbrurclelx,
            CLIMSPANL: self._climspanl,
            VONFLONGRALR: self._vonflongralr,
            VAXTREXCLULT: self._vaxtrexclult,
            SLALGRARTREX: self._slalgrartrex,
            DRANKREL: self._drankrel,
            BRALFLEN: self._bralflen,
            DRURPRORSPULT: self._drurprorspult,
            BLORSTOR: self._blorstor,
            VENVEXGLANK: self._venvexglank,
            SPEXVAXSLURX: self._spexvaxslurx,
            GLIXBLALBRART: self._glixblalbrart,
            TREXPRALT: self._trexpralt,
            PRORSKEXT: self._prorskext,
            FLELSPORBLAL: self._flelsporblal,
            BLOSSTULVURL: self._blosstulvurl,
        }
        while self._state["current"] not in _R and self._state["cycle"] - cycle < 8000:
            _dispatch[self._state["current"]](hint)
        _ret     = _R.get(self._state["current"], -1)
        _is_err  = self._state["current"] == PROSGLALKRIX
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
    return SkanpronnFSM().invoke(hint=hint, span=span, caller=caller, ctx=ctx, cycle=cycle)
