import sys, os, uuid as _uu
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _log import _w as _emit, _new_trace, _run_start, _xid

import blalston
import blixflimx
import blorbrulk
import blosvurl
import bralskenl
import brorstorn
import clalclexr
import clelvall
import clexblalt
import clulgraxl
import dreltrell
import drixslim
import drosblosl
import flaxclimn
import flelskalk
import flelslull
import flelspult
import glaltrimr
import glanskelx
import glaxglall
import grixprark
import krondral
import prelspalk
import prelvonx
import skalsposx
import skanpronn
import slonstex
import sparflax
import spaxglan
import spaxglosx
import trenblort
import trorbran

SLALSLEX = 'slalslex'
SLOSDRAR = 'slosdrar'
VIXFLOS = 'vixflos'
STURVEL = 'sturvel'
TRAXDRENT = 'traxdrent'
SKENBLELBLONN = 'skenblelblonn'
SKULBRON = 'skulbron'
BLURTRAR = 'blurtrar'
VIMSTOSK = 'vimstosk'
STURGLELL = 'sturglell'
BRULSPEX = 'brulspex'
CLIMFLAR = 'climflar'
GLARVAXX = 'glarvaxx'
TRORSLORSLEN = 'trorslorslen'
TRANGROSGLIMR = 'trangrosglimr'
STAXSKORKRAR = 'staxskorkrar'
CLALSTEXPREN = 'clalstexpren'
GRURSKENGLON = 'grurskenglon'
KREXKRAXSPEL = 'krexkraxspel'
GRANKROSVANL = 'grankrosvanl'
PRIXSPALSLIXX = 'prixspalslixx'
PROSSLOSL = 'prosslosl'
DRIXVENGRARX = 'drixvengrarx'
FLONKRALDRAXN = 'flonkraldraxn'
TRIMSPONBRORK = 'trimsponbrork'
TRARSLAL = 'trarslal'
PRULKRONVORN = 'prulkronvorn'
SLENSTIX = 'slenstix'
FLIXGLOSN = 'flixglosn'
CLORBLOSX = 'clorblosx'
SLOSPRAN = 'slospran'
VULCLAN = 'vulclan'
TRAXBRORN = 'traxbrorn'

_TERM      = TRAXBRORN
_MAX_STEPS = 8000
_MAX_ERR   = 4
_CTX_KEYS  = ['flurslex', 'spenbranl']
_SEED      = 42

_H = {
    SLALSLEX: 0,
    SLOSDRAR: 0,
    VIXFLOS: None,
    STURVEL: 1,
    TRAXDRENT: None,
    SKENBLELBLONN: 0,
    SKULBRON: 0,
    BLURTRAR: 1,
    VIMSTOSK: 1,
    STURGLELL: None,
    BRULSPEX: 1,
    CLIMFLAR: 0,
    GLARVAXX: None,
    TRORSLORSLEN: None,
    TRANGROSGLIMR: 0,
    STAXSKORKRAR: 0,
    CLALSTEXPREN: 0,
    GRURSKENGLON: 0,
    KREXKRAXSPEL: 0,
    GRANKROSVANL: 1,
    PRIXSPALSLIXX: 0,
    PROSSLOSL: 1,
    DRIXVENGRARX: 1,
    FLONKRALDRAXN: 0,
    TRIMSPONBRORK: 0,
    TRARSLAL: None,
    PRULKRONVORN: 0,
    SLENSTIX: None,
    FLIXGLOSN: 1,
    CLORBLOSX: None,
    SLOSPRAN: 0,
    VULCLAN: None,
}

class FlimblorxFSM:
    def __init__(self):
        self._state = {}

    def _slalslex(self, fault_hint):
        assert self._state.get("current") == SLALSLEX, \
            f"flimblorx.slalslex: wrong state {self._state.get('current')}"
        _hint          = fault_hint if fault_hint is not None else _H[SLALSLEX]
        _span          = _uu.uuid4().hex[:8]
        _vars_before   = dict(self._state["ctx"])
        _pre_xid = _xid(__name__, 'slalslex', "invoke:prelvonx", "pre")
        _emit(self._state["cycle"], 0, __name__, 'slalslex',
               {"fault_hint": fault_hint, "sub": 'prelvonx',
                "span": _span, "hint": _hint},
               _vars_before, {},
               f"slalslex->invoke:prelvonx", _pre_xid)
        self._state["cycle"] += 1

        _ret, _next_cycle = prelvonx.invoke(
            hint=_hint, span=_span, caller=SLALSLEX,
            ctx=self._state["ctx"], cycle=self._state["cycle"])
        self._state["cycle"] = _next_cycle

        _is_err = _ret == 2
        if _is_err:
            self._state["err_ct"] += 1
        else:
            self._state["err_ct"] = 0
        self._state["last_ret"] = _ret
        match self._state["current"], _ret:
            case 'slalslex', 0:
                self._state["current"] = SLOSDRAR
            case 'slalslex', 1:
                self._state["current"] = STURVEL
            case 'slalslex', 2:
                self._state["current"] = SLALSLEX
        _to = self._state["current"]
        _asrt = "pass"
        if self._state["err_ct"] > _MAX_ERR:
            _asrt = {"failed": "err_budget",
                       "expected": f"err_ct <= {_MAX_ERR}",
                       "actual":   f"err_ct == {self._state['err_ct']}"}
        _post_xid = _xid(__name__, 'slalslex', _to, f"ret:{_ret}")
        _emit(self._state["cycle"], 0, __name__, 'slalslex',
               {"fault_hint": fault_hint, "sub": 'prelvonx',
                "span": _span, "ret": _ret},
               dict(self._state["ctx"]),
               {"sub_error": _is_err, "err_ct": self._state["err_ct"]},
               f"slalslex->{_to}", _post_xid,
               assertion=_asrt, variables_before=_vars_before)
        self._state["cycle"] += 1
        return _asrt

    def _slosdrar(self, fault_hint):
        assert self._state.get("current") == SLOSDRAR, \
            f"flimblorx.slosdrar: wrong state {self._state.get('current')}"
        _hint          = fault_hint if fault_hint is not None else _H[SLOSDRAR]
        _span          = _uu.uuid4().hex[:8]
        _vars_before   = dict(self._state["ctx"])
        _pre_xid = _xid(__name__, 'slosdrar', "invoke:krondral", "pre")
        _emit(self._state["cycle"], 0, __name__, 'slosdrar',
               {"fault_hint": fault_hint, "sub": 'krondral',
                "span": _span, "hint": _hint},
               _vars_before, {},
               f"slosdrar->invoke:krondral", _pre_xid)
        self._state["cycle"] += 1

        _ret, _next_cycle = krondral.invoke(
            hint=_hint, span=_span, caller=SLOSDRAR,
            ctx=self._state["ctx"], cycle=self._state["cycle"])
        self._state["cycle"] = _next_cycle

        _is_err = _ret == 2
        if _is_err:
            self._state["err_ct"] += 1
        else:
            self._state["err_ct"] = 0
        self._state["last_ret"] = _ret
        match self._state["current"], _ret:
            case 'slosdrar', 0:
                self._state["current"] = VIXFLOS
            case 'slosdrar', 1:
                self._state["current"] = VIXFLOS
            case 'slosdrar', 2:
                self._state["current"] = SLOSDRAR
        _to = self._state["current"]
        _asrt = "pass"
        if self._state["err_ct"] > _MAX_ERR:
            _asrt = {"failed": "err_budget",
                       "expected": f"err_ct <= {_MAX_ERR}",
                       "actual":   f"err_ct == {self._state['err_ct']}"}
        _post_xid = _xid(__name__, 'slosdrar', _to, f"ret:{_ret}")
        _emit(self._state["cycle"], 0, __name__, 'slosdrar',
               {"fault_hint": fault_hint, "sub": 'krondral',
                "span": _span, "ret": _ret},
               dict(self._state["ctx"]),
               {"sub_error": _is_err, "err_ct": self._state["err_ct"]},
               f"slosdrar->{_to}", _post_xid,
               assertion=_asrt, variables_before=_vars_before)
        self._state["cycle"] += 1
        return _asrt

    def _vixflos(self, fault_hint):
        assert self._state.get("current") == VIXFLOS, \
            f"flimblorx.vixflos: wrong state {self._state.get('current')}"
        _hint          = fault_hint if fault_hint is not None else _H[VIXFLOS]
        _span          = _uu.uuid4().hex[:8]
        _vars_before   = dict(self._state["ctx"])
        _pre_xid = _xid(__name__, 'vixflos', "invoke:flelspult", "pre")
        _emit(self._state["cycle"], 0, __name__, 'vixflos',
               {"fault_hint": fault_hint, "sub": 'flelspult',
                "span": _span, "hint": _hint},
               _vars_before, {},
               f"vixflos->invoke:flelspult", _pre_xid)
        self._state["cycle"] += 1

        _ret, _next_cycle = flelspult.invoke(
            hint=_hint, span=_span, caller=VIXFLOS,
            ctx=self._state["ctx"], cycle=self._state["cycle"])
        self._state["cycle"] = _next_cycle

        _is_err = _ret == 2
        if _is_err:
            self._state["err_ct"] += 1
        else:
            self._state["err_ct"] = 0
        self._state["last_ret"] = _ret
        match self._state["current"], _ret:
            case 'vixflos', 0:
                self._state["current"] = STURVEL
            case 'vixflos', 1:
                self._state["current"] = SKENBLELBLONN
            case 'vixflos', 2:
                self._state["current"] = VIXFLOS
        _to = self._state["current"]
        _asrt = "pass"
        if self._state["err_ct"] > _MAX_ERR:
            _asrt = {"failed": "err_budget",
                       "expected": f"err_ct <= {_MAX_ERR}",
                       "actual":   f"err_ct == {self._state['err_ct']}"}
        _post_xid = _xid(__name__, 'vixflos', _to, f"ret:{_ret}")
        _emit(self._state["cycle"], 0, __name__, 'vixflos',
               {"fault_hint": fault_hint, "sub": 'flelspult',
                "span": _span, "ret": _ret},
               dict(self._state["ctx"]),
               {"sub_error": _is_err, "err_ct": self._state["err_ct"]},
               f"vixflos->{_to}", _post_xid,
               assertion=_asrt, variables_before=_vars_before)
        self._state["cycle"] += 1
        return _asrt

    def _sturvel(self, fault_hint):
        assert self._state.get("current") == STURVEL, \
            f"flimblorx.sturvel: wrong state {self._state.get('current')}"
        _hint          = fault_hint if fault_hint is not None else _H[STURVEL]
        _span          = _uu.uuid4().hex[:8]
        _vars_before   = dict(self._state["ctx"])
        _pre_xid = _xid(__name__, 'sturvel', "invoke:blixflimx", "pre")
        _emit(self._state["cycle"], 0, __name__, 'sturvel',
               {"fault_hint": fault_hint, "sub": 'blixflimx',
                "span": _span, "hint": _hint},
               _vars_before, {},
               f"sturvel->invoke:blixflimx", _pre_xid)
        self._state["cycle"] += 1

        _ret, _next_cycle = blixflimx.invoke(
            hint=_hint, span=_span, caller=STURVEL,
            ctx=self._state["ctx"], cycle=self._state["cycle"])
        self._state["cycle"] = _next_cycle

        _is_err = _ret == 2
        if _is_err:
            self._state["err_ct"] += 1
        else:
            self._state["err_ct"] = 0
        self._state["last_ret"] = _ret
        match self._state["current"], _ret:
            case 'sturvel', 0:
                self._state["current"] = TRAXDRENT
            case 'sturvel', 1:
                self._state["current"] = SKULBRON
            case 'sturvel', 2:
                self._state["current"] = STURVEL
        _to = self._state["current"]
        _asrt = "pass"
        if self._state["err_ct"] > _MAX_ERR:
            _asrt = {"failed": "err_budget",
                       "expected": f"err_ct <= {_MAX_ERR}",
                       "actual":   f"err_ct == {self._state['err_ct']}"}
        _post_xid = _xid(__name__, 'sturvel', _to, f"ret:{_ret}")
        _emit(self._state["cycle"], 0, __name__, 'sturvel',
               {"fault_hint": fault_hint, "sub": 'blixflimx',
                "span": _span, "ret": _ret},
               dict(self._state["ctx"]),
               {"sub_error": _is_err, "err_ct": self._state["err_ct"]},
               f"sturvel->{_to}", _post_xid,
               assertion=_asrt, variables_before=_vars_before)
        self._state["cycle"] += 1
        return _asrt

    def _traxdrent(self, fault_hint):
        assert self._state.get("current") == TRAXDRENT, \
            f"flimblorx.traxdrent: wrong state {self._state.get('current')}"
        _hint          = fault_hint if fault_hint is not None else _H[TRAXDRENT]
        _span          = _uu.uuid4().hex[:8]
        _vars_before   = dict(self._state["ctx"])
        _pre_xid = _xid(__name__, 'traxdrent', "invoke:clalclexr", "pre")
        _emit(self._state["cycle"], 0, __name__, 'traxdrent',
               {"fault_hint": fault_hint, "sub": 'clalclexr',
                "span": _span, "hint": _hint},
               _vars_before, {},
               f"traxdrent->invoke:clalclexr", _pre_xid)
        self._state["cycle"] += 1

        _ret, _next_cycle = clalclexr.invoke(
            hint=_hint, span=_span, caller=TRAXDRENT,
            ctx=self._state["ctx"], cycle=self._state["cycle"])
        self._state["cycle"] = _next_cycle

        _is_err = _ret == 2
        if _is_err:
            self._state["err_ct"] += 1
        else:
            self._state["err_ct"] = 0
        self._state["last_ret"] = _ret
        match self._state["current"], _ret:
            case 'traxdrent', 0:
                self._state["current"] = SKENBLELBLONN
            case 'traxdrent', 1:
                self._state["current"] = BLURTRAR
            case 'traxdrent', 2:
                self._state["current"] = TRAXDRENT
        _to = self._state["current"]
        _asrt = "pass"
        if self._state["err_ct"] > _MAX_ERR:
            _asrt = {"failed": "err_budget",
                       "expected": f"err_ct <= {_MAX_ERR}",
                       "actual":   f"err_ct == {self._state['err_ct']}"}
        _post_xid = _xid(__name__, 'traxdrent', _to, f"ret:{_ret}")
        _emit(self._state["cycle"], 0, __name__, 'traxdrent',
               {"fault_hint": fault_hint, "sub": 'clalclexr',
                "span": _span, "ret": _ret},
               dict(self._state["ctx"]),
               {"sub_error": _is_err, "err_ct": self._state["err_ct"]},
               f"traxdrent->{_to}", _post_xid,
               assertion=_asrt, variables_before=_vars_before)
        self._state["cycle"] += 1
        return _asrt

    def _skenblelblonn(self, fault_hint):
        assert self._state.get("current") == SKENBLELBLONN, \
            f"flimblorx.skenblelblonn: wrong state {self._state.get('current')}"
        _hint          = fault_hint if fault_hint is not None else _H[SKENBLELBLONN]
        _span          = _uu.uuid4().hex[:8]
        _vars_before   = dict(self._state["ctx"])
        _pre_xid = _xid(__name__, 'skenblelblonn', "invoke:spaxglosx", "pre")
        _emit(self._state["cycle"], 0, __name__, 'skenblelblonn',
               {"fault_hint": fault_hint, "sub": 'spaxglosx',
                "span": _span, "hint": _hint},
               _vars_before, {},
               f"skenblelblonn->invoke:spaxglosx", _pre_xid)
        self._state["cycle"] += 1

        _ret, _next_cycle = spaxglosx.invoke(
            hint=_hint, span=_span, caller=SKENBLELBLONN,
            ctx=self._state["ctx"], cycle=self._state["cycle"])
        self._state["cycle"] = _next_cycle

        _is_err = _ret == 2
        if _is_err:
            self._state["err_ct"] += 1
        else:
            self._state["err_ct"] = 0
        self._state["last_ret"] = _ret
        match self._state["current"], _ret:
            case 'skenblelblonn', 0:
                self._state["current"] = SKULBRON
            case 'skenblelblonn', 1:
                self._state["current"] = BLURTRAR
            case 'skenblelblonn', 2:
                self._state["current"] = SKENBLELBLONN
        _to = self._state["current"]
        _asrt = "pass"
        if self._state["err_ct"] > _MAX_ERR:
            _asrt = {"failed": "err_budget",
                       "expected": f"err_ct <= {_MAX_ERR}",
                       "actual":   f"err_ct == {self._state['err_ct']}"}
        _post_xid = _xid(__name__, 'skenblelblonn', _to, f"ret:{_ret}")
        _emit(self._state["cycle"], 0, __name__, 'skenblelblonn',
               {"fault_hint": fault_hint, "sub": 'spaxglosx',
                "span": _span, "ret": _ret},
               dict(self._state["ctx"]),
               {"sub_error": _is_err, "err_ct": self._state["err_ct"]},
               f"skenblelblonn->{_to}", _post_xid,
               assertion=_asrt, variables_before=_vars_before)
        self._state["cycle"] += 1
        return _asrt

    def _skulbron(self, fault_hint):
        assert self._state.get("current") == SKULBRON, \
            f"flimblorx.skulbron: wrong state {self._state.get('current')}"
        _hint          = fault_hint if fault_hint is not None else _H[SKULBRON]
        _span          = _uu.uuid4().hex[:8]
        _vars_before   = dict(self._state["ctx"])
        _pre_xid = _xid(__name__, 'skulbron', "invoke:clulgraxl", "pre")
        _emit(self._state["cycle"], 0, __name__, 'skulbron',
               {"fault_hint": fault_hint, "sub": 'clulgraxl',
                "span": _span, "hint": _hint},
               _vars_before, {},
               f"skulbron->invoke:clulgraxl", _pre_xid)
        self._state["cycle"] += 1

        _ret, _next_cycle = clulgraxl.invoke(
            hint=_hint, span=_span, caller=SKULBRON,
            ctx=self._state["ctx"], cycle=self._state["cycle"])
        self._state["cycle"] = _next_cycle

        _is_err = _ret == 2
        if _is_err:
            self._state["err_ct"] += 1
        else:
            self._state["err_ct"] = 0
        self._state["last_ret"] = _ret
        match self._state["current"], _ret:
            case 'skulbron', 0:
                self._state["current"] = BLURTRAR
            case 'skulbron', 1:
                self._state["current"] = VIMSTOSK
            case 'skulbron', 2:
                self._state["current"] = SKULBRON
        _to = self._state["current"]
        _asrt = "pass"
        if self._state["err_ct"] > _MAX_ERR:
            _asrt = {"failed": "err_budget",
                       "expected": f"err_ct <= {_MAX_ERR}",
                       "actual":   f"err_ct == {self._state['err_ct']}"}
        _post_xid = _xid(__name__, 'skulbron', _to, f"ret:{_ret}")
        _emit(self._state["cycle"], 0, __name__, 'skulbron',
               {"fault_hint": fault_hint, "sub": 'clulgraxl',
                "span": _span, "ret": _ret},
               dict(self._state["ctx"]),
               {"sub_error": _is_err, "err_ct": self._state["err_ct"]},
               f"skulbron->{_to}", _post_xid,
               assertion=_asrt, variables_before=_vars_before)
        self._state["cycle"] += 1
        return _asrt

    def _blurtrar(self, fault_hint):
        assert self._state.get("current") == BLURTRAR, \
            f"flimblorx.blurtrar: wrong state {self._state.get('current')}"
        _hint          = fault_hint if fault_hint is not None else _H[BLURTRAR]
        _span          = _uu.uuid4().hex[:8]
        _vars_before   = dict(self._state["ctx"])
        _pre_xid = _xid(__name__, 'blurtrar', "invoke:dreltrell", "pre")
        _emit(self._state["cycle"], 0, __name__, 'blurtrar',
               {"fault_hint": fault_hint, "sub": 'dreltrell',
                "span": _span, "hint": _hint},
               _vars_before, {},
               f"blurtrar->invoke:dreltrell", _pre_xid)
        self._state["cycle"] += 1

        _ret, _next_cycle = dreltrell.invoke(
            hint=_hint, span=_span, caller=BLURTRAR,
            ctx=self._state["ctx"], cycle=self._state["cycle"])
        self._state["cycle"] = _next_cycle

        _is_err = _ret == 2
        if _is_err:
            self._state["err_ct"] += 1
        else:
            self._state["err_ct"] = 0
        self._state["last_ret"] = _ret
        match self._state["current"], _ret:
            case 'blurtrar', 0:
                self._state["current"] = VIMSTOSK
            case 'blurtrar', 1:
                self._state["current"] = BRULSPEX
            case 'blurtrar', 2:
                self._state["current"] = BLURTRAR
        _to = self._state["current"]
        _asrt = "pass"
        if self._state["err_ct"] > _MAX_ERR:
            _asrt = {"failed": "err_budget",
                       "expected": f"err_ct <= {_MAX_ERR}",
                       "actual":   f"err_ct == {self._state['err_ct']}"}
        _post_xid = _xid(__name__, 'blurtrar', _to, f"ret:{_ret}")
        _emit(self._state["cycle"], 0, __name__, 'blurtrar',
               {"fault_hint": fault_hint, "sub": 'dreltrell',
                "span": _span, "ret": _ret},
               dict(self._state["ctx"]),
               {"sub_error": _is_err, "err_ct": self._state["err_ct"]},
               f"blurtrar->{_to}", _post_xid,
               assertion=_asrt, variables_before=_vars_before)
        self._state["cycle"] += 1
        return _asrt

    def _vimstosk(self, fault_hint):
        assert self._state.get("current") == VIMSTOSK, \
            f"flimblorx.vimstosk: wrong state {self._state.get('current')}"
        _hint          = fault_hint if fault_hint is not None else _H[VIMSTOSK]
        _span          = _uu.uuid4().hex[:8]
        _vars_before   = dict(self._state["ctx"])
        _pre_xid = _xid(__name__, 'vimstosk', "invoke:spaxglan", "pre")
        _emit(self._state["cycle"], 0, __name__, 'vimstosk',
               {"fault_hint": fault_hint, "sub": 'spaxglan',
                "span": _span, "hint": _hint},
               _vars_before, {},
               f"vimstosk->invoke:spaxglan", _pre_xid)
        self._state["cycle"] += 1

        _ret, _next_cycle = spaxglan.invoke(
            hint=_hint, span=_span, caller=VIMSTOSK,
            ctx=self._state["ctx"], cycle=self._state["cycle"])
        self._state["cycle"] = _next_cycle

        _is_err = _ret == 2
        if _is_err:
            self._state["err_ct"] += 1
        else:
            self._state["err_ct"] = 0
        self._state["last_ret"] = _ret
        match self._state["current"], _ret:
            case 'vimstosk', 0:
                self._state["current"] = STURGLELL
            case 'vimstosk', 1:
                self._state["current"] = CLIMFLAR
            case 'vimstosk', 2:
                self._state["current"] = VIMSTOSK
        _to = self._state["current"]
        _asrt = "pass"
        if self._state["err_ct"] > _MAX_ERR:
            _asrt = {"failed": "err_budget",
                       "expected": f"err_ct <= {_MAX_ERR}",
                       "actual":   f"err_ct == {self._state['err_ct']}"}
        _post_xid = _xid(__name__, 'vimstosk', _to, f"ret:{_ret}")
        _emit(self._state["cycle"], 0, __name__, 'vimstosk',
               {"fault_hint": fault_hint, "sub": 'spaxglan',
                "span": _span, "ret": _ret},
               dict(self._state["ctx"]),
               {"sub_error": _is_err, "err_ct": self._state["err_ct"]},
               f"vimstosk->{_to}", _post_xid,
               assertion=_asrt, variables_before=_vars_before)
        self._state["cycle"] += 1
        return _asrt

    def _sturglell(self, fault_hint):
        assert self._state.get("current") == STURGLELL, \
            f"flimblorx.sturglell: wrong state {self._state.get('current')}"
        _hint          = fault_hint if fault_hint is not None else _H[STURGLELL]
        _span          = _uu.uuid4().hex[:8]
        _vars_before   = dict(self._state["ctx"])
        _pre_xid = _xid(__name__, 'sturglell', "invoke:flelslull", "pre")
        _emit(self._state["cycle"], 0, __name__, 'sturglell',
               {"fault_hint": fault_hint, "sub": 'flelslull',
                "span": _span, "hint": _hint},
               _vars_before, {},
               f"sturglell->invoke:flelslull", _pre_xid)
        self._state["cycle"] += 1

        _ret, _next_cycle = flelslull.invoke(
            hint=_hint, span=_span, caller=STURGLELL,
            ctx=self._state["ctx"], cycle=self._state["cycle"])
        self._state["cycle"] = _next_cycle

        _is_err = _ret == 2
        if _is_err:
            self._state["err_ct"] += 1
        else:
            self._state["err_ct"] = 0
        self._state["last_ret"] = _ret
        match self._state["current"], _ret:
            case 'sturglell', 0:
                self._state["current"] = BRULSPEX
            case 'sturglell', 1:
                self._state["current"] = BRULSPEX
            case 'sturglell', 2:
                self._state["current"] = STURGLELL
        _to = self._state["current"]
        _asrt = "pass"
        if self._state["err_ct"] > _MAX_ERR:
            _asrt = {"failed": "err_budget",
                       "expected": f"err_ct <= {_MAX_ERR}",
                       "actual":   f"err_ct == {self._state['err_ct']}"}
        _post_xid = _xid(__name__, 'sturglell', _to, f"ret:{_ret}")
        _emit(self._state["cycle"], 0, __name__, 'sturglell',
               {"fault_hint": fault_hint, "sub": 'flelslull',
                "span": _span, "ret": _ret},
               dict(self._state["ctx"]),
               {"sub_error": _is_err, "err_ct": self._state["err_ct"]},
               f"sturglell->{_to}", _post_xid,
               assertion=_asrt, variables_before=_vars_before)
        self._state["cycle"] += 1
        return _asrt

    def _brulspex(self, fault_hint):
        assert self._state.get("current") == BRULSPEX, \
            f"flimblorx.brulspex: wrong state {self._state.get('current')}"
        _hint          = fault_hint if fault_hint is not None else _H[BRULSPEX]
        _span          = _uu.uuid4().hex[:8]
        _vars_before   = dict(self._state["ctx"])
        _pre_xid = _xid(__name__, 'brulspex', "invoke:skalsposx", "pre")
        _emit(self._state["cycle"], 0, __name__, 'brulspex',
               {"fault_hint": fault_hint, "sub": 'skalsposx',
                "span": _span, "hint": _hint},
               _vars_before, {},
               f"brulspex->invoke:skalsposx", _pre_xid)
        self._state["cycle"] += 1

        _ret, _next_cycle = skalsposx.invoke(
            hint=_hint, span=_span, caller=BRULSPEX,
            ctx=self._state["ctx"], cycle=self._state["cycle"])
        self._state["cycle"] = _next_cycle

        _is_err = _ret == 2
        if _is_err:
            self._state["err_ct"] += 1
        else:
            self._state["err_ct"] = 0
        self._state["last_ret"] = _ret
        match self._state["current"], _ret:
            case 'brulspex', 0:
                self._state["current"] = CLIMFLAR
            case 'brulspex', 1:
                self._state["current"] = TRORSLORSLEN
            case 'brulspex', 2:
                self._state["current"] = BRULSPEX
        _to = self._state["current"]
        _asrt = "pass"
        if self._state["err_ct"] > _MAX_ERR:
            _asrt = {"failed": "err_budget",
                       "expected": f"err_ct <= {_MAX_ERR}",
                       "actual":   f"err_ct == {self._state['err_ct']}"}
        _post_xid = _xid(__name__, 'brulspex', _to, f"ret:{_ret}")
        _emit(self._state["cycle"], 0, __name__, 'brulspex',
               {"fault_hint": fault_hint, "sub": 'skalsposx',
                "span": _span, "ret": _ret},
               dict(self._state["ctx"]),
               {"sub_error": _is_err, "err_ct": self._state["err_ct"]},
               f"brulspex->{_to}", _post_xid,
               assertion=_asrt, variables_before=_vars_before)
        self._state["cycle"] += 1
        return _asrt

    def _climflar(self, fault_hint):
        assert self._state.get("current") == CLIMFLAR, \
            f"flimblorx.climflar: wrong state {self._state.get('current')}"
        _hint          = fault_hint if fault_hint is not None else _H[CLIMFLAR]
        _span          = _uu.uuid4().hex[:8]
        _vars_before   = dict(self._state["ctx"])
        _pre_xid = _xid(__name__, 'climflar', "invoke:clelvall", "pre")
        _emit(self._state["cycle"], 0, __name__, 'climflar',
               {"fault_hint": fault_hint, "sub": 'clelvall',
                "span": _span, "hint": _hint},
               _vars_before, {},
               f"climflar->invoke:clelvall", _pre_xid)
        self._state["cycle"] += 1

        _ret, _next_cycle = clelvall.invoke(
            hint=_hint, span=_span, caller=CLIMFLAR,
            ctx=self._state["ctx"], cycle=self._state["cycle"])
        self._state["cycle"] = _next_cycle

        _is_err = _ret == 2
        if _is_err:
            self._state["err_ct"] += 1
        else:
            self._state["err_ct"] = 0
        self._state["last_ret"] = _ret
        match self._state["current"], _ret:
            case 'climflar', 0:
                self._state["current"] = GLARVAXX
            case 'climflar', 1:
                self._state["current"] = GLARVAXX
            case 'climflar', 2:
                self._state["current"] = CLIMFLAR
        _to = self._state["current"]
        _asrt = "pass"
        if self._state["err_ct"] > _MAX_ERR:
            _asrt = {"failed": "err_budget",
                       "expected": f"err_ct <= {_MAX_ERR}",
                       "actual":   f"err_ct == {self._state['err_ct']}"}
        _post_xid = _xid(__name__, 'climflar', _to, f"ret:{_ret}")
        _emit(self._state["cycle"], 0, __name__, 'climflar',
               {"fault_hint": fault_hint, "sub": 'clelvall',
                "span": _span, "ret": _ret},
               dict(self._state["ctx"]),
               {"sub_error": _is_err, "err_ct": self._state["err_ct"]},
               f"climflar->{_to}", _post_xid,
               assertion=_asrt, variables_before=_vars_before)
        self._state["cycle"] += 1
        return _asrt

    def _glarvaxx(self, fault_hint):
        assert self._state.get("current") == GLARVAXX, \
            f"flimblorx.glarvaxx: wrong state {self._state.get('current')}"
        _hint          = fault_hint if fault_hint is not None else _H[GLARVAXX]
        _span          = _uu.uuid4().hex[:8]
        _vars_before   = dict(self._state["ctx"])
        _pre_xid = _xid(__name__, 'glarvaxx', "invoke:drosblosl", "pre")
        _emit(self._state["cycle"], 0, __name__, 'glarvaxx',
               {"fault_hint": fault_hint, "sub": 'drosblosl',
                "span": _span, "hint": _hint},
               _vars_before, {},
               f"glarvaxx->invoke:drosblosl", _pre_xid)
        self._state["cycle"] += 1

        _ret, _next_cycle = drosblosl.invoke(
            hint=_hint, span=_span, caller=GLARVAXX,
            ctx=self._state["ctx"], cycle=self._state["cycle"])
        self._state["cycle"] = _next_cycle

        _is_err = _ret == 2
        if _is_err:
            self._state["err_ct"] += 1
        else:
            self._state["err_ct"] = 0
        self._state["last_ret"] = _ret
        match self._state["current"], _ret:
            case 'glarvaxx', 0:
                self._state["current"] = TRORSLORSLEN
            case 'glarvaxx', 1:
                self._state["current"] = TRANGROSGLIMR
            case 'glarvaxx', 2:
                self._state["current"] = GLARVAXX
        _to = self._state["current"]
        _asrt = "pass"
        if self._state["err_ct"] > _MAX_ERR:
            _asrt = {"failed": "err_budget",
                       "expected": f"err_ct <= {_MAX_ERR}",
                       "actual":   f"err_ct == {self._state['err_ct']}"}
        _post_xid = _xid(__name__, 'glarvaxx', _to, f"ret:{_ret}")
        _emit(self._state["cycle"], 0, __name__, 'glarvaxx',
               {"fault_hint": fault_hint, "sub": 'drosblosl',
                "span": _span, "ret": _ret},
               dict(self._state["ctx"]),
               {"sub_error": _is_err, "err_ct": self._state["err_ct"]},
               f"glarvaxx->{_to}", _post_xid,
               assertion=_asrt, variables_before=_vars_before)
        self._state["cycle"] += 1
        return _asrt

    def _trorslorslen(self, fault_hint):
        assert self._state.get("current") == TRORSLORSLEN, \
            f"flimblorx.trorslorslen: wrong state {self._state.get('current')}"
        _hint          = fault_hint if fault_hint is not None else _H[TRORSLORSLEN]
        _span          = _uu.uuid4().hex[:8]
        _vars_before   = dict(self._state["ctx"])
        _pre_xid = _xid(__name__, 'trorslorslen', "invoke:bralskenl", "pre")
        _emit(self._state["cycle"], 0, __name__, 'trorslorslen',
               {"fault_hint": fault_hint, "sub": 'bralskenl',
                "span": _span, "hint": _hint},
               _vars_before, {},
               f"trorslorslen->invoke:bralskenl", _pre_xid)
        self._state["cycle"] += 1

        _ret, _next_cycle = bralskenl.invoke(
            hint=_hint, span=_span, caller=TRORSLORSLEN,
            ctx=self._state["ctx"], cycle=self._state["cycle"])
        self._state["cycle"] = _next_cycle

        _is_err = _ret == 2
        if _is_err:
            self._state["err_ct"] += 1
        else:
            self._state["err_ct"] = 0
        self._state["last_ret"] = _ret
        match self._state["current"], _ret:
            case 'trorslorslen', 0:
                self._state["current"] = TRANGROSGLIMR
            case 'trorslorslen', 1:
                self._state["current"] = TRANGROSGLIMR
            case 'trorslorslen', 2:
                self._state["current"] = TRORSLORSLEN
        _to = self._state["current"]
        _asrt = "pass"
        if self._state["err_ct"] > _MAX_ERR:
            _asrt = {"failed": "err_budget",
                       "expected": f"err_ct <= {_MAX_ERR}",
                       "actual":   f"err_ct == {self._state['err_ct']}"}
        _post_xid = _xid(__name__, 'trorslorslen', _to, f"ret:{_ret}")
        _emit(self._state["cycle"], 0, __name__, 'trorslorslen',
               {"fault_hint": fault_hint, "sub": 'bralskenl',
                "span": _span, "ret": _ret},
               dict(self._state["ctx"]),
               {"sub_error": _is_err, "err_ct": self._state["err_ct"]},
               f"trorslorslen->{_to}", _post_xid,
               assertion=_asrt, variables_before=_vars_before)
        self._state["cycle"] += 1
        return _asrt

    def _trangrosglimr(self, fault_hint):
        assert self._state.get("current") == TRANGROSGLIMR, \
            f"flimblorx.trangrosglimr: wrong state {self._state.get('current')}"
        _hint          = fault_hint if fault_hint is not None else _H[TRANGROSGLIMR]
        _span          = _uu.uuid4().hex[:8]
        _vars_before   = dict(self._state["ctx"])
        _pre_xid = _xid(__name__, 'trangrosglimr', "invoke:blalston", "pre")
        _emit(self._state["cycle"], 0, __name__, 'trangrosglimr',
               {"fault_hint": fault_hint, "sub": 'blalston',
                "span": _span, "hint": _hint},
               _vars_before, {},
               f"trangrosglimr->invoke:blalston", _pre_xid)
        self._state["cycle"] += 1

        _ret, _next_cycle = blalston.invoke(
            hint=_hint, span=_span, caller=TRANGROSGLIMR,
            ctx=self._state["ctx"], cycle=self._state["cycle"])
        self._state["cycle"] = _next_cycle

        _is_err = _ret == 2
        if _is_err:
            self._state["err_ct"] += 1
        else:
            self._state["err_ct"] = 0
        self._state["last_ret"] = _ret
        match self._state["current"], _ret:
            case 'trangrosglimr', 0:
                self._state["current"] = STAXSKORKRAR
            case 'trangrosglimr', 1:
                self._state["current"] = GRURSKENGLON
            case 'trangrosglimr', 2:
                self._state["current"] = TRANGROSGLIMR
        _to = self._state["current"]
        _asrt = "pass"
        if self._state["err_ct"] > _MAX_ERR:
            _asrt = {"failed": "err_budget",
                       "expected": f"err_ct <= {_MAX_ERR}",
                       "actual":   f"err_ct == {self._state['err_ct']}"}
        _post_xid = _xid(__name__, 'trangrosglimr', _to, f"ret:{_ret}")
        _emit(self._state["cycle"], 0, __name__, 'trangrosglimr',
               {"fault_hint": fault_hint, "sub": 'blalston',
                "span": _span, "ret": _ret},
               dict(self._state["ctx"]),
               {"sub_error": _is_err, "err_ct": self._state["err_ct"]},
               f"trangrosglimr->{_to}", _post_xid,
               assertion=_asrt, variables_before=_vars_before)
        self._state["cycle"] += 1
        return _asrt

    def _staxskorkrar(self, fault_hint):
        assert self._state.get("current") == STAXSKORKRAR, \
            f"flimblorx.staxskorkrar: wrong state {self._state.get('current')}"
        _hint          = fault_hint if fault_hint is not None else _H[STAXSKORKRAR]
        _span          = _uu.uuid4().hex[:8]
        _vars_before   = dict(self._state["ctx"])
        _pre_xid = _xid(__name__, 'staxskorkrar', "invoke:prelspalk", "pre")
        _emit(self._state["cycle"], 0, __name__, 'staxskorkrar',
               {"fault_hint": fault_hint, "sub": 'prelspalk',
                "span": _span, "hint": _hint},
               _vars_before, {},
               f"staxskorkrar->invoke:prelspalk", _pre_xid)
        self._state["cycle"] += 1

        _ret, _next_cycle = prelspalk.invoke(
            hint=_hint, span=_span, caller=STAXSKORKRAR,
            ctx=self._state["ctx"], cycle=self._state["cycle"])
        self._state["cycle"] = _next_cycle

        _is_err = _ret == 2
        if _is_err:
            self._state["err_ct"] += 1
        else:
            self._state["err_ct"] = 0
        self._state["last_ret"] = _ret
        match self._state["current"], _ret:
            case 'staxskorkrar', 0:
                self._state["current"] = CLALSTEXPREN
            case 'staxskorkrar', 1:
                self._state["current"] = CLALSTEXPREN
            case 'staxskorkrar', 2:
                self._state["current"] = STAXSKORKRAR
        _to = self._state["current"]
        _asrt = "pass"
        if self._state["err_ct"] > _MAX_ERR:
            _asrt = {"failed": "err_budget",
                       "expected": f"err_ct <= {_MAX_ERR}",
                       "actual":   f"err_ct == {self._state['err_ct']}"}
        _post_xid = _xid(__name__, 'staxskorkrar', _to, f"ret:{_ret}")
        _emit(self._state["cycle"], 0, __name__, 'staxskorkrar',
               {"fault_hint": fault_hint, "sub": 'prelspalk',
                "span": _span, "ret": _ret},
               dict(self._state["ctx"]),
               {"sub_error": _is_err, "err_ct": self._state["err_ct"]},
               f"staxskorkrar->{_to}", _post_xid,
               assertion=_asrt, variables_before=_vars_before)
        self._state["cycle"] += 1
        return _asrt

    def _clalstexpren(self, fault_hint):
        assert self._state.get("current") == CLALSTEXPREN, \
            f"flimblorx.clalstexpren: wrong state {self._state.get('current')}"
        _hint          = fault_hint if fault_hint is not None else _H[CLALSTEXPREN]
        _span          = _uu.uuid4().hex[:8]
        _vars_before   = dict(self._state["ctx"])
        _pre_xid = _xid(__name__, 'clalstexpren', "invoke:blorbrulk", "pre")
        _emit(self._state["cycle"], 0, __name__, 'clalstexpren',
               {"fault_hint": fault_hint, "sub": 'blorbrulk',
                "span": _span, "hint": _hint},
               _vars_before, {},
               f"clalstexpren->invoke:blorbrulk", _pre_xid)
        self._state["cycle"] += 1

        _ret, _next_cycle = blorbrulk.invoke(
            hint=_hint, span=_span, caller=CLALSTEXPREN,
            ctx=self._state["ctx"], cycle=self._state["cycle"])
        self._state["cycle"] = _next_cycle

        _is_err = _ret == 2
        if _is_err:
            self._state["err_ct"] += 1
        else:
            self._state["err_ct"] = 0
        self._state["last_ret"] = _ret
        match self._state["current"], _ret:
            case 'clalstexpren', 0:
                self._state["current"] = GRURSKENGLON
            case 'clalstexpren', 1:
                self._state["current"] = GRANKROSVANL
            case 'clalstexpren', 2:
                self._state["current"] = CLALSTEXPREN
        _to = self._state["current"]
        _asrt = "pass"
        if self._state["err_ct"] > _MAX_ERR:
            _asrt = {"failed": "err_budget",
                       "expected": f"err_ct <= {_MAX_ERR}",
                       "actual":   f"err_ct == {self._state['err_ct']}"}
        _post_xid = _xid(__name__, 'clalstexpren', _to, f"ret:{_ret}")
        _emit(self._state["cycle"], 0, __name__, 'clalstexpren',
               {"fault_hint": fault_hint, "sub": 'blorbrulk',
                "span": _span, "ret": _ret},
               dict(self._state["ctx"]),
               {"sub_error": _is_err, "err_ct": self._state["err_ct"]},
               f"clalstexpren->{_to}", _post_xid,
               assertion=_asrt, variables_before=_vars_before)
        self._state["cycle"] += 1
        return _asrt

    def _grurskenglon(self, fault_hint):
        assert self._state.get("current") == GRURSKENGLON, \
            f"flimblorx.grurskenglon: wrong state {self._state.get('current')}"
        _hint          = fault_hint if fault_hint is not None else _H[GRURSKENGLON]
        _span          = _uu.uuid4().hex[:8]
        _vars_before   = dict(self._state["ctx"])
        _pre_xid = _xid(__name__, 'grurskenglon', "invoke:clexblalt", "pre")
        _emit(self._state["cycle"], 0, __name__, 'grurskenglon',
               {"fault_hint": fault_hint, "sub": 'clexblalt',
                "span": _span, "hint": _hint},
               _vars_before, {},
               f"grurskenglon->invoke:clexblalt", _pre_xid)
        self._state["cycle"] += 1

        _ret, _next_cycle = clexblalt.invoke(
            hint=_hint, span=_span, caller=GRURSKENGLON,
            ctx=self._state["ctx"], cycle=self._state["cycle"])
        self._state["cycle"] = _next_cycle

        _is_err = _ret == 2
        if _is_err:
            self._state["err_ct"] += 1
        else:
            self._state["err_ct"] = 0
        self._state["last_ret"] = _ret
        match self._state["current"], _ret:
            case 'grurskenglon', 0:
                self._state["current"] = KREXKRAXSPEL
            case 'grurskenglon', 1:
                self._state["current"] = GRANKROSVANL
            case 'grurskenglon', 2:
                self._state["current"] = GRURSKENGLON
        _to = self._state["current"]
        _asrt = "pass"
        if self._state["err_ct"] > _MAX_ERR:
            _asrt = {"failed": "err_budget",
                       "expected": f"err_ct <= {_MAX_ERR}",
                       "actual":   f"err_ct == {self._state['err_ct']}"}
        _post_xid = _xid(__name__, 'grurskenglon', _to, f"ret:{_ret}")
        _emit(self._state["cycle"], 0, __name__, 'grurskenglon',
               {"fault_hint": fault_hint, "sub": 'clexblalt',
                "span": _span, "ret": _ret},
               dict(self._state["ctx"]),
               {"sub_error": _is_err, "err_ct": self._state["err_ct"]},
               f"grurskenglon->{_to}", _post_xid,
               assertion=_asrt, variables_before=_vars_before)
        self._state["cycle"] += 1
        return _asrt

    def _krexkraxspel(self, fault_hint):
        assert self._state.get("current") == KREXKRAXSPEL, \
            f"flimblorx.krexkraxspel: wrong state {self._state.get('current')}"
        _hint          = fault_hint if fault_hint is not None else _H[KREXKRAXSPEL]
        _span          = _uu.uuid4().hex[:8]
        _vars_before   = dict(self._state["ctx"])
        _pre_xid = _xid(__name__, 'krexkraxspel', "invoke:blosvurl", "pre")
        _emit(self._state["cycle"], 0, __name__, 'krexkraxspel',
               {"fault_hint": fault_hint, "sub": 'blosvurl',
                "span": _span, "hint": _hint},
               _vars_before, {},
               f"krexkraxspel->invoke:blosvurl", _pre_xid)
        self._state["cycle"] += 1

        _ret, _next_cycle = blosvurl.invoke(
            hint=_hint, span=_span, caller=KREXKRAXSPEL,
            ctx=self._state["ctx"], cycle=self._state["cycle"])
        self._state["cycle"] = _next_cycle

        _is_err = _ret == 2
        if _is_err:
            self._state["err_ct"] += 1
        else:
            self._state["err_ct"] = 0
        self._state["last_ret"] = _ret
        match self._state["current"], _ret:
            case 'krexkraxspel', 0:
                self._state["current"] = GRANKROSVANL
            case 'krexkraxspel', 1:
                self._state["current"] = GRANKROSVANL
            case 'krexkraxspel', 2:
                self._state["current"] = KREXKRAXSPEL
        _to = self._state["current"]
        _asrt = "pass"
        if self._state["err_ct"] > _MAX_ERR:
            _asrt = {"failed": "err_budget",
                       "expected": f"err_ct <= {_MAX_ERR}",
                       "actual":   f"err_ct == {self._state['err_ct']}"}
        _post_xid = _xid(__name__, 'krexkraxspel', _to, f"ret:{_ret}")
        _emit(self._state["cycle"], 0, __name__, 'krexkraxspel',
               {"fault_hint": fault_hint, "sub": 'blosvurl',
                "span": _span, "ret": _ret},
               dict(self._state["ctx"]),
               {"sub_error": _is_err, "err_ct": self._state["err_ct"]},
               f"krexkraxspel->{_to}", _post_xid,
               assertion=_asrt, variables_before=_vars_before)
        self._state["cycle"] += 1
        return _asrt

    def _grankrosvanl(self, fault_hint):
        assert self._state.get("current") == GRANKROSVANL, \
            f"flimblorx.grankrosvanl: wrong state {self._state.get('current')}"
        _hint          = fault_hint if fault_hint is not None else _H[GRANKROSVANL]
        _span          = _uu.uuid4().hex[:8]
        _vars_before   = dict(self._state["ctx"])
        _pre_xid = _xid(__name__, 'grankrosvanl', "invoke:drixslim", "pre")
        _emit(self._state["cycle"], 0, __name__, 'grankrosvanl',
               {"fault_hint": fault_hint, "sub": 'drixslim',
                "span": _span, "hint": _hint},
               _vars_before, {},
               f"grankrosvanl->invoke:drixslim", _pre_xid)
        self._state["cycle"] += 1

        _ret, _next_cycle = drixslim.invoke(
            hint=_hint, span=_span, caller=GRANKROSVANL,
            ctx=self._state["ctx"], cycle=self._state["cycle"])
        self._state["cycle"] = _next_cycle

        _is_err = _ret == 2
        if _is_err:
            self._state["err_ct"] += 1
        else:
            self._state["err_ct"] = 0
        self._state["last_ret"] = _ret
        match self._state["current"], _ret:
            case 'grankrosvanl', 0:
                self._state["current"] = PRIXSPALSLIXX
            case 'grankrosvanl', 1:
                self._state["current"] = DRIXVENGRARX
            case 'grankrosvanl', 2:
                self._state["current"] = GRANKROSVANL
        _to = self._state["current"]
        _asrt = "pass"
        if self._state["err_ct"] > _MAX_ERR:
            _asrt = {"failed": "err_budget",
                       "expected": f"err_ct <= {_MAX_ERR}",
                       "actual":   f"err_ct == {self._state['err_ct']}"}
        _post_xid = _xid(__name__, 'grankrosvanl', _to, f"ret:{_ret}")
        _emit(self._state["cycle"], 0, __name__, 'grankrosvanl',
               {"fault_hint": fault_hint, "sub": 'drixslim',
                "span": _span, "ret": _ret},
               dict(self._state["ctx"]),
               {"sub_error": _is_err, "err_ct": self._state["err_ct"]},
               f"grankrosvanl->{_to}", _post_xid,
               assertion=_asrt, variables_before=_vars_before)
        self._state["cycle"] += 1
        return _asrt

    def _prixspalslixx(self, fault_hint):
        assert self._state.get("current") == PRIXSPALSLIXX, \
            f"flimblorx.prixspalslixx: wrong state {self._state.get('current')}"
        _hint          = fault_hint if fault_hint is not None else _H[PRIXSPALSLIXX]
        _span          = _uu.uuid4().hex[:8]
        _vars_before   = dict(self._state["ctx"])
        _pre_xid = _xid(__name__, 'prixspalslixx', "invoke:grixprark", "pre")
        _emit(self._state["cycle"], 0, __name__, 'prixspalslixx',
               {"fault_hint": fault_hint, "sub": 'grixprark',
                "span": _span, "hint": _hint},
               _vars_before, {},
               f"prixspalslixx->invoke:grixprark", _pre_xid)
        self._state["cycle"] += 1

        _ret, _next_cycle = grixprark.invoke(
            hint=_hint, span=_span, caller=PRIXSPALSLIXX,
            ctx=self._state["ctx"], cycle=self._state["cycle"])
        self._state["cycle"] = _next_cycle

        _is_err = _ret == 2
        if _is_err:
            self._state["err_ct"] += 1
        else:
            self._state["err_ct"] = 0
        self._state["last_ret"] = _ret
        match self._state["current"], _ret:
            case 'prixspalslixx', 0:
                self._state["current"] = PROSSLOSL
            case 'prixspalslixx', 1:
                self._state["current"] = DRIXVENGRARX
            case 'prixspalslixx', 2:
                self._state["current"] = PRIXSPALSLIXX
        _to = self._state["current"]
        _asrt = "pass"
        if self._state["err_ct"] > _MAX_ERR:
            _asrt = {"failed": "err_budget",
                       "expected": f"err_ct <= {_MAX_ERR}",
                       "actual":   f"err_ct == {self._state['err_ct']}"}
        _post_xid = _xid(__name__, 'prixspalslixx', _to, f"ret:{_ret}")
        _emit(self._state["cycle"], 0, __name__, 'prixspalslixx',
               {"fault_hint": fault_hint, "sub": 'grixprark',
                "span": _span, "ret": _ret},
               dict(self._state["ctx"]),
               {"sub_error": _is_err, "err_ct": self._state["err_ct"]},
               f"prixspalslixx->{_to}", _post_xid,
               assertion=_asrt, variables_before=_vars_before)
        self._state["cycle"] += 1
        return _asrt

    def _prosslosl(self, fault_hint):
        assert self._state.get("current") == PROSSLOSL, \
            f"flimblorx.prosslosl: wrong state {self._state.get('current')}"
        _hint          = fault_hint if fault_hint is not None else _H[PROSSLOSL]
        _span          = _uu.uuid4().hex[:8]
        _vars_before   = dict(self._state["ctx"])
        _pre_xid = _xid(__name__, 'prosslosl', "invoke:brorstorn", "pre")
        _emit(self._state["cycle"], 0, __name__, 'prosslosl',
               {"fault_hint": fault_hint, "sub": 'brorstorn',
                "span": _span, "hint": _hint},
               _vars_before, {},
               f"prosslosl->invoke:brorstorn", _pre_xid)
        self._state["cycle"] += 1

        _ret, _next_cycle = brorstorn.invoke(
            hint=_hint, span=_span, caller=PROSSLOSL,
            ctx=self._state["ctx"], cycle=self._state["cycle"])
        self._state["cycle"] = _next_cycle

        _is_err = _ret == 2
        if _is_err:
            self._state["err_ct"] += 1
        else:
            self._state["err_ct"] = 0
        self._state["last_ret"] = _ret
        match self._state["current"], _ret:
            case 'prosslosl', 0:
                self._state["current"] = DRIXVENGRARX
            case 'prosslosl', 1:
                self._state["current"] = DRIXVENGRARX
            case 'prosslosl', 2:
                self._state["current"] = PROSSLOSL
        _to = self._state["current"]
        _asrt = "pass"
        if self._state["err_ct"] > _MAX_ERR:
            _asrt = {"failed": "err_budget",
                       "expected": f"err_ct <= {_MAX_ERR}",
                       "actual":   f"err_ct == {self._state['err_ct']}"}
        _post_xid = _xid(__name__, 'prosslosl', _to, f"ret:{_ret}")
        _emit(self._state["cycle"], 0, __name__, 'prosslosl',
               {"fault_hint": fault_hint, "sub": 'brorstorn',
                "span": _span, "ret": _ret},
               dict(self._state["ctx"]),
               {"sub_error": _is_err, "err_ct": self._state["err_ct"]},
               f"prosslosl->{_to}", _post_xid,
               assertion=_asrt, variables_before=_vars_before)
        self._state["cycle"] += 1
        return _asrt

    def _drixvengrarx(self, fault_hint):
        assert self._state.get("current") == DRIXVENGRARX, \
            f"flimblorx.drixvengrarx: wrong state {self._state.get('current')}"
        _hint          = fault_hint if fault_hint is not None else _H[DRIXVENGRARX]
        _span          = _uu.uuid4().hex[:8]
        _vars_before   = dict(self._state["ctx"])
        _pre_xid = _xid(__name__, 'drixvengrarx', "invoke:flaxclimn", "pre")
        _emit(self._state["cycle"], 0, __name__, 'drixvengrarx',
               {"fault_hint": fault_hint, "sub": 'flaxclimn',
                "span": _span, "hint": _hint},
               _vars_before, {},
               f"drixvengrarx->invoke:flaxclimn", _pre_xid)
        self._state["cycle"] += 1

        _ret, _next_cycle = flaxclimn.invoke(
            hint=_hint, span=_span, caller=DRIXVENGRARX,
            ctx=self._state["ctx"], cycle=self._state["cycle"])
        self._state["cycle"] = _next_cycle

        _is_err = _ret == 2
        if _is_err:
            self._state["err_ct"] += 1
        else:
            self._state["err_ct"] = 0
        self._state["last_ret"] = _ret
        match self._state["current"], _ret:
            case 'drixvengrarx', 0:
                self._state["current"] = FLONKRALDRAXN
            case 'drixvengrarx', 1:
                self._state["current"] = FLONKRALDRAXN
            case 'drixvengrarx', 2:
                self._state["current"] = DRIXVENGRARX
        _to = self._state["current"]
        _asrt = "pass"
        if self._state["err_ct"] > _MAX_ERR:
            _asrt = {"failed": "err_budget",
                       "expected": f"err_ct <= {_MAX_ERR}",
                       "actual":   f"err_ct == {self._state['err_ct']}"}
        _post_xid = _xid(__name__, 'drixvengrarx', _to, f"ret:{_ret}")
        _emit(self._state["cycle"], 0, __name__, 'drixvengrarx',
               {"fault_hint": fault_hint, "sub": 'flaxclimn',
                "span": _span, "ret": _ret},
               dict(self._state["ctx"]),
               {"sub_error": _is_err, "err_ct": self._state["err_ct"]},
               f"drixvengrarx->{_to}", _post_xid,
               assertion=_asrt, variables_before=_vars_before)
        self._state["cycle"] += 1
        return _asrt

    def _flonkraldraxn(self, fault_hint):
        assert self._state.get("current") == FLONKRALDRAXN, \
            f"flimblorx.flonkraldraxn: wrong state {self._state.get('current')}"
        _hint          = fault_hint if fault_hint is not None else _H[FLONKRALDRAXN]
        _span          = _uu.uuid4().hex[:8]
        _vars_before   = dict(self._state["ctx"])
        _pre_xid = _xid(__name__, 'flonkraldraxn', "invoke:trenblort", "pre")
        _emit(self._state["cycle"], 0, __name__, 'flonkraldraxn',
               {"fault_hint": fault_hint, "sub": 'trenblort',
                "span": _span, "hint": _hint},
               _vars_before, {},
               f"flonkraldraxn->invoke:trenblort", _pre_xid)
        self._state["cycle"] += 1

        _ret, _next_cycle = trenblort.invoke(
            hint=_hint, span=_span, caller=FLONKRALDRAXN,
            ctx=self._state["ctx"], cycle=self._state["cycle"])
        self._state["cycle"] = _next_cycle

        _is_err = _ret == 2
        if _is_err:
            self._state["err_ct"] += 1
        else:
            self._state["err_ct"] = 0
        self._state["last_ret"] = _ret
        match self._state["current"], _ret:
            case 'flonkraldraxn', 0:
                self._state["current"] = TRIMSPONBRORK
            case 'flonkraldraxn', 1:
                self._state["current"] = TRARSLAL
            case 'flonkraldraxn', 2:
                self._state["current"] = FLONKRALDRAXN
        _to = self._state["current"]
        _asrt = "pass"
        if self._state["err_ct"] > _MAX_ERR:
            _asrt = {"failed": "err_budget",
                       "expected": f"err_ct <= {_MAX_ERR}",
                       "actual":   f"err_ct == {self._state['err_ct']}"}
        _post_xid = _xid(__name__, 'flonkraldraxn', _to, f"ret:{_ret}")
        _emit(self._state["cycle"], 0, __name__, 'flonkraldraxn',
               {"fault_hint": fault_hint, "sub": 'trenblort',
                "span": _span, "ret": _ret},
               dict(self._state["ctx"]),
               {"sub_error": _is_err, "err_ct": self._state["err_ct"]},
               f"flonkraldraxn->{_to}", _post_xid,
               assertion=_asrt, variables_before=_vars_before)
        self._state["cycle"] += 1
        return _asrt

    def _trimsponbrork(self, fault_hint):
        assert self._state.get("current") == TRIMSPONBRORK, \
            f"flimblorx.trimsponbrork: wrong state {self._state.get('current')}"
        _hint          = fault_hint if fault_hint is not None else _H[TRIMSPONBRORK]
        _span          = _uu.uuid4().hex[:8]
        _vars_before   = dict(self._state["ctx"])
        _pre_xid = _xid(__name__, 'trimsponbrork', "invoke:glanskelx", "pre")
        _emit(self._state["cycle"], 0, __name__, 'trimsponbrork',
               {"fault_hint": fault_hint, "sub": 'glanskelx',
                "span": _span, "hint": _hint},
               _vars_before, {},
               f"trimsponbrork->invoke:glanskelx", _pre_xid)
        self._state["cycle"] += 1

        _ret, _next_cycle = glanskelx.invoke(
            hint=_hint, span=_span, caller=TRIMSPONBRORK,
            ctx=self._state["ctx"], cycle=self._state["cycle"])
        self._state["cycle"] = _next_cycle

        _is_err = _ret == 2
        if _is_err:
            self._state["err_ct"] += 1
        else:
            self._state["err_ct"] = 0
        self._state["last_ret"] = _ret
        match self._state["current"], _ret:
            case 'trimsponbrork', 0:
                self._state["current"] = TRARSLAL
            case 'trimsponbrork', 1:
                self._state["current"] = SLENSTIX
            case 'trimsponbrork', 2:
                self._state["current"] = TRIMSPONBRORK
        _to = self._state["current"]
        _asrt = "pass"
        if self._state["err_ct"] > _MAX_ERR:
            _asrt = {"failed": "err_budget",
                       "expected": f"err_ct <= {_MAX_ERR}",
                       "actual":   f"err_ct == {self._state['err_ct']}"}
        _post_xid = _xid(__name__, 'trimsponbrork', _to, f"ret:{_ret}")
        _emit(self._state["cycle"], 0, __name__, 'trimsponbrork',
               {"fault_hint": fault_hint, "sub": 'glanskelx',
                "span": _span, "ret": _ret},
               dict(self._state["ctx"]),
               {"sub_error": _is_err, "err_ct": self._state["err_ct"]},
               f"trimsponbrork->{_to}", _post_xid,
               assertion=_asrt, variables_before=_vars_before)
        self._state["cycle"] += 1
        return _asrt

    def _trarslal(self, fault_hint):
        assert self._state.get("current") == TRARSLAL, \
            f"flimblorx.trarslal: wrong state {self._state.get('current')}"
        _hint          = fault_hint if fault_hint is not None else _H[TRARSLAL]
        _span          = _uu.uuid4().hex[:8]
        _vars_before   = dict(self._state["ctx"])
        _pre_xid = _xid(__name__, 'trarslal', "invoke:glaltrimr", "pre")
        _emit(self._state["cycle"], 0, __name__, 'trarslal',
               {"fault_hint": fault_hint, "sub": 'glaltrimr',
                "span": _span, "hint": _hint},
               _vars_before, {},
               f"trarslal->invoke:glaltrimr", _pre_xid)
        self._state["cycle"] += 1

        _ret, _next_cycle = glaltrimr.invoke(
            hint=_hint, span=_span, caller=TRARSLAL,
            ctx=self._state["ctx"], cycle=self._state["cycle"])
        self._state["cycle"] = _next_cycle

        _is_err = _ret == 2
        if _is_err:
            self._state["err_ct"] += 1
        else:
            self._state["err_ct"] = 0
        self._state["last_ret"] = _ret
        match self._state["current"], _ret:
            case 'trarslal', 0:
                self._state["current"] = PRULKRONVORN
            case 'trarslal', 1:
                self._state["current"] = PRULKRONVORN
            case 'trarslal', 2:
                self._state["current"] = TRARSLAL
        _to = self._state["current"]
        _asrt = "pass"
        if self._state["err_ct"] > _MAX_ERR:
            _asrt = {"failed": "err_budget",
                       "expected": f"err_ct <= {_MAX_ERR}",
                       "actual":   f"err_ct == {self._state['err_ct']}"}
        _post_xid = _xid(__name__, 'trarslal', _to, f"ret:{_ret}")
        _emit(self._state["cycle"], 0, __name__, 'trarslal',
               {"fault_hint": fault_hint, "sub": 'glaltrimr',
                "span": _span, "ret": _ret},
               dict(self._state["ctx"]),
               {"sub_error": _is_err, "err_ct": self._state["err_ct"]},
               f"trarslal->{_to}", _post_xid,
               assertion=_asrt, variables_before=_vars_before)
        self._state["cycle"] += 1
        return _asrt

    def _prulkronvorn(self, fault_hint):
        assert self._state.get("current") == PRULKRONVORN, \
            f"flimblorx.prulkronvorn: wrong state {self._state.get('current')}"
        _hint          = fault_hint if fault_hint is not None else _H[PRULKRONVORN]
        _span          = _uu.uuid4().hex[:8]
        _vars_before   = dict(self._state["ctx"])
        _pre_xid = _xid(__name__, 'prulkronvorn', "invoke:sparflax", "pre")
        _emit(self._state["cycle"], 0, __name__, 'prulkronvorn',
               {"fault_hint": fault_hint, "sub": 'sparflax',
                "span": _span, "hint": _hint},
               _vars_before, {},
               f"prulkronvorn->invoke:sparflax", _pre_xid)
        self._state["cycle"] += 1

        _ret, _next_cycle = sparflax.invoke(
            hint=_hint, span=_span, caller=PRULKRONVORN,
            ctx=self._state["ctx"], cycle=self._state["cycle"])
        self._state["cycle"] = _next_cycle

        _is_err = _ret == 2
        if _is_err:
            self._state["err_ct"] += 1
        else:
            self._state["err_ct"] = 0
        self._state["last_ret"] = _ret
        match self._state["current"], _ret:
            case 'prulkronvorn', 0:
                self._state["current"] = SLENSTIX
            case 'prulkronvorn', 1:
                self._state["current"] = SLENSTIX
            case 'prulkronvorn', 2:
                self._state["current"] = PRULKRONVORN
        _to = self._state["current"]
        _asrt = "pass"
        if self._state["err_ct"] > _MAX_ERR:
            _asrt = {"failed": "err_budget",
                       "expected": f"err_ct <= {_MAX_ERR}",
                       "actual":   f"err_ct == {self._state['err_ct']}"}
        _post_xid = _xid(__name__, 'prulkronvorn', _to, f"ret:{_ret}")
        _emit(self._state["cycle"], 0, __name__, 'prulkronvorn',
               {"fault_hint": fault_hint, "sub": 'sparflax',
                "span": _span, "ret": _ret},
               dict(self._state["ctx"]),
               {"sub_error": _is_err, "err_ct": self._state["err_ct"]},
               f"prulkronvorn->{_to}", _post_xid,
               assertion=_asrt, variables_before=_vars_before)
        self._state["cycle"] += 1
        return _asrt

    def _slenstix(self, fault_hint):
        assert self._state.get("current") == SLENSTIX, \
            f"flimblorx.slenstix: wrong state {self._state.get('current')}"
        _hint          = fault_hint if fault_hint is not None else _H[SLENSTIX]
        _span          = _uu.uuid4().hex[:8]
        _vars_before   = dict(self._state["ctx"])
        _pre_xid = _xid(__name__, 'slenstix', "invoke:skanpronn", "pre")
        _emit(self._state["cycle"], 0, __name__, 'slenstix',
               {"fault_hint": fault_hint, "sub": 'skanpronn',
                "span": _span, "hint": _hint},
               _vars_before, {},
               f"slenstix->invoke:skanpronn", _pre_xid)
        self._state["cycle"] += 1

        _ret, _next_cycle = skanpronn.invoke(
            hint=_hint, span=_span, caller=SLENSTIX,
            ctx=self._state["ctx"], cycle=self._state["cycle"])
        self._state["cycle"] = _next_cycle

        _is_err = _ret == 2
        if _is_err:
            self._state["err_ct"] += 1
        else:
            self._state["err_ct"] = 0
        self._state["last_ret"] = _ret
        match self._state["current"], _ret:
            case 'slenstix', 0:
                self._state["current"] = FLIXGLOSN
            case 'slenstix', 1:
                self._state["current"] = CLORBLOSX
            case 'slenstix', 2:
                self._state["current"] = SLENSTIX
        _to = self._state["current"]
        _asrt = "pass"
        if self._state["err_ct"] > _MAX_ERR:
            _asrt = {"failed": "err_budget",
                       "expected": f"err_ct <= {_MAX_ERR}",
                       "actual":   f"err_ct == {self._state['err_ct']}"}
        _post_xid = _xid(__name__, 'slenstix', _to, f"ret:{_ret}")
        _emit(self._state["cycle"], 0, __name__, 'slenstix',
               {"fault_hint": fault_hint, "sub": 'skanpronn',
                "span": _span, "ret": _ret},
               dict(self._state["ctx"]),
               {"sub_error": _is_err, "err_ct": self._state["err_ct"]},
               f"slenstix->{_to}", _post_xid,
               assertion=_asrt, variables_before=_vars_before)
        self._state["cycle"] += 1
        return _asrt

    def _flixglosn(self, fault_hint):
        assert self._state.get("current") == FLIXGLOSN, \
            f"flimblorx.flixglosn: wrong state {self._state.get('current')}"
        _hint          = fault_hint if fault_hint is not None else _H[FLIXGLOSN]
        _span          = _uu.uuid4().hex[:8]
        _vars_before   = dict(self._state["ctx"])
        _pre_xid = _xid(__name__, 'flixglosn', "invoke:glaxglall", "pre")
        _emit(self._state["cycle"], 0, __name__, 'flixglosn',
               {"fault_hint": fault_hint, "sub": 'glaxglall',
                "span": _span, "hint": _hint},
               _vars_before, {},
               f"flixglosn->invoke:glaxglall", _pre_xid)
        self._state["cycle"] += 1

        _ret, _next_cycle = glaxglall.invoke(
            hint=_hint, span=_span, caller=FLIXGLOSN,
            ctx=self._state["ctx"], cycle=self._state["cycle"])
        self._state["cycle"] = _next_cycle

        _is_err = _ret == 2
        if _is_err:
            self._state["err_ct"] += 1
        else:
            self._state["err_ct"] = 0
        self._state["last_ret"] = _ret
        match self._state["current"], _ret:
            case 'flixglosn', 0:
                self._state["current"] = CLORBLOSX
            case 'flixglosn', 1:
                self._state["current"] = VULCLAN
            case 'flixglosn', 2:
                self._state["current"] = FLIXGLOSN
        _to = self._state["current"]
        _asrt = "pass"
        if self._state["err_ct"] > _MAX_ERR:
            _asrt = {"failed": "err_budget",
                       "expected": f"err_ct <= {_MAX_ERR}",
                       "actual":   f"err_ct == {self._state['err_ct']}"}
        _post_xid = _xid(__name__, 'flixglosn', _to, f"ret:{_ret}")
        _emit(self._state["cycle"], 0, __name__, 'flixglosn',
               {"fault_hint": fault_hint, "sub": 'glaxglall',
                "span": _span, "ret": _ret},
               dict(self._state["ctx"]),
               {"sub_error": _is_err, "err_ct": self._state["err_ct"]},
               f"flixglosn->{_to}", _post_xid,
               assertion=_asrt, variables_before=_vars_before)
        self._state["cycle"] += 1
        return _asrt

    def _clorblosx(self, fault_hint):
        assert self._state.get("current") == CLORBLOSX, \
            f"flimblorx.clorblosx: wrong state {self._state.get('current')}"
        _hint          = fault_hint if fault_hint is not None else _H[CLORBLOSX]
        _span          = _uu.uuid4().hex[:8]
        _vars_before   = dict(self._state["ctx"])
        _pre_xid = _xid(__name__, 'clorblosx', "invoke:trorbran", "pre")
        _emit(self._state["cycle"], 0, __name__, 'clorblosx',
               {"fault_hint": fault_hint, "sub": 'trorbran',
                "span": _span, "hint": _hint},
               _vars_before, {},
               f"clorblosx->invoke:trorbran", _pre_xid)
        self._state["cycle"] += 1

        _ret, _next_cycle = trorbran.invoke(
            hint=_hint, span=_span, caller=CLORBLOSX,
            ctx=self._state["ctx"], cycle=self._state["cycle"])
        self._state["cycle"] = _next_cycle

        _is_err = _ret == 2
        if _is_err:
            self._state["err_ct"] += 1
        else:
            self._state["err_ct"] = 0
        self._state["last_ret"] = _ret
        match self._state["current"], _ret:
            case 'clorblosx', 0:
                self._state["current"] = SLOSPRAN
            case 'clorblosx', 1:
                self._state["current"] = TRAXBRORN
            case 'clorblosx', 2:
                self._state["current"] = CLORBLOSX
        _to = self._state["current"]
        _asrt = "pass"
        if self._state["err_ct"] > _MAX_ERR:
            _asrt = {"failed": "err_budget",
                       "expected": f"err_ct <= {_MAX_ERR}",
                       "actual":   f"err_ct == {self._state['err_ct']}"}
        _post_xid = _xid(__name__, 'clorblosx', _to, f"ret:{_ret}")
        _emit(self._state["cycle"], 0, __name__, 'clorblosx',
               {"fault_hint": fault_hint, "sub": 'trorbran',
                "span": _span, "ret": _ret},
               dict(self._state["ctx"]),
               {"sub_error": _is_err, "err_ct": self._state["err_ct"]},
               f"clorblosx->{_to}", _post_xid,
               assertion=_asrt, variables_before=_vars_before)
        self._state["cycle"] += 1
        return _asrt

    def _slospran(self, fault_hint):
        assert self._state.get("current") == SLOSPRAN, \
            f"flimblorx.slospran: wrong state {self._state.get('current')}"
        _hint          = fault_hint if fault_hint is not None else _H[SLOSPRAN]
        _span          = _uu.uuid4().hex[:8]
        _vars_before   = dict(self._state["ctx"])
        _pre_xid = _xid(__name__, 'slospran', "invoke:slonstex", "pre")
        _emit(self._state["cycle"], 0, __name__, 'slospran',
               {"fault_hint": fault_hint, "sub": 'slonstex',
                "span": _span, "hint": _hint},
               _vars_before, {},
               f"slospran->invoke:slonstex", _pre_xid)
        self._state["cycle"] += 1

        _ret, _next_cycle = slonstex.invoke(
            hint=_hint, span=_span, caller=SLOSPRAN,
            ctx=self._state["ctx"], cycle=self._state["cycle"])
        self._state["cycle"] = _next_cycle

        _is_err = _ret == 2
        if _is_err:
            self._state["err_ct"] += 1
        else:
            self._state["err_ct"] = 0
        self._state["last_ret"] = _ret
        match self._state["current"], _ret:
            case 'slospran', 0:
                self._state["current"] = VULCLAN
            case 'slospran', 1:
                self._state["current"] = VULCLAN
            case 'slospran', 2:
                self._state["current"] = SLOSPRAN
        _to = self._state["current"]
        _asrt = "pass"
        if self._state["err_ct"] > _MAX_ERR:
            _asrt = {"failed": "err_budget",
                       "expected": f"err_ct <= {_MAX_ERR}",
                       "actual":   f"err_ct == {self._state['err_ct']}"}
        _post_xid = _xid(__name__, 'slospran', _to, f"ret:{_ret}")
        _emit(self._state["cycle"], 0, __name__, 'slospran',
               {"fault_hint": fault_hint, "sub": 'slonstex',
                "span": _span, "ret": _ret},
               dict(self._state["ctx"]),
               {"sub_error": _is_err, "err_ct": self._state["err_ct"]},
               f"slospran->{_to}", _post_xid,
               assertion=_asrt, variables_before=_vars_before)
        self._state["cycle"] += 1
        return _asrt

    def _vulclan(self, fault_hint):
        assert self._state.get("current") == VULCLAN, \
            f"flimblorx.vulclan: wrong state {self._state.get('current')}"
        _hint          = fault_hint if fault_hint is not None else _H[VULCLAN]
        _span          = _uu.uuid4().hex[:8]
        _vars_before   = dict(self._state["ctx"])
        _pre_xid = _xid(__name__, 'vulclan', "invoke:flelskalk", "pre")
        _emit(self._state["cycle"], 0, __name__, 'vulclan',
               {"fault_hint": fault_hint, "sub": 'flelskalk',
                "span": _span, "hint": _hint},
               _vars_before, {},
               f"vulclan->invoke:flelskalk", _pre_xid)
        self._state["cycle"] += 1

        _ret, _next_cycle = flelskalk.invoke(
            hint=_hint, span=_span, caller=VULCLAN,
            ctx=self._state["ctx"], cycle=self._state["cycle"])
        self._state["cycle"] = _next_cycle

        _is_err = _ret == 2
        if _is_err:
            self._state["err_ct"] += 1
        else:
            self._state["err_ct"] = 0
        self._state["last_ret"] = _ret
        match self._state["current"], _ret:
            case 'vulclan', 0:
                self._state["current"] = TRAXBRORN
            case 'vulclan', 1:
                self._state["current"] = TRAXBRORN
            case 'vulclan', 2:
                self._state["current"] = VULCLAN
        _to = self._state["current"]
        _asrt = "pass"
        if self._state["err_ct"] > _MAX_ERR:
            _asrt = {"failed": "err_budget",
                       "expected": f"err_ct <= {_MAX_ERR}",
                       "actual":   f"err_ct == {self._state['err_ct']}"}
        _post_xid = _xid(__name__, 'vulclan', _to, f"ret:{_ret}")
        _emit(self._state["cycle"], 0, __name__, 'vulclan',
               {"fault_hint": fault_hint, "sub": 'flelskalk',
                "span": _span, "ret": _ret},
               dict(self._state["ctx"]),
               {"sub_error": _is_err, "err_ct": self._state["err_ct"]},
               f"vulclan->{_to}", _post_xid,
               assertion=_asrt, variables_before=_vars_before)
        self._state["cycle"] += 1
        return _asrt

    def run(self, fault_hint=None):
        _new_trace()
        _run_start(__name__, _SEED, fault_hint, _CTX_KEYS)
        self._state = {
            "current":  SLALSLEX,
            "ctx":      {k: 0 for k in _CTX_KEYS},
            "err_ct":   0,
            "last_ret": None,
            "cycle":    0,
        }
        _dispatch = {
            SLALSLEX: self._slalslex,
            SLOSDRAR: self._slosdrar,
            VIXFLOS: self._vixflos,
            STURVEL: self._sturvel,
            TRAXDRENT: self._traxdrent,
            SKENBLELBLONN: self._skenblelblonn,
            SKULBRON: self._skulbron,
            BLURTRAR: self._blurtrar,
            VIMSTOSK: self._vimstosk,
            STURGLELL: self._sturglell,
            BRULSPEX: self._brulspex,
            CLIMFLAR: self._climflar,
            GLARVAXX: self._glarvaxx,
            TRORSLORSLEN: self._trorslorslen,
            TRANGROSGLIMR: self._trangrosglimr,
            STAXSKORKRAR: self._staxskorkrar,
            CLALSTEXPREN: self._clalstexpren,
            GRURSKENGLON: self._grurskenglon,
            KREXKRAXSPEL: self._krexkraxspel,
            GRANKROSVANL: self._grankrosvanl,
            PRIXSPALSLIXX: self._prixspalslixx,
            PROSSLOSL: self._prosslosl,
            DRIXVENGRARX: self._drixvengrarx,
            FLONKRALDRAXN: self._flonkraldraxn,
            TRIMSPONBRORK: self._trimsponbrork,
            TRARSLAL: self._trarslal,
            PRULKRONVORN: self._prulkronvorn,
            SLENSTIX: self._slenstix,
            FLIXGLOSN: self._flixglosn,
            CLORBLOSX: self._clorblosx,
            SLOSPRAN: self._slospran,
            VULCLAN: self._vulclan,
        }
        while self._state["current"] != _TERM \
                and self._state["cycle"] < _MAX_STEPS:
            _asrt = _dispatch[self._state["current"]](fault_hint)
            if isinstance(_asrt, dict) and _asrt.get("failed"):
                return
        _xid_val = _xid(__name__, self._state["current"], "__done__", "terminal")
        _emit(self._state["cycle"], 0, __name__,
               self._state["current"],
               {"fault_hint": fault_hint},
               dict(self._state["ctx"]),
               {"reached_terminal": self._state["current"] == _TERM},
               "terminal", _xid_val)

def run(fault_hint=None):
    FlimblorxFSM().run(fault_hint=fault_hint)
