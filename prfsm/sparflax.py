from _log import _w as _emit, _xid

BRENCLORSTAXN = 'brenclorstaxn'
SLORKRULN = 'slorkruln'
KREXFLALBRON = 'krexflalbron'
DRALKRART = 'dralkrart'
SLULBRULT = 'slulbrult'
SLARSPIMKRAR = 'slarspimkrar'
PRIMGRENDRENX = 'primgrendrenx'
PRULSLORDRUR = 'prulslordrur'
PRENSTON = 'prenston'
GRIMGLARN = 'grimglarn'
KRENSKAXBLEXN = 'krenskaxblexn'
BRENSLORX = 'brenslorx'
STARTRENVAX = 'startrenvax'
PRELGREXVOR = 'prelgrexvor'
CLIMVAXR = 'climvaxr'
TRANCLALSTONL = 'tranclalstonl'
TRONGRORGRONX = 'trongrorgronx'
STAXDRARSLALK = 'staxdrarslalk'
SKEXSLELVURT = 'skexslelvurt'
DRORGRELX = 'drorgrelx'
SKELVONL = 'skelvonl'
KRIMPROS = 'krimpros'
GLALDRIMDRAN = 'glaldrimdran'
SLONSLELK = 'slonslelk'
VULGLALT = 'vulglalt'
TRENPREXX = 'trenprexx'
SPONKRARSTON = 'sponkrarston'
BRORFLANX = 'brorflanx'
KREXSPIXCLEL = 'krexspixclel'
BLORSKEN = 'blorsken'
KRULPROS = 'krulpros'
FLALSTIXTRAX = 'flalstixtrax'
FLANPRALX = 'flanpralx'
VELBREN = 'velbren'
SPURSKULK = 'spurskulk'
VONPRELGRIM = 'vonprelgrim'
CLALSPALDRIML = 'clalspaldriml'
GRONGLARGRARR = 'gronglargrarr'
FLONBLIXSPORL = 'flonblixsporl'
BRARGRURSKULR = 'brargrurskulr'
KRORCLURTRUL = 'krorclurtrul'
GLENTROS = 'glentros'
GRANTRURSKAL = 'grantrurskal'
SPORBLELR = 'sporblelr'
STENBLANX = 'stenblanx'
SKOSFLAXBLIXK = 'skosflaxblixk'
TRULSKORBRALT = 'trulskorbralt'
GRONBRIMX = 'gronbrimx'
GLIXTRARVAX = 'glixtrarvax'
PRAXPRIMTRIMX = 'praxprimtrimx'
GRONGRURCLOSN = 'grongrurclosn'
DRANBRENTRIXL = 'dranbrentrixl'
SLOSSLEN = 'slosslen'
GLAXFLENSPURX = 'glaxflenspurx'
GRURPRIM = 'grurprim'
CLIMSPIX = 'climspix'
BRIMBRANT = 'brimbrant'
GLORSPENDREXN = 'glorspendrexn'
DRARTRURBLUR = 'drartrurblur'
GROSGLANX = 'grosglanx'
GRENSKIMX = 'grenskimx'
GRARGRIMSLEXK = 'grargrimslexk'
SLIMSPELT = 'slimspelt'
FLURFLAXR = 'flurflaxr'
CLOSSKANSTAXL = 'closskanstaxl'
VALPRURL = 'valprurl'
GLORBRALTREXR = 'glorbraltrexr'
DRAXBRAXBLON = 'draxbraxblon'

_R = {
    VALPRURL: 0,
    GLORBRALTREXR: 1,
    DRAXBRAXBLON: 2,
}

_CTX_READS_KEY = 'flurslex'
_CTX_THRESHOLD = 16

class SparflaxFSM:
    def __init__(self):
        self._state = {}

    def _brenclorstaxn(self, hint):
        assert self._state.get("current") == BRENCLORSTAXN, \
            f"sparflax.brenclorstaxn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brenclorstaxn', 2:
                self._state["current"] = DRAXBRAXBLON
                self._state["trig"]    = "hint:2"
            case 'brenclorstaxn', 0:
                self._state["current"] = GLORBRALTREXR
                self._state["trig"]    = "hint:0"
            case 'brenclorstaxn', _:
                self._state["current"] = SLORKRULN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brenclorstaxn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brenclorstaxn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brenclorstaxn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slorkruln(self, hint):
        assert self._state.get("current") == SLORKRULN, \
            f"sparflax.slorkruln: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slorkruln', 2:
                self._state["current"] = DRAXBRAXBLON
                self._state["trig"]    = "hint:2"
            case 'slorkruln', _:
                self._state["current"] = KREXFLALBRON
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slorkruln', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slorkruln',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slorkruln->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _krexflalbron(self, hint):
        assert self._state.get("current") == KREXFLALBRON, \
            f"sparflax.krexflalbron: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'krexflalbron', 2:
                self._state["current"] = DRAXBRAXBLON
                self._state["trig"]    = "hint:2"
            case 'krexflalbron', 1:
                self._state["current"] = GLORBRALTREXR
                self._state["trig"]    = "hint:1"
            case 'krexflalbron', _:
                self._state["current"] = DRALKRART
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'krexflalbron', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'krexflalbron',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"krexflalbron->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _dralkrart(self, hint):
        assert self._state.get("current") == DRALKRART, \
            f"sparflax.dralkrart: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'dralkrart', 2:
                self._state["current"] = DRAXBRAXBLON
                self._state["trig"]    = "hint:2"
            case 'dralkrart', 1:
                self._state["current"] = GLORBRALTREXR
                self._state["trig"]    = "hint:1"
            case 'dralkrart', _:
                self._state["current"] = SLULBRULT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'dralkrart', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'dralkrart',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"dralkrart->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slulbrult(self, hint):
        assert self._state.get("current") == SLULBRULT, \
            f"sparflax.slulbrult: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slulbrult', 2:
                self._state["current"] = DRAXBRAXBLON
                self._state["trig"]    = "hint:2"
            case 'slulbrult', _:
                self._state["current"] = SLARSPIMKRAR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slulbrult', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slulbrult',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slulbrult->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slarspimkrar(self, hint):
        assert self._state.get("current") == SLARSPIMKRAR, \
            f"sparflax.slarspimkrar: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slarspimkrar', 2:
                self._state["current"] = DRAXBRAXBLON
                self._state["trig"]    = "hint:2"
            case 'slarspimkrar', _:
                self._state["current"] = PRIMGRENDRENX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slarspimkrar', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slarspimkrar',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slarspimkrar->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _primgrendrenx(self, hint):
        assert self._state.get("current") == PRIMGRENDRENX, \
            f"sparflax.primgrendrenx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'primgrendrenx', 2:
                self._state["current"] = DRAXBRAXBLON
                self._state["trig"]    = "hint:2"
            case 'primgrendrenx', _:
                self._state["current"] = PRULSLORDRUR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'primgrendrenx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'primgrendrenx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"primgrendrenx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _prulslordrur(self, hint):
        assert self._state.get("current") == PRULSLORDRUR, \
            f"sparflax.prulslordrur: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'prulslordrur', 2:
                self._state["current"] = DRAXBRAXBLON
                self._state["trig"]    = "hint:2"
            case 'prulslordrur', 1:
                self._state["current"] = GRIMGLARN
                self._state["trig"]    = "hint:1"
            case 'prulslordrur', _:
                self._state["current"] = PRENSTON
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'prulslordrur', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'prulslordrur',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"prulslordrur->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _prenston(self, hint):
        assert self._state.get("current") == PRENSTON, \
            f"sparflax.prenston: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'prenston', 2:
                self._state["current"] = DRAXBRAXBLON
                self._state["trig"]    = "hint:2"
            case 'prenston', _:
                self._state["current"] = GRIMGLARN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'prenston', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'prenston',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"prenston->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _grimglarn(self, hint):
        assert self._state.get("current") == GRIMGLARN, \
            f"sparflax.grimglarn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'grimglarn', 2:
                self._state["current"] = DRAXBRAXBLON
                self._state["trig"]    = "hint:2"
            case 'grimglarn', 0:
                self._state["current"] = BRENSLORX
                self._state["trig"]    = "hint:0"
            case 'grimglarn', _:
                self._state["current"] = KRENSKAXBLEXN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'grimglarn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'grimglarn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"grimglarn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _krenskaxblexn(self, hint):
        assert self._state.get("current") == KRENSKAXBLEXN, \
            f"sparflax.krenskaxblexn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'krenskaxblexn', 2:
                self._state["current"] = DRAXBRAXBLON
                self._state["trig"]    = "hint:2"
            case 'krenskaxblexn', _:
                self._state["current"] = BRENSLORX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'krenskaxblexn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'krenskaxblexn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"krenskaxblexn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brenslorx(self, hint):
        assert self._state.get("current") == BRENSLORX, \
            f"sparflax.brenslorx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brenslorx', 2:
                self._state["current"] = DRAXBRAXBLON
                self._state["trig"]    = "hint:2"
            case 'brenslorx', _:
                self._state["current"] = STARTRENVAX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brenslorx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brenslorx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brenslorx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _startrenvax(self, hint):
        assert self._state.get("current") == STARTRENVAX, \
            f"sparflax.startrenvax: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'startrenvax', 2:
                self._state["current"] = DRAXBRAXBLON
                self._state["trig"]    = "hint:2"
            case 'startrenvax', 0:
                self._state["current"] = CLIMVAXR
                self._state["trig"]    = "hint:0"
            case 'startrenvax', _:
                self._state["current"] = PRELGREXVOR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'startrenvax', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'startrenvax',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"startrenvax->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _prelgrexvor(self, hint):
        assert self._state.get("current") == PRELGREXVOR, \
            f"sparflax.prelgrexvor: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'prelgrexvor', 2:
                self._state["current"] = DRAXBRAXBLON
                self._state["trig"]    = "hint:2"
            case 'prelgrexvor', 0:
                self._state["current"] = TRANCLALSTONL
                self._state["trig"]    = "hint:0"
            case 'prelgrexvor', _:
                self._state["current"] = CLIMVAXR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'prelgrexvor', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'prelgrexvor',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"prelgrexvor->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _climvaxr(self, hint):
        assert self._state.get("current") == CLIMVAXR, \
            f"sparflax.climvaxr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'climvaxr', 2:
                self._state["current"] = DRAXBRAXBLON
                self._state["trig"]    = "hint:2"
            case 'climvaxr', 1:
                self._state["current"] = GLORBRALTREXR
                self._state["trig"]    = "hint:1"
            case 'climvaxr', _:
                self._state["current"] = TRANCLALSTONL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'climvaxr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'climvaxr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"climvaxr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _tranclalstonl(self, hint):
        assert self._state.get("current") == TRANCLALSTONL, \
            f"sparflax.tranclalstonl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'tranclalstonl', 2:
                self._state["current"] = DRAXBRAXBLON
                self._state["trig"]    = "hint:2"
            case 'tranclalstonl', 1:
                self._state["current"] = GLORBRALTREXR
                self._state["trig"]    = "hint:1"
            case 'tranclalstonl', _:
                self._state["current"] = TRONGRORGRONX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'tranclalstonl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'tranclalstonl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"tranclalstonl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _trongrorgronx(self, hint):
        assert self._state.get("current") == TRONGRORGRONX, \
            f"sparflax.trongrorgronx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'trongrorgronx', 2:
                self._state["current"] = DRAXBRAXBLON
                self._state["trig"]    = "hint:2"
            case 'trongrorgronx', _:
                self._state["current"] = STAXDRARSLALK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'trongrorgronx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'trongrorgronx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"trongrorgronx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _staxdrarslalk(self, hint):
        assert self._state.get("current") == STAXDRARSLALK, \
            f"sparflax.staxdrarslalk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'staxdrarslalk', 2:
                self._state["current"] = DRAXBRAXBLON
                self._state["trig"]    = "hint:2"
            case 'staxdrarslalk', 0:
                self._state["current"] = GLORBRALTREXR
                self._state["trig"]    = "hint:0"
            case 'staxdrarslalk', _:
                self._state["current"] = SKEXSLELVURT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'staxdrarslalk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'staxdrarslalk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"staxdrarslalk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skexslelvurt(self, hint):
        assert self._state.get("current") == SKEXSLELVURT, \
            f"sparflax.skexslelvurt: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skexslelvurt', 2:
                self._state["current"] = DRAXBRAXBLON
                self._state["trig"]    = "hint:2"
            case 'skexslelvurt', _:
                self._state["current"] = DRORGRELX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skexslelvurt', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skexslelvurt',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skexslelvurt->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _drorgrelx(self, hint):
        assert self._state.get("current") == DRORGRELX, \
            f"sparflax.drorgrelx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'drorgrelx', 2:
                self._state["current"] = DRAXBRAXBLON
                self._state["trig"]    = "hint:2"
            case 'drorgrelx', 0:
                self._state["current"] = KRIMPROS
                self._state["trig"]    = "hint:0"
            case 'drorgrelx', _:
                self._state["current"] = SKELVONL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'drorgrelx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'drorgrelx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"drorgrelx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skelvonl(self, hint):
        assert self._state.get("current") == SKELVONL, \
            f"sparflax.skelvonl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skelvonl', 2:
                self._state["current"] = DRAXBRAXBLON
                self._state["trig"]    = "hint:2"
            case 'skelvonl', _:
                self._state["current"] = KRIMPROS
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skelvonl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skelvonl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skelvonl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _krimpros(self, hint):
        assert self._state.get("current") == KRIMPROS, \
            f"sparflax.krimpros: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'krimpros', 2:
                self._state["current"] = DRAXBRAXBLON
                self._state["trig"]    = "hint:2"
            case 'krimpros', 0:
                self._state["current"] = GLORBRALTREXR
                self._state["trig"]    = "hint:0"
            case 'krimpros', _:
                self._state["current"] = GLALDRIMDRAN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'krimpros', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'krimpros',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"krimpros->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glaldrimdran(self, hint):
        assert self._state.get("current") == GLALDRIMDRAN, \
            f"sparflax.glaldrimdran: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glaldrimdran', 2:
                self._state["current"] = DRAXBRAXBLON
                self._state["trig"]    = "hint:2"
            case 'glaldrimdran', 0:
                self._state["current"] = VULGLALT
                self._state["trig"]    = "hint:0"
            case 'glaldrimdran', _:
                self._state["current"] = SLONSLELK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glaldrimdran', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glaldrimdran',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glaldrimdran->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slonslelk(self, hint):
        assert self._state.get("current") == SLONSLELK, \
            f"sparflax.slonslelk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slonslelk', 2:
                self._state["current"] = DRAXBRAXBLON
                self._state["trig"]    = "hint:2"
            case 'slonslelk', 0:
                self._state["current"] = GLORBRALTREXR
                self._state["trig"]    = "hint:0"
            case 'slonslelk', _:
                self._state["current"] = VULGLALT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slonslelk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slonslelk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slonslelk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _vulglalt(self, hint):
        assert self._state.get("current") == VULGLALT, \
            f"sparflax.vulglalt: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'vulglalt', 2:
                self._state["current"] = DRAXBRAXBLON
                self._state["trig"]    = "hint:2"
            case 'vulglalt', 0:
                self._state["current"] = SPONKRARSTON
                self._state["trig"]    = "hint:0"
            case 'vulglalt', _:
                self._state["current"] = TRENPREXX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'vulglalt', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'vulglalt',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"vulglalt->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _trenprexx(self, hint):
        assert self._state.get("current") == TRENPREXX, \
            f"sparflax.trenprexx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'trenprexx', 2:
                self._state["current"] = DRAXBRAXBLON
                self._state["trig"]    = "hint:2"
            case 'trenprexx', _:
                self._state["current"] = SPONKRARSTON
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'trenprexx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'trenprexx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"trenprexx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _sponkrarston(self, hint):
        assert self._state.get("current") == SPONKRARSTON, \
            f"sparflax.sponkrarston: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'sponkrarston', 2:
                self._state["current"] = DRAXBRAXBLON
                self._state["trig"]    = "hint:2"
            case 'sponkrarston', _:
                self._state["current"] = BRORFLANX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'sponkrarston', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'sponkrarston',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"sponkrarston->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brorflanx(self, hint):
        assert self._state.get("current") == BRORFLANX, \
            f"sparflax.brorflanx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brorflanx', 2:
                self._state["current"] = DRAXBRAXBLON
                self._state["trig"]    = "hint:2"
            case 'brorflanx', 1:
                self._state["current"] = GLORBRALTREXR
                self._state["trig"]    = "hint:1"
            case 'brorflanx', _:
                self._state["current"] = KREXSPIXCLEL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brorflanx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brorflanx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brorflanx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _krexspixclel(self, hint):
        assert self._state.get("current") == KREXSPIXCLEL, \
            f"sparflax.krexspixclel: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'krexspixclel', 2:
                self._state["current"] = DRAXBRAXBLON
                self._state["trig"]    = "hint:2"
            case 'krexspixclel', 1:
                self._state["current"] = KRULPROS
                self._state["trig"]    = "hint:1"
            case 'krexspixclel', _:
                self._state["current"] = BLORSKEN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'krexspixclel', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'krexspixclel',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"krexspixclel->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _blorsken(self, hint):
        assert self._state.get("current") == BLORSKEN, \
            f"sparflax.blorsken: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'blorsken', 2:
                self._state["current"] = DRAXBRAXBLON
                self._state["trig"]    = "hint:2"
            case 'blorsken', _:
                self._state["current"] = KRULPROS
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'blorsken', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'blorsken',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"blorsken->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _krulpros(self, hint):
        assert self._state.get("current") == KRULPROS, \
            f"sparflax.krulpros: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'krulpros', 2:
                self._state["current"] = DRAXBRAXBLON
                self._state["trig"]    = "hint:2"
            case 'krulpros', 0:
                self._state["current"] = GLORBRALTREXR
                self._state["trig"]    = "hint:0"
            case 'krulpros', _:
                self._state["current"] = FLALSTIXTRAX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'krulpros', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'krulpros',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"krulpros->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _flalstixtrax(self, hint):
        assert self._state.get("current") == FLALSTIXTRAX, \
            f"sparflax.flalstixtrax: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'flalstixtrax', 2:
                self._state["current"] = DRAXBRAXBLON
                self._state["trig"]    = "hint:2"
            case 'flalstixtrax', _:
                self._state["current"] = FLANPRALX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'flalstixtrax', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'flalstixtrax',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"flalstixtrax->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _flanpralx(self, hint):
        assert self._state.get("current") == FLANPRALX, \
            f"sparflax.flanpralx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'flanpralx', 2:
                self._state["current"] = DRAXBRAXBLON
                self._state["trig"]    = "hint:2"
            case 'flanpralx', 0:
                self._state["current"] = SPURSKULK
                self._state["trig"]    = "hint:0"
            case 'flanpralx', _:
                self._state["current"] = VELBREN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'flanpralx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'flanpralx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"flanpralx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _velbren(self, hint):
        assert self._state.get("current") == VELBREN, \
            f"sparflax.velbren: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'velbren', 2:
                self._state["current"] = DRAXBRAXBLON
                self._state["trig"]    = "hint:2"
            case 'velbren', 1:
                self._state["current"] = VONPRELGRIM
                self._state["trig"]    = "hint:1"
            case 'velbren', _:
                self._state["current"] = SPURSKULK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'velbren', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'velbren',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"velbren->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _spurskulk(self, hint):
        assert self._state.get("current") == SPURSKULK, \
            f"sparflax.spurskulk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'spurskulk', 2:
                self._state["current"] = DRAXBRAXBLON
                self._state["trig"]    = "hint:2"
            case 'spurskulk', 0:
                self._state["current"] = GLORBRALTREXR
                self._state["trig"]    = "hint:0"
            case 'spurskulk', _:
                self._state["current"] = VONPRELGRIM
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'spurskulk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'spurskulk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"spurskulk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _vonprelgrim(self, hint):
        assert self._state.get("current") == VONPRELGRIM, \
            f"sparflax.vonprelgrim: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'vonprelgrim', 2:
                self._state["current"] = DRAXBRAXBLON
                self._state["trig"]    = "hint:2"
            case 'vonprelgrim', _:
                self._state["current"] = CLALSPALDRIML
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'vonprelgrim', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'vonprelgrim',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"vonprelgrim->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _clalspaldriml(self, hint):
        assert self._state.get("current") == CLALSPALDRIML, \
            f"sparflax.clalspaldriml: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'clalspaldriml', 2:
                self._state["current"] = DRAXBRAXBLON
                self._state["trig"]    = "hint:2"
            case 'clalspaldriml', _:
                self._state["current"] = GRONGLARGRARR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'clalspaldriml', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'clalspaldriml',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"clalspaldriml->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _gronglargrarr(self, hint):
        assert self._state.get("current") == GRONGLARGRARR, \
            f"sparflax.gronglargrarr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'gronglargrarr', 2:
                self._state["current"] = DRAXBRAXBLON
                self._state["trig"]    = "hint:2"
            case 'gronglargrarr', 0:
                self._state["current"] = BRARGRURSKULR
                self._state["trig"]    = "hint:0"
            case 'gronglargrarr', _:
                self._state["current"] = FLONBLIXSPORL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'gronglargrarr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'gronglargrarr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"gronglargrarr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _flonblixsporl(self, hint):
        assert self._state.get("current") == FLONBLIXSPORL, \
            f"sparflax.flonblixsporl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'flonblixsporl', 2:
                self._state["current"] = DRAXBRAXBLON
                self._state["trig"]    = "hint:2"
            case 'flonblixsporl', _:
                self._state["current"] = BRARGRURSKULR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'flonblixsporl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'flonblixsporl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"flonblixsporl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brargrurskulr(self, hint):
        assert self._state.get("current") == BRARGRURSKULR, \
            f"sparflax.brargrurskulr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brargrurskulr', 2:
                self._state["current"] = DRAXBRAXBLON
                self._state["trig"]    = "hint:2"
            case 'brargrurskulr', _:
                self._state["current"] = KRORCLURTRUL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brargrurskulr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brargrurskulr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brargrurskulr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _krorclurtrul(self, hint):
        assert self._state.get("current") == KRORCLURTRUL, \
            f"sparflax.krorclurtrul: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'krorclurtrul', 2:
                self._state["current"] = DRAXBRAXBLON
                self._state["trig"]    = "hint:2"
            case 'krorclurtrul', 1:
                self._state["current"] = GLORBRALTREXR
                self._state["trig"]    = "hint:1"
            case 'krorclurtrul', _:
                self._state["current"] = GLENTROS
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'krorclurtrul', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'krorclurtrul',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"krorclurtrul->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glentros(self, hint):
        assert self._state.get("current") == GLENTROS, \
            f"sparflax.glentros: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glentros', 2:
                self._state["current"] = DRAXBRAXBLON
                self._state["trig"]    = "hint:2"
            case 'glentros', 0:
                self._state["current"] = GLORBRALTREXR
                self._state["trig"]    = "hint:0"
            case 'glentros', _:
                self._state["current"] = GRANTRURSKAL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glentros', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glentros',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glentros->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _grantrurskal(self, hint):
        assert self._state.get("current") == GRANTRURSKAL, \
            f"sparflax.grantrurskal: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'grantrurskal', 2:
                self._state["current"] = DRAXBRAXBLON
                self._state["trig"]    = "hint:2"
            case 'grantrurskal', 1:
                self._state["current"] = GLORBRALTREXR
                self._state["trig"]    = "hint:1"
            case 'grantrurskal', _:
                self._state["current"] = SPORBLELR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'grantrurskal', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'grantrurskal',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"grantrurskal->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _sporblelr(self, hint):
        assert self._state.get("current") == SPORBLELR, \
            f"sparflax.sporblelr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'sporblelr', 2:
                self._state["current"] = DRAXBRAXBLON
                self._state["trig"]    = "hint:2"
            case 'sporblelr', 1:
                self._state["current"] = GLORBRALTREXR
                self._state["trig"]    = "hint:1"
            case 'sporblelr', _:
                self._state["current"] = STENBLANX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'sporblelr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'sporblelr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"sporblelr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _stenblanx(self, hint):
        assert self._state.get("current") == STENBLANX, \
            f"sparflax.stenblanx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'stenblanx', 2:
                self._state["current"] = DRAXBRAXBLON
                self._state["trig"]    = "hint:2"
            case 'stenblanx', 1:
                self._state["current"] = TRULSKORBRALT
                self._state["trig"]    = "hint:1"
            case 'stenblanx', _:
                self._state["current"] = SKOSFLAXBLIXK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'stenblanx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'stenblanx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"stenblanx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _skosflaxblixk(self, hint):
        assert self._state.get("current") == SKOSFLAXBLIXK, \
            f"sparflax.skosflaxblixk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'skosflaxblixk', 2:
                self._state["current"] = DRAXBRAXBLON
                self._state["trig"]    = "hint:2"
            case 'skosflaxblixk', 0:
                self._state["current"] = GLORBRALTREXR
                self._state["trig"]    = "hint:0"
            case 'skosflaxblixk', _:
                self._state["current"] = TRULSKORBRALT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'skosflaxblixk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'skosflaxblixk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"skosflaxblixk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _trulskorbralt(self, hint):
        assert self._state.get("current") == TRULSKORBRALT, \
            f"sparflax.trulskorbralt: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'trulskorbralt', 2:
                self._state["current"] = DRAXBRAXBLON
                self._state["trig"]    = "hint:2"
            case 'trulskorbralt', _:
                self._state["current"] = GRONBRIMX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'trulskorbralt', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'trulskorbralt',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"trulskorbralt->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _gronbrimx(self, hint):
        assert self._state.get("current") == GRONBRIMX, \
            f"sparflax.gronbrimx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'gronbrimx', 2:
                self._state["current"] = DRAXBRAXBLON
                self._state["trig"]    = "hint:2"
            case 'gronbrimx', _:
                self._state["current"] = GLIXTRARVAX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'gronbrimx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'gronbrimx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"gronbrimx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glixtrarvax(self, hint):
        assert self._state.get("current") == GLIXTRARVAX, \
            f"sparflax.glixtrarvax: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glixtrarvax', 2:
                self._state["current"] = DRAXBRAXBLON
                self._state["trig"]    = "hint:2"
            case 'glixtrarvax', _:
                self._state["current"] = PRAXPRIMTRIMX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glixtrarvax', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glixtrarvax',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glixtrarvax->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _praxprimtrimx(self, hint):
        assert self._state.get("current") == PRAXPRIMTRIMX, \
            f"sparflax.praxprimtrimx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'praxprimtrimx', 2:
                self._state["current"] = DRAXBRAXBLON
                self._state["trig"]    = "hint:2"
            case 'praxprimtrimx', 1:
                self._state["current"] = DRANBRENTRIXL
                self._state["trig"]    = "hint:1"
            case 'praxprimtrimx', _:
                self._state["current"] = GRONGRURCLOSN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'praxprimtrimx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'praxprimtrimx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"praxprimtrimx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _grongrurclosn(self, hint):
        assert self._state.get("current") == GRONGRURCLOSN, \
            f"sparflax.grongrurclosn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'grongrurclosn', 2:
                self._state["current"] = DRAXBRAXBLON
                self._state["trig"]    = "hint:2"
            case 'grongrurclosn', _:
                self._state["current"] = DRANBRENTRIXL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'grongrurclosn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'grongrurclosn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"grongrurclosn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _dranbrentrixl(self, hint):
        assert self._state.get("current") == DRANBRENTRIXL, \
            f"sparflax.dranbrentrixl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'dranbrentrixl', 2:
                self._state["current"] = DRAXBRAXBLON
                self._state["trig"]    = "hint:2"
            case 'dranbrentrixl', _:
                self._state["current"] = SLOSSLEN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'dranbrentrixl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'dranbrentrixl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"dranbrentrixl->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slosslen(self, hint):
        assert self._state.get("current") == SLOSSLEN, \
            f"sparflax.slosslen: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slosslen', 2:
                self._state["current"] = DRAXBRAXBLON
                self._state["trig"]    = "hint:2"
            case 'slosslen', 0:
                self._state["current"] = GRURPRIM
                self._state["trig"]    = "hint:0"
            case 'slosslen', _:
                self._state["current"] = GLAXFLENSPURX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slosslen', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slosslen',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slosslen->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glaxflenspurx(self, hint):
        assert self._state.get("current") == GLAXFLENSPURX, \
            f"sparflax.glaxflenspurx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glaxflenspurx', 2:
                self._state["current"] = DRAXBRAXBLON
                self._state["trig"]    = "hint:2"
            case 'glaxflenspurx', _:
                self._state["current"] = GRURPRIM
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glaxflenspurx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glaxflenspurx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glaxflenspurx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _grurprim(self, hint):
        assert self._state.get("current") == GRURPRIM, \
            f"sparflax.grurprim: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'grurprim', 2:
                self._state["current"] = DRAXBRAXBLON
                self._state["trig"]    = "hint:2"
            case 'grurprim', _:
                self._state["current"] = CLIMSPIX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'grurprim', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'grurprim',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"grurprim->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _climspix(self, hint):
        assert self._state.get("current") == CLIMSPIX, \
            f"sparflax.climspix: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'climspix', 2:
                self._state["current"] = DRAXBRAXBLON
                self._state["trig"]    = "hint:2"
            case 'climspix', 0:
                self._state["current"] = GLORBRALTREXR
                self._state["trig"]    = "hint:0"
            case 'climspix', _:
                self._state["current"] = BRIMBRANT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'climspix', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'climspix',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"climspix->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _brimbrant(self, hint):
        assert self._state.get("current") == BRIMBRANT, \
            f"sparflax.brimbrant: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'brimbrant', 2:
                self._state["current"] = DRAXBRAXBLON
                self._state["trig"]    = "hint:2"
            case 'brimbrant', 0:
                self._state["current"] = GLORBRALTREXR
                self._state["trig"]    = "hint:0"
            case 'brimbrant', _:
                self._state["current"] = GLORSPENDREXN
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'brimbrant', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'brimbrant',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"brimbrant->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _glorspendrexn(self, hint):
        assert self._state.get("current") == GLORSPENDREXN, \
            f"sparflax.glorspendrexn: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'glorspendrexn', 2:
                self._state["current"] = DRAXBRAXBLON
                self._state["trig"]    = "hint:2"
            case 'glorspendrexn', 1:
                self._state["current"] = GLORBRALTREXR
                self._state["trig"]    = "hint:1"
            case 'glorspendrexn', _:
                self._state["current"] = DRARTRURBLUR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'glorspendrexn', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'glorspendrexn',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"glorspendrexn->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _drartrurblur(self, hint):
        assert self._state.get("current") == DRARTRURBLUR, \
            f"sparflax.drartrurblur: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'drartrurblur', 2:
                self._state["current"] = DRAXBRAXBLON
                self._state["trig"]    = "hint:2"
            case 'drartrurblur', 1:
                self._state["current"] = GRENSKIMX
                self._state["trig"]    = "hint:1"
            case 'drartrurblur', _:
                self._state["current"] = GROSGLANX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'drartrurblur', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'drartrurblur',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"drartrurblur->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _grosglanx(self, hint):
        assert self._state.get("current") == GROSGLANX, \
            f"sparflax.grosglanx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'grosglanx', 2:
                self._state["current"] = DRAXBRAXBLON
                self._state["trig"]    = "hint:2"
            case 'grosglanx', _:
                self._state["current"] = GRENSKIMX
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'grosglanx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'grosglanx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"grosglanx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _grenskimx(self, hint):
        assert self._state.get("current") == GRENSKIMX, \
            f"sparflax.grenskimx: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'grenskimx', 2:
                self._state["current"] = DRAXBRAXBLON
                self._state["trig"]    = "hint:2"
            case 'grenskimx', 1:
                self._state["current"] = SLIMSPELT
                self._state["trig"]    = "hint:1"
            case 'grenskimx', _:
                self._state["current"] = GRARGRIMSLEXK
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'grenskimx', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'grenskimx',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"grenskimx->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _grargrimslexk(self, hint):
        assert self._state.get("current") == GRARGRIMSLEXK, \
            f"sparflax.grargrimslexk: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'grargrimslexk', 2:
                self._state["current"] = DRAXBRAXBLON
                self._state["trig"]    = "hint:2"
            case 'grargrimslexk', 0:
                self._state["current"] = FLURFLAXR
                self._state["trig"]    = "hint:0"
            case 'grargrimslexk', _:
                self._state["current"] = SLIMSPELT
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'grargrimslexk', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'grargrimslexk',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"grargrimslexk->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _slimspelt(self, hint):
        assert self._state.get("current") == SLIMSPELT, \
            f"sparflax.slimspelt: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'slimspelt', 2:
                self._state["current"] = DRAXBRAXBLON
                self._state["trig"]    = "hint:2"
            case 'slimspelt', _:
                self._state["current"] = FLURFLAXR
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'slimspelt', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'slimspelt',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"slimspelt->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _flurflaxr(self, hint):
        assert self._state.get("current") == FLURFLAXR, \
            f"sparflax.flurflaxr: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'flurflaxr', 2:
                self._state["current"] = DRAXBRAXBLON
                self._state["trig"]    = "hint:2"
            case 'flurflaxr', _:
                self._state["current"] = CLOSSKANSTAXL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'flurflaxr', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'flurflaxr',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"flurflaxr->{_to}", _xid_val)
        self._state["cycle"] += 1

    def _closskanstaxl(self, hint):
        assert self._state.get("current") == CLOSSKANSTAXL, \
            f"sparflax.closskanstaxl: wrong state {self._state.get('current')}"
        _hint_branch = hint is not None and hint != 2
        match self._state["current"], hint:
            case 'closskanstaxl', 2:
                self._state["current"] = DRAXBRAXBLON
                self._state["trig"]    = "hint:2"
            case 'closskanstaxl', _:
                self._state["current"] = VALPRURL
                self._state["trig"]    = "auto"
        _to   = self._state["current"]
        _trig = self._state["trig"]
        _xid_val = _xid(__name__, 'closskanstaxl', _to, _trig)
        _conds = {"hint_branch": _hint_branch}
        _emit(self._state["cycle"], 1, __name__, 'closskanstaxl',
              {"hint": hint, "span": self._state.get("span"),
               "caller": self._state.get("caller")},
              dict(self._state["ctx"]), _conds,
              f"closskanstaxl->{_to}", _xid_val)
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
            _xid_val = _xid(__name__, 'brenclorstaxn', "error", "assert_fail")
            _emit(cycle, 1, __name__, 'brenclorstaxn',
                   {"hint": hint, "span": span, "caller": caller},
                   dict(ctx), _conds,
                   "entry_blocked->error", _xid_val, assertion=_asrt)
            return 2, cycle + 1

        self._state = {"current": BRENCLORSTAXN, "ctx": ctx,
                        "span": span, "caller": caller,
                        "trig": "auto", "cycle": cycle}
        _dispatch = {
            BRENCLORSTAXN: self._brenclorstaxn,
            SLORKRULN: self._slorkruln,
            KREXFLALBRON: self._krexflalbron,
            DRALKRART: self._dralkrart,
            SLULBRULT: self._slulbrult,
            SLARSPIMKRAR: self._slarspimkrar,
            PRIMGRENDRENX: self._primgrendrenx,
            PRULSLORDRUR: self._prulslordrur,
            PRENSTON: self._prenston,
            GRIMGLARN: self._grimglarn,
            KRENSKAXBLEXN: self._krenskaxblexn,
            BRENSLORX: self._brenslorx,
            STARTRENVAX: self._startrenvax,
            PRELGREXVOR: self._prelgrexvor,
            CLIMVAXR: self._climvaxr,
            TRANCLALSTONL: self._tranclalstonl,
            TRONGRORGRONX: self._trongrorgronx,
            STAXDRARSLALK: self._staxdrarslalk,
            SKEXSLELVURT: self._skexslelvurt,
            DRORGRELX: self._drorgrelx,
            SKELVONL: self._skelvonl,
            KRIMPROS: self._krimpros,
            GLALDRIMDRAN: self._glaldrimdran,
            SLONSLELK: self._slonslelk,
            VULGLALT: self._vulglalt,
            TRENPREXX: self._trenprexx,
            SPONKRARSTON: self._sponkrarston,
            BRORFLANX: self._brorflanx,
            KREXSPIXCLEL: self._krexspixclel,
            BLORSKEN: self._blorsken,
            KRULPROS: self._krulpros,
            FLALSTIXTRAX: self._flalstixtrax,
            FLANPRALX: self._flanpralx,
            VELBREN: self._velbren,
            SPURSKULK: self._spurskulk,
            VONPRELGRIM: self._vonprelgrim,
            CLALSPALDRIML: self._clalspaldriml,
            GRONGLARGRARR: self._gronglargrarr,
            FLONBLIXSPORL: self._flonblixsporl,
            BRARGRURSKULR: self._brargrurskulr,
            KRORCLURTRUL: self._krorclurtrul,
            GLENTROS: self._glentros,
            GRANTRURSKAL: self._grantrurskal,
            SPORBLELR: self._sporblelr,
            STENBLANX: self._stenblanx,
            SKOSFLAXBLIXK: self._skosflaxblixk,
            TRULSKORBRALT: self._trulskorbralt,
            GRONBRIMX: self._gronbrimx,
            GLIXTRARVAX: self._glixtrarvax,
            PRAXPRIMTRIMX: self._praxprimtrimx,
            GRONGRURCLOSN: self._grongrurclosn,
            DRANBRENTRIXL: self._dranbrentrixl,
            SLOSSLEN: self._slosslen,
            GLAXFLENSPURX: self._glaxflenspurx,
            GRURPRIM: self._grurprim,
            CLIMSPIX: self._climspix,
            BRIMBRANT: self._brimbrant,
            GLORSPENDREXN: self._glorspendrexn,
            DRARTRURBLUR: self._drartrurblur,
            GROSGLANX: self._grosglanx,
            GRENSKIMX: self._grenskimx,
            GRARGRIMSLEXK: self._grargrimslexk,
            SLIMSPELT: self._slimspelt,
            FLURFLAXR: self._flurflaxr,
            CLOSSKANSTAXL: self._closskanstaxl,
        }
        while self._state["current"] not in _R and self._state["cycle"] - cycle < 8000:
            _dispatch[self._state["current"]](hint)
        _ret     = _R.get(self._state["current"], -1)
        _is_err  = self._state["current"] == DRAXBRAXBLON
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
    return SparflaxFSM().invoke(hint=hint, span=span, caller=caller, ctx=ctx, cycle=cycle)
