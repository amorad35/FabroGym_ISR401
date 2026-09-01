'use strict';
(() => {
  const KEY = 'fabrogym_validado_2b_v1';
  const seed = window.FABRO_SEED;
  const $ = (s, root=document) => root.querySelector(s);
  const $$ = (s, root=document) => [...root.querySelectorAll(s)];
  const today = () => new Date().toISOString().slice(0,10);
  const nowTime = () => new Date().toTimeString().slice(0,5);
  const addDays = (dateStr, days) => {
    const d = dateStr ? new Date(`${dateStr}T12:00:00`) : new Date();
    d.setDate(d.getDate() + Number(days || 0));
    return d.toISOString().slice(0,10);
  };
  const uid = p => `${p}-${Date.now()}-${Math.random().toString(16).slice(2,6).toUpperCase()}`;
  const money = n => `$${Number(n || 0).toFixed(2)}`;
  const clone = o => JSON.parse(JSON.stringify(o));
  const esc = v => String(v ?? '').replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#039;'}[c]));

  function hydrateSeed(){
    const s = clone(seed);
    const t = today();
    s.clients.forEach((c,i)=>{
      const p = s.plans.find(x=>x.id===c.planId) || s.plans[0];
      c.start = addDays(t, -(i*8+3));
      c.expiry = addDays(c.start, p.days);
      if(i===2) c.expiry = addDays(t,-5);
      if(i===3) c.expiry = addDays(t,6);
      c.createdAt = c.start;
    });
    s.attendance = [
      { id:'ASI-001', clientId:'CLI-002', date:t, time:'07:15', shift:'Mañana', channel:'Recepción' },
      { id:'ASI-002', clientId:'CLI-004', date:t, time:'16:10', shift:'Tarde', channel:'Código QR simulado' }
    ];
    s.notices[0].due = addDays(t,3); s.notices[0].createdAt = t;
    return s;
  }

  function normalizeState(s){
    const base = hydrateSeed();
    if(!s || typeof s!=='object') return base;
    for(const k of ['plans','clients','payments','attendance','products','notices','routines']) {
      if(!Array.isArray(s[k])) s[k] = base[k];
    }
    return s;
  }
  function load(){ try { return normalizeState(JSON.parse(localStorage.getItem(KEY))); } catch { return hydrateSeed(); } }
  function save(){ localStorage.setItem(KEY, JSON.stringify(state)); }
  let state = load();
  let session = null;
  let currentView = 'dashboard';
  let lastReceipt = null;

  const icons = {
    home:'<svg viewBox="0 0 24 24"><path d="M3 11 12 3l9 8v9a1 1 0 0 1-1 1h-5v-6H9v6H4a1 1 0 0 1-1-1z"/></svg>',
    user:'<svg viewBox="0 0 24 24"><circle cx="12" cy="8" r="4"/><path d="M4 21c1-5 4-7 8-7s7 2 8 7"/></svg>',
    card:'<svg viewBox="0 0 24 24"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 10h18"/></svg>',
    money:'<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M15 8.5c-.8-.7-1.8-1-3-1-1.8 0-3 .8-3 2s1 1.8 3 2.2 3 1 3 2.3-1.2 2.2-3 2.2c-1.3 0-2.5-.4-3.4-1.2M12 5v14"/></svg>',
    check:'<svg viewBox="0 0 24 24"><path d="m5 12 4 4L19 6"/></svg>',
    box:'<svg viewBox="0 0 24 24"><path d="m4 7 8-4 8 4-8 4z"/><path d="M4 7v10l8 4 8-4V7M12 11v10"/></svg>',
    alert:'<svg viewBox="0 0 24 24"><path d="M12 3 2 20h20z"/><path d="M12 9v5M12 17h.01"/></svg>',
    routine:'<svg viewBox="0 0 24 24"><path d="M7 6h14M7 12h14M7 18h14"/><circle cx="3" cy="6" r="1"/><circle cx="3" cy="12" r="1"/><circle cx="3" cy="18" r="1"/></svg>',
    shield:'<svg viewBox="0 0 24 24"><path d="M12 3 4 6v6c0 5 3.5 8 8 9 4.5-1 8-4 8-9V6z"/><path d="m8.5 12 2.2 2.2 4.8-5"/></svg>',
    search:'<svg viewBox="0 0 24 24"><circle cx="11" cy="11" r="7"/><path d="m20 20-4-4"/></svg>',
    logout:'<svg viewBox="0 0 24 24"><path d="M10 4H5a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h5M14 8l4 4-4 4M8 12h10"/></svg>'
  };
  const icon = n => `<span class="ico">${icons[n] || icons.home}</span>`;
  const brand = () => `<div class="brand brand-small"><svg class="brand-mark" viewBox="0 0 90 52" aria-hidden="true"><g fill="none" stroke="currentColor" stroke-width="6" stroke-linecap="round"><path d="M24 26h42"/><path d="M17 14v24M9 18v16M73 14v24M81 18v16"/></g></svg><b>Fabro<span>Gym</span></b></div>`;

  function toast(msg,type='success'){
    const root=$('#toast-root');
    root.innerHTML=`<div class="toast ${type}">${esc(msg)}</div>`;
    setTimeout(()=>{ if(root) root.innerHTML=''; },2400);
  }
  function plan(id){ return state.plans.find(x=>x.id===id); }
  function client(id){ return state.clients.find(x=>x.id===id); }
  function isMembershipValid(c){ return c && c.status==='Activo' && c.expiry >= today(); }
  function activePlans(){ return state.plans.filter(p=>p.status==='Activo' && (!p.validUntil || p.validUntil>=today())); }
  function role(){ return session?.role || ''; }
  function can(view){
    const r=role();
    if(r==='Administrador') return true;
    if(r==='Recepción') return !['plans'].includes(view);
    if(r==='Instructor') return ['dashboard','routines','coverage'].includes(view);
    return false;
  }

  function renderLogin(){
    currentView='login';
    $('#app').innerHTML=`
      <section class="auth-page">
        <div class="auth-scene"><div class="floor"></div><div class="rack"></div><div class="bench"></div></div>
        <div class="auth-left">
          ${brand()}
          <div class="auth-copy"><h1>Gestión clara para una operación <span>más ágil</span></h1><p>Prototipo académico interactivo de FabroGym. Todos los datos mostrados son sintéticos y de demostración.</p><div class="short-line"></div></div>
        </div>
        <div class="auth-card-wrap">
          <div class="auth-card">
            <div class="auth-icon">${icon('user')}</div>
            <h2>Iniciar sesión</h2><p class="auth-sub">Entrega 4 (2B) · MVP funcional</p>
            <form id="loginForm">
              <div class="auth-field"><label class="form-label">Usuario <span class="req">*</span></label><div class="field"><span class="leading ico">${icons.user}</span><input id="loginUser" class="input" value="admin" required></div></div>
              <div class="auth-field"><label class="form-label">Contraseña <span class="req">*</span></label><div class="field"><span class="leading ico">${icons.shield}</span><input id="loginPass" class="input" type="password" value="admin123" required></div></div>
              <div class="auth-actions"><button class="btn btn-primary btn-lg" type="submit">Ingresar</button></div>
            </form>
            <div class="requirements"><strong>Credenciales de demostración</strong><div><span>admin / admin123</span><span>recepcion / recep123</span><span>instructor / instr123</span><span>DATO SINTÉTICO — NO REAL</span></div></div>
          </div>
        </div>
        <div class="auth-footer"><span><strong>FabroGym</strong> · ISR-401</span><div class="links"><span>Prototipo académico</span><span>Sin datos reales</span></div></div>
      </section>`;
    $('#loginForm').addEventListener('submit',e=>{
      e.preventDefault();
      const u=$('#loginUser').value.trim(), p=$('#loginPass').value;
      const found=seed.users[u];
      if(!found || found.password!==p){ toast('Credenciales incorrectas','error'); return; }
      session={user:u,role:found.role,name:found.name};
      currentView = found.role==='Instructor' ? 'routines' : 'dashboard';
      renderShell();
    });
  }

  const navItems=[
    ['dashboard','home','Resumen'],['clients','user','Clientes'],['plans','card','Planes'],['payments','money','Pagos'],['attendance','check','Asistencias'],['inventory','box','Inventario'],['notices','alert','Novedades'],['routines','routine','Rutinas'],['coverage','shield','Cobertura RF']
  ];
  function renderShell(){
    if(!session) return renderLogin();
    if(!can(currentView)) currentView = role()==='Instructor'?'routines':'dashboard';
    $('#app').innerHTML=`<div class="app-shell">
      <aside class="sidebar"><div class="sidebar-head">${brand()}</div><div class="nav-scroll"><div class="nav-group-label">OPERACIÓN</div>${navItems.filter(([v])=>can(v)).map(([v,i,l])=>`<button class="nav-item ${currentView===v?'active':''}" data-view="${v}" type="button">${icon(i)}<span>${l}</span></button>`).join('')}</div>
      <div class="sidebar-user"><div class="user-box"><div class="avatar">${esc(session.name.slice(0,2).toUpperCase())}</div><div class="details"><strong>${esc(session.name)}</strong><small>${esc(session.role)}</small></div></div><button id="logoutBtn" class="logout" type="button">${icon('logout')} Cerrar sesión</button></div></aside>
      <main class="main"><header class="topbar"><div><h1 id="topTitle">${esc(titleFor(currentView))}</h1></div><div class="top-user"><div class="avatar sm">FG</div><div class="name">Entrega 4 (2B)<small>DATO SINTÉTICO</small></div></div></header><div id="view" class="content"></div></main>
    </div>`;
    $$('.nav-item').forEach(b=>b.addEventListener('click',()=>{currentView=b.dataset.view; renderShell();}));
    $('#logoutBtn').onclick=()=>{session=null;renderLogin();};
    renderView();
  }
  function titleFor(v){ return ({dashboard:'Resumen operativo',clients:'Clientes y membresías',plans:'Planes y promociones',payments:'Pagos y comprobantes',attendance:'Gestión de asistencias',inventory:'Inventario',notices:'Novedades internas',routines:'Rutinas y seguimiento',coverage:'Cobertura de requisitos Must'})[v] || 'FabroGym'; }
  function renderView(){
    const f={dashboard:renderDashboard,clients:renderClients,plans:renderPlans,payments:renderPayments,attendance:renderAttendance,inventory:renderInventory,notices:renderNotices,routines:renderRoutines,coverage:renderCoverage}[currentView];
    if(f) f();
  }

  function pageHead(title,desc,actions=''){ return `<div class="page-head"><div><h2>${title}</h2><p>${desc}</p></div><div class="head-actions">${actions}</div></div>`; }
  function renderDashboard(){
    const active=state.clients.filter(c=>c.status==='Activo');
    const expiring=state.clients.filter(c=>c.status==='Activo' && c.expiry>=today() && c.expiry<=addDays(today(),7)).length;
    const openNotices=state.notices.filter(n=>['Pendiente','En proceso'].includes(n.status)).length;
    $('#view').innerHTML=pageHead('Resumen operativo','Indicadores sintéticos del MVP final de FabroGym.')+`
      <div class="stat-grid four">
       <div class="stat-card"><div class="stat-icon">${icon('user')}</div><div><div class="stat-label">Clientes activos</div><div class="stat-value">${active.length}</div></div><div class="stat-trend"><strong>RF-CLI-01/02/03</strong></div></div>
       <div class="stat-card"><div class="stat-icon">${icon('card')}</div><div><div class="stat-label">Membresías vigentes</div><div class="stat-value">${active.filter(isMembershipValid).length}</div></div><div class="stat-trend"><strong>${expiring}</strong> próximas a vencer</div></div>
       <div class="stat-card"><div class="stat-icon">${icon('money')}</div><div><div class="stat-label">Pagos registrados</div><div class="stat-value">${state.payments.length}</div></div><div class="stat-trend"><strong>RF-PAG-01</strong></div></div>
       <div class="stat-card ${openNotices?'warn':''}"><div class="stat-icon">${icon('alert')}</div><div><div class="stat-label">Novedades abiertas</div><div class="stat-value">${openNotices}</div></div><div class="stat-trend"><strong>RF-NOV-01</strong></div></div>
      </div>
      <div class="grid grid-half">
        <section class="card card-pad"><div class="section-title-row"><h3>Alertas de membresía</h3><span class="badge warning">RF-MEM-04</span></div><div class="mini-list">${state.clients.slice().sort((a,b)=>a.expiry.localeCompare(b.expiry)).slice(0,6).map(c=>`<div class="mini-row"><div><strong>${esc(c.name)}</strong><small>${esc(plan(c.planId)?.name||'Sin plan')} · vence ${esc(c.expiry)}</small></div><span class="badge ${isMembershipValid(c)?(c.expiry<=addDays(today(),7)?'warning':''):'danger'}">${isMembershipValid(c)?'Vigente':'No vigente'}</span></div>`).join('')}</div></section>
        <section class="card card-pad"><div class="section-title-row"><h3>Cobertura 2B</h3><span class="badge">C3</span></div><div style="text-align:center;padding:28px 10px"><div style="font-size:48px;font-weight:800;color:var(--green)">84,2 %</div><p class="muted">16 de 19 requisitos Must implementados.</p><div class="progress"><span style="width:84.2%"></span></div></div></section>
      </div>`;
  }

  function planOptions(selected=''){ return activePlans().map(p=>`<option value="${p.id}" ${selected===p.id?'selected':''}>${esc(p.name)} · ${p.days} días · ${money(p.price)}</option>`).join(''); }
  function clientOptions(selected=''){ return state.clients.filter(c=>c.status==='Activo').map(c=>`<option value="${c.id}" ${selected===c.id?'selected':''}>${esc(c.name)} · ${esc(c.doc)}</option>`).join(''); }

  function renderClients(){
    $('#view').innerHTML=pageHead('Clientes y membresías','Registro, consulta, actualización, renovación y vigencia.')+`
      <div class="form-layout"><section class="card form-card"><form id="clientForm"><input type="hidden" id="clientEditId"><div class="form-section"><h3>Datos mínimos del cliente</h3><div class="compact-grid">
      <div class="compact-group"><label>Identificación ficticia</label><input id="clientDoc" class="input" required></div><div class="compact-group"><label>Nombre ficticio</label><input id="clientName" class="input" required></div>
      <div class="compact-group"><label>Teléfono ficticio</label><input id="clientPhone" class="input" required></div><div class="compact-group"><label>Estado</label><select id="clientStatus" class="select"><option>Activo</option><option>Inactivo</option></select></div>
      <div class="compact-group"><label>Plan activo</label><select id="clientPlan" class="select" required>${planOptions()}</select></div><div class="compact-group"><label>Vencimiento</label><input id="clientExpiry" class="input" type="date" required value="${addDays(today(),30)}"></div></div></div>
      <div class="form-buttons"><button type="button" id="clearClient" class="btn btn-light">Limpiar</button><button class="btn btn-primary" type="submit">Guardar cliente</button></div></form></section>
      <aside class="card side-summary"><h3>RF cubiertos</h3><div class="summary-kv"><div class="row"><span>Registrar</span><b>RF-CLI-01</b></div><div class="row"><span>Consultar</span><b>RF-CLI-02</b></div><div class="row"><span>Actualizar/reactivar</span><b>RF-CLI-03</b></div><div class="row"><span>Renovar</span><b>RF-MEM-02</b></div><div class="row"><span>Vigencia</span><b>RF-MEM-03</b></div></div></aside></div>
      <section class="card" style="margin-top:20px"><div class="toolbar"><div class="search">${icon('search')}<input id="clientSearch" class="input" placeholder="Buscar por nombre o identificación"></div></div><div class="table-wrap"><table class="table"><thead><tr><th>Cliente</th><th>Plan</th><th>Vencimiento</th><th>Estado</th><th>Acciones</th></tr></thead><tbody id="clientRows"></tbody></table></div></section>`;
    const renderRows=()=>{
      const q=$('#clientSearch').value.toLowerCase();
      const rows=state.clients.filter(c=>`${c.name} ${c.doc}`.toLowerCase().includes(q));
      $('#clientRows').innerHTML=rows.map(c=>`<tr><td><div class="person"><div class="avatar">${esc(c.name.slice(0,2).toUpperCase())}</div><div><strong>${esc(c.name)}</strong><small>${esc(c.doc)} · ${esc(c.phone)}</small></div></div></td><td>${esc(plan(c.planId)?.name||'Sin plan')}</td><td>${esc(c.expiry)}</td><td><span class="badge ${isMembershipValid(c)?'':'danger'}">${isMembershipValid(c)?'Vigente':'No vigente'}</span></td><td><div class="table-actions"><button class="btn btn-sm btn-light" data-edit="${c.id}">Editar</button><button class="btn btn-sm btn-outline" data-renew="${c.id}">Renovar</button></div></td></tr>`).join('');
      $$('[data-edit]').forEach(b=>b.onclick=()=>editClient(b.dataset.edit)); $$('[data-renew]').forEach(b=>b.onclick=()=>renewClient(b.dataset.renew));
    };
    $('#clientSearch').oninput=renderRows; renderRows();
    $('#clientForm').onsubmit=e=>{e.preventDefault(); const id=$('#clientEditId').value; const doc=$('#clientDoc').value.trim(); if(state.clients.some(c=>c.doc===doc&&c.id!==id)){toast('La identificación ya existe','error');return;} const pId=$('#clientPlan').value; const data={doc,name:$('#clientName').value.trim(),phone:$('#clientPhone').value.trim(),status:$('#clientStatus').value,planId:pId,expiry:$('#clientExpiry').value}; if(id){Object.assign(client(id),data);} else {state.clients.push({id:uid('CLI'),start:today(),createdAt:today(),...data});} save(); toast(id?'Cliente actualizado':'Cliente registrado'); clearClientForm(); renderRows();};
    $('#clearClient').onclick=clearClientForm;
    function clearClientForm(){ $('#clientForm').reset(); $('#clientEditId').value=''; $('#clientPlan').innerHTML=planOptions(); $('#clientExpiry').value=addDays(today(),30); }
    function editClient(id){const c=client(id); $('#clientEditId').value=c.id; $('#clientDoc').value=c.doc; $('#clientName').value=c.name; $('#clientPhone').value=c.phone; $('#clientStatus').value=c.status; $('#clientPlan').innerHTML=planOptions(c.planId); $('#clientExpiry').value=c.expiry; window.scrollTo({top:0,behavior:'smooth'});}
    function renewClient(id){ const c=client(id), p=plan(c.planId); if(!p){toast('El cliente no tiene un plan válido','error');return;} const start=c.expiry>=today()?c.expiry:today(); c.start=today(); c.expiry=addDays(start,p.days); c.status='Activo'; save(); renderRows(); toast(`Membresía renovada hasta ${c.expiry}`); }
  }

  function renderPlans(){
    if(role()!=='Administrador'){ currentView='dashboard'; return renderShell(); }
    $('#view').innerHTML=pageHead('Planes y promociones','RF-MEM-01 · Catálogo activo consumido por el registro de clientes.')+`
      <div class="form-layout"><section class="card form-card"><form id="planForm"><input id="planEditId" type="hidden"><div class="form-section"><h3>Configurar plan</h3><div class="compact-grid">
      <div class="compact-group"><label>Nombre</label><input id="planName" class="input" required></div><div class="compact-group"><label>Duración (días)</label><input id="planDays" class="input" type="number" min="1" value="30" required></div>
      <div class="compact-group"><label>Precio</label><input id="planPrice" class="input" type="number" min="0" step="0.01" value="25" required></div><div class="compact-group"><label>Descuento (%)</label><input id="planDiscount" class="input" type="number" min="0" max="100" value="0"></div>
      <div class="compact-group"><label>Vigencia hasta (opcional)</label><input id="planValidUntil" class="input" type="date"></div><div class="compact-group"><label>Estado</label><select id="planStatus" class="select"><option>Activo</option><option>Inactivo</option></select></div></div></div><div class="form-buttons"><button id="clearPlan" class="btn btn-light" type="button">Limpiar</button><button class="btn btn-primary" type="submit">Guardar plan</button></div></form></section>
      <aside class="card side-summary"><h3>Criterio funcional</h3><div class="tip-box"><strong>RF-MEM-01</strong>Nombre, duración, precio, vigencia, estado y promoción opcional. El selector de clientes usa este catálogo.</div></aside></div>
      <section class="card" style="margin-top:20px"><div class="table-wrap"><table class="table"><thead><tr><th>Plan</th><th>Días</th><th>Precio</th><th>Promoción</th><th>Vigencia</th><th>Estado</th><th>Acción</th></tr></thead><tbody id="planRows"></tbody></table></div></section>`;
    const rows=()=>{ $('#planRows').innerHTML=state.plans.map(p=>`<tr><td><strong>${esc(p.name)}</strong></td><td>${p.days}</td><td>${money(p.price)}</td><td>${p.discount?`${p.discount}%`:'—'}</td><td>${esc(p.validUntil||'Sin límite')}</td><td><span class="badge ${p.status==='Activo'?'':'gray'}">${esc(p.status)}</span></td><td><button class="btn btn-sm btn-light" data-plan-edit="${p.id}">Editar</button></td></tr>`).join(''); $$('[data-plan-edit]').forEach(b=>b.onclick=()=>edit(b.dataset.planEdit)); };
    rows(); $('#clearPlan').onclick=()=>{$('#planForm').reset();$('#planEditId').value='';};
    $('#planForm').onsubmit=e=>{e.preventDefault(); const id=$('#planEditId').value; const name=$('#planName').value.trim(); if(state.plans.some(p=>p.name.toLowerCase()===name.toLowerCase()&&p.id!==id)){toast('Ya existe un plan con ese nombre','error');return;} const data={name,days:Number($('#planDays').value),price:Number($('#planPrice').value),discount:Number($('#planDiscount').value||0),validUntil:$('#planValidUntil').value,status:$('#planStatus').value}; if(id) Object.assign(plan(id),data); else state.plans.push({id:uid('PLAN'),...data}); save(); rows(); $('#planForm').reset(); $('#planEditId').value=''; toast(id?'Plan actualizado':'Plan creado');};
    function edit(id){const p=plan(id); $('#planEditId').value=id; $('#planName').value=p.name; $('#planDays').value=p.days; $('#planPrice').value=p.price; $('#planDiscount').value=p.discount||0; $('#planValidUntil').value=p.validUntil||''; $('#planStatus').value=p.status;}
  }

  function renderPayments(){
    $('#view').innerHTML=pageHead('Pagos y comprobantes','RF-PAG-01 · Registro interno demostrativo, sin facturación electrónica ni pasarela bancaria.')+`
      <div class="form-layout"><section class="card form-card"><form id="paymentForm"><div class="form-section"><h3>Registrar pago</h3><div class="compact-grid">
      <div class="compact-group span-12"><label>Cliente</label><select id="paymentClient" class="select" required>${clientOptions()}</select></div><div class="compact-group"><label>Monto</label><input id="paymentAmount" class="input" type="number" min="0.01" step="0.01" required></div><div class="compact-group"><label>Fecha</label><input id="paymentDate" class="input" type="date" value="${today()}" required></div>
      <div class="compact-group"><label>Concepto</label><select id="paymentConcept" class="select"><option>Membresía</option><option>Producto</option><option>Otro</option></select></div><div class="compact-group"><label>Medio</label><select id="paymentMethod" class="select"><option>Efectivo</option><option>Transferencia demostrativa</option><option>Tarjeta registrada manualmente</option></select></div>
      <div class="compact-group span-12"><label>Referencia opcional</label><input id="paymentReference" class="input" placeholder="REF-DEMO-001"></div></div></div><div class="form-buttons"><button class="btn btn-primary" type="submit">Registrar pago</button></div></form><div id="receiptBox"></div></section>
      <aside class="card side-summary"><h3>Restricción</h3><div class="tip-box"><strong>Solo demostración</strong>No procesa cobros reales, no emite facturas electrónicas y no conecta con bancos.</div></aside></div>
      <section class="card" style="margin-top:20px"><div class="table-wrap"><table class="table"><thead><tr><th>ID</th><th>Cliente</th><th>Fecha</th><th>Concepto</th><th>Medio</th><th>Referencia</th><th>Monto</th></tr></thead><tbody id="paymentRows"></tbody></table></div></section>`;
    const rows=()=>$('#paymentRows').innerHTML=state.payments.slice().reverse().map(p=>`<tr><td><strong>${esc(p.id)}</strong></td><td>${esc(client(p.clientId)?.name||'Cliente')}</td><td>${esc(p.date)}</td><td>${esc(p.concept)}</td><td>${esc(p.method)}</td><td>${esc(p.reference||'—')}</td><td>${money(p.amount)}</td></tr>`).join('') || '<tr><td colspan="7" class="empty">Sin pagos registrados.</td></tr>';
    rows();
    $('#paymentForm').onsubmit=e=>{e.preventDefault(); const amount=Number($('#paymentAmount').value); if(!(amount>0)){toast('El monto debe ser mayor que 0','error');return;} const rec={id:uid('PAG'),clientId:$('#paymentClient').value,amount,concept:$('#paymentConcept').value,method:$('#paymentMethod').value,reference:$('#paymentReference').value.trim(),date:$('#paymentDate').value,createdAt:new Date().toISOString()}; state.payments.push(rec); save(); lastReceipt=rec; rows(); showReceipt(rec); e.target.reset(); $('#paymentDate').value=today(); $('#paymentClient').innerHTML=clientOptions(); toast('Pago registrado y comprobante generado');};
    function showReceipt(p){ const c=client(p.clientId); $('#receiptBox').innerHTML=`<div class="security-box" style="margin-top:18px"><h4>Comprobante interno ${esc(p.id)}</h4><div class="summary-list"><div class="summary-item"><b>Cliente</b>${esc(c?.name||'Cliente')}</div><div class="summary-item"><b>Fecha</b>${esc(p.date)}</div><div class="summary-item"><b>Concepto</b>${esc(p.concept)}</div><div class="summary-item"><b>Medio</b>${esc(p.method)}</div><div class="summary-item"><b>Monto</b>${money(p.amount)}</div></div><button id="downloadReceipt" type="button" class="btn btn-outline btn-sm" style="margin-top:12px">Descargar comprobante</button></div>`; $('#downloadReceipt').onclick=()=>downloadReceipt(p); }
  }
  function downloadReceipt(p){ const c=client(p.clientId); const text=`FABROGYM — COMPROBANTE INTERNO DEMOSTRATIVO\nID: ${p.id}\nCliente: ${c?.name||''}\nFecha: ${p.date}\nConcepto: ${p.concept}\nMedio: ${p.method}\nReferencia: ${p.reference||'N/A'}\nMonto: ${money(p.amount)}\n\nNo constituye factura electrónica ni comprobante tributario.`; download(`${p.id}_comprobante.txt`,text,'text/plain'); }

  function renderAttendance(){
    $('#view').innerHTML=pageHead('Gestión de asistencias','RF-ASI-01/02 · Registro no biométrico y consulta.')+`
      <div class="form-layout"><section class="card form-card"><form id="attendanceForm"><div class="form-section"><h3>Registrar ingreso</h3><div class="compact-grid"><div class="compact-group span-12"><label>Cliente</label><select id="attendanceClient" class="select" required>${clientOptions()}</select></div><div class="compact-group"><label>Fecha</label><input id="attendanceDate" class="input" type="date" value="${today()}" required></div><div class="compact-group"><label>Hora</label><input id="attendanceTime" class="input" type="time" value="${nowTime()}" required></div><div class="compact-group"><label>Turno</label><select id="attendanceShift" class="select"><option>Mañana</option><option>Tarde</option><option>Noche</option></select></div><div class="compact-group"><label>Canal</label><select id="attendanceChannel" class="select"><option>Recepción</option><option>Código QR simulado</option></select></div></div></div><div class="form-buttons"><button class="btn btn-primary" type="submit">Confirmar ingreso</button></div></form><div id="attendanceResult"></div></section><aside class="card side-summary"><h3>Control</h3><div class="tip-box"><strong>RF-ASI-01</strong>Rechaza membresía no vigente y evita duplicados del mismo cliente en la fecha.</div></aside></div>
      <section class="card" style="margin-top:20px"><div class="toolbar"><div class="search">${icon('search')}<input id="attendanceSearch" class="input" placeholder="Filtrar cliente"></div><input id="attendanceFilterDate" class="input" type="date" style="max-width:180px"><button id="exportAttendance" class="btn btn-outline btn-sm">Exportar CSV</button></div><div class="table-wrap"><table class="table"><thead><tr><th>Cliente</th><th>Fecha</th><th>Hora</th><th>Turno</th><th>Canal</th></tr></thead><tbody id="attendanceRows"></tbody></table></div></section>`;
    const rows=()=>{ const q=$('#attendanceSearch').value.toLowerCase(), d=$('#attendanceFilterDate').value; const rs=state.attendance.filter(a=>(!q||(client(a.clientId)?.name||'').toLowerCase().includes(q))&&(!d||a.date===d)); $('#attendanceRows').innerHTML=rs.slice().reverse().map(a=>`<tr><td>${esc(client(a.clientId)?.name||'Cliente')}</td><td>${a.date}</td><td>${a.time}</td><td>${a.shift}</td><td>${a.channel}</td></tr>`).join('')||'<tr><td colspan="5" class="empty">Sin registros.</td></tr>'; };
    rows(); $('#attendanceSearch').oninput=rows; $('#attendanceFilterDate').onchange=rows;
    $('#attendanceForm').onsubmit=e=>{e.preventDefault(); const c=client($('#attendanceClient').value), d=$('#attendanceDate').value; if(!isMembershipValid(c)){toast('Ingreso rechazado: membresía no vigente','error'); return;} if(state.attendance.some(a=>a.clientId===c.id&&a.date===d)){toast('Registro duplicado para esta fecha','error');return;} state.attendance.push({id:uid('ASI'),clientId:c.id,date:d,time:$('#attendanceTime').value,shift:$('#attendanceShift').value,channel:$('#attendanceChannel').value}); save(); rows(); toast('Asistencia registrada');};
    $('#exportAttendance').onclick=()=>download('asistencias_fabrogym.csv','cliente,fecha,hora,turno,canal\n'+state.attendance.map(a=>`"${client(a.clientId)?.name||''}",${a.date},${a.time},${a.shift},${a.channel}`).join('\n'),'text/csv');
  }

  function renderInventory(){
    $('#view').innerHTML=pageHead('Inventario','RF-INV-01 · Administración de productos sintéticos.')+`
      <div class="form-layout"><section class="card form-card"><form id="productForm"><input id="productEditId" type="hidden"><div class="form-section"><h3>Producto</h3><div class="compact-grid"><div class="compact-group"><label>Código único</label><input id="productCode" class="input" required></div><div class="compact-group"><label>Nombre</label><input id="productName" class="input" required></div><div class="compact-group"><label>Precio</label><input id="productPrice" class="input" type="number" min="0" step="0.01" required></div><div class="compact-group"><label>Unidad</label><input id="productUnit" class="input" value="unidad" required></div><div class="compact-group"><label>Stock mínimo</label><input id="productMinStock" class="input" type="number" min="0" step="1" required></div><div class="compact-group"><label>Estado</label><select id="productStatus" class="select"><option>Activo</option><option>Inactivo</option></select></div></div></div><div class="form-buttons"><button id="clearProduct" class="btn btn-light" type="button">Limpiar</button><button class="btn btn-primary" type="submit">Guardar producto</button></div></form></section><aside class="card side-summary"><h3>Alcance</h3><div class="tip-box"><strong>RF-INV-01</strong>Esta pantalla no cuenta movimientos de stock ni ventas como RF implementados.</div></aside></div>
      <section class="card" style="margin-top:20px"><div class="toolbar"><div class="search">${icon('search')}<input id="productSearch" class="input" placeholder="Buscar por código o nombre"></div></div><div class="table-wrap"><table class="table"><thead><tr><th>Código</th><th>Producto</th><th>Precio</th><th>Unidad</th><th>Stock mín.</th><th>Estado</th><th>Acción</th></tr></thead><tbody id="productRows"></tbody></table></div></section>`;
    const rows=()=>{const q=$('#productSearch').value.toLowerCase(); const rs=state.products.filter(p=>`${p.code} ${p.name}`.toLowerCase().includes(q)); $('#productRows').innerHTML=rs.map(p=>`<tr><td><strong>${esc(p.code)}</strong></td><td>${esc(p.name)}</td><td>${money(p.price)}</td><td>${esc(p.unit)}</td><td>${p.minStock}</td><td><span class="badge ${p.status==='Activo'?'':'gray'}">${p.status}</span></td><td><button class="btn btn-sm btn-light" data-product-edit="${p.id}">Editar</button></td></tr>`).join(''); $$('[data-product-edit]').forEach(b=>b.onclick=()=>edit(b.dataset.productEdit));};
    rows(); $('#productSearch').oninput=rows; $('#clearProduct').onclick=()=>{$('#productForm').reset();$('#productEditId').value='';};
    $('#productForm').onsubmit=e=>{e.preventDefault(); const id=$('#productEditId').value, code=$('#productCode').value.trim(); if(state.products.some(p=>p.code.toLowerCase()===code.toLowerCase()&&p.id!==id)){toast('Código de producto duplicado','error');return;} const data={code,name:$('#productName').value.trim(),price:Number($('#productPrice').value),unit:$('#productUnit').value.trim(),minStock:Number($('#productMinStock').value),status:$('#productStatus').value}; if(id) Object.assign(state.products.find(p=>p.id===id),data); else state.products.push({id:uid('PROD'),...data}); save(); rows(); $('#productForm').reset(); $('#productEditId').value=''; toast(id?'Producto actualizado':'Producto creado');};
    function edit(id){const p=state.products.find(x=>x.id===id); $('#productEditId').value=p.id; $('#productCode').value=p.code; $('#productName').value=p.name; $('#productPrice').value=p.price; $('#productUnit').value=p.unit; $('#productMinStock').value=p.minStock; $('#productStatus').value=p.status;}
  }

  function renderNotices(){
    $('#view').innerHTML=pageHead('Novedades internas','RF-NOV-01 · Registro y seguimiento de asuntos operativos.')+`
      <div class="form-layout"><section class="card form-card"><form id="noticeForm"><div class="form-section"><h3>Nueva novedad</h3><div class="compact-grid"><div class="compact-group"><label>Categoría</label><select id="noticeCategory" class="select"><option>Operación</option><option>Membresía</option><option>Pago</option><option>Inventario</option><option>Instalaciones</option><option>Otro</option></select></div><div class="compact-group"><label>Responsable</label><select id="noticeOwner" class="select"><option>Administrador</option><option>Recepción</option><option>Instructor</option></select></div><div class="compact-group span-12"><label>Detalle</label><textarea id="noticeDetail" class="textarea" required></textarea></div><div class="compact-group"><label>Vencimiento</label><input id="noticeDue" class="input" type="date" value="${addDays(today(),3)}" required></div><div class="compact-group"><label>Estado</label><select id="noticeStatus" class="select"><option>Pendiente</option><option>En proceso</option><option>Resuelta</option><option>Cancelada</option></select></div></div></div><div class="form-buttons"><button class="btn btn-primary" type="submit">Crear novedad</button></div></form></section><aside class="card side-summary"><h3>Estados</h3><div class="summary-kv"><div class="row"><span>Pendiente</span><b>Abierta</b></div><div class="row"><span>En proceso</span><b>Abierta</b></div><div class="row"><span>Resuelta</span><b>Cerrada</b></div><div class="row"><span>Cancelada</span><b>Cerrada</b></div></div></aside></div><div id="noticeList" class="grid grid-half" style="margin-top:20px"></div>`;
    const cards=()=>{ $('#noticeList').innerHTML=state.notices.slice().reverse().map(n=>`<article class="card card-pad"><div class="section-title-row"><h3>${esc(n.category)} · ${esc(n.id)}</h3><span class="badge ${['Resuelta','Cancelada'].includes(n.status)?'gray':n.status==='En proceso'?'info':'warning'}">${esc(n.status)}</span></div><p>${esc(n.detail)}</p><div class="summary-kv"><div class="row"><span>Responsable</span><b>${esc(n.owner)}</b></div><div class="row"><span>Vencimiento</span><b>${esc(n.due)}</b></div></div><label style="display:block;margin-top:12px;font-size:12px;font-weight:700">Cambiar estado</label><select class="select" data-notice-state="${n.id}" style="min-height:40px;font-size:13px"><option ${n.status==='Pendiente'?'selected':''}>Pendiente</option><option ${n.status==='En proceso'?'selected':''}>En proceso</option><option ${n.status==='Resuelta'?'selected':''}>Resuelta</option><option ${n.status==='Cancelada'?'selected':''}>Cancelada</option></select></article>`).join('') || '<div class="empty">Sin novedades.</div>'; $$('[data-notice-state]').forEach(s=>s.onchange=()=>{state.notices.find(n=>n.id===s.dataset.noticeState).status=s.value;save();cards();toast('Estado de novedad actualizado');}); };
    cards(); $('#noticeForm').onsubmit=e=>{e.preventDefault(); state.notices.push({id:uid('NOV'),category:$('#noticeCategory').value,detail:$('#noticeDetail').value.trim(),owner:$('#noticeOwner').value,due:$('#noticeDue').value,status:$('#noticeStatus').value,createdAt:today()}); save(); e.target.reset(); $('#noticeDue').value=addDays(today(),3); cards(); toast('Novedad creada');};
  }

  function renderRoutines(){
    $('#view').innerHTML=pageHead('Rutinas y seguimiento','RF-RUT-01/02 · Administración de rutinas y registro de cumplimiento.')+`
      <div class="form-layout"><section class="card form-card"><form id="routineForm"><div class="form-section"><h3>Crear y asignar rutina</h3><div class="compact-grid"><div class="compact-group"><label>Cliente</label><select id="routineClient" class="select" required>${clientOptions()}</select></div><div class="compact-group"><label>Instructor</label><select id="routineInstructor" class="select"><option>Instructor Alfa</option><option>Instructor Beta</option></select></div><div class="compact-group span-12"><label>Nombre</label><input id="routineName" class="input" required></div><div class="compact-group"><label>Ejercicio principal</label><input id="routineExercise" class="input" required></div><div class="compact-group"><label>Series × repeticiones</label><input id="routineSets" class="input" value="3 × 12" required></div><div class="compact-group"><label>Descanso</label><input id="routineRest" class="input" value="60 segundos" required></div><div class="compact-group"><label>Estado</label><select id="routineStatus" class="select"><option>Activa</option><option>Inactiva</option></select></div></div></div><div class="form-buttons"><button class="btn btn-primary" type="submit">Guardar rutina</button></div></form></section><aside class="card side-summary"><h3>Cobertura</h3><div class="summary-kv"><div class="row"><span>Administrar</span><b>RF-RUT-01</b></div><div class="row"><span>Seguimiento</span><b>RF-RUT-02</b></div></div></aside></div><div id="routineList" class="grid grid-half" style="margin-top:20px"></div>`;
    const cards=()=>{ $('#routineList').innerHTML=state.routines.map(r=>`<article class="card card-pad"><div class="section-title-row"><h3>${esc(r.name)}</h3><span class="badge ${r.status==='Activa'?'':'gray'}">${r.status}</span></div><p class="muted">${esc(client(r.clientId)?.name||'Cliente')} · ${esc(r.instructor)} · versión ${r.version}</p><div class="summary-kv"><div class="row"><span>Ejercicio</span><b>${esc(r.exercise)}</b></div><div class="row"><span>Series</span><b>${esc(r.sets)}</b></div><div class="row"><span>Descanso</span><b>${esc(r.rest)}</b></div><div class="row"><span>Seguimientos</span><b>${r.followups.length}</b></div></div><div class="compact-grid" style="margin-top:14px"><div class="compact-group"><label>Cumplimiento</label><select class="select" data-follow-status="${r.id}"><option>Completa</option><option>Parcial</option><option>No realizada</option></select></div><div class="compact-group"><label>Observación</label><input class="input" data-follow-note="${r.id}" placeholder="Observación sintética"></div></div><button class="btn btn-outline btn-sm" style="margin-top:10px" data-follow-save="${r.id}">Registrar seguimiento</button>${r.followups.length?`<div class="tip-box"><strong>Último</strong>${esc(r.followups[r.followups.length-1].date)} · ${esc(r.followups[r.followups.length-1].compliance)} · ${esc(r.followups[r.followups.length-1].note||'Sin observación')}</div>`:''}</article>`).join(''); $$('[data-follow-save]').forEach(b=>b.onclick=()=>{const id=b.dataset.followSave,r=state.routines.find(x=>x.id===id);r.followups.push({date:today(),compliance:$(`[data-follow-status="${id}"]`).value,note:$(`[data-follow-note="${id}"]`).value.trim()});save();cards();toast('Seguimiento registrado');}); };
    cards(); $('#routineForm').onsubmit=e=>{e.preventDefault(); state.routines.push({id:uid('RUT'),clientId:$('#routineClient').value,instructor:$('#routineInstructor').value,name:$('#routineName').value.trim(),exercise:$('#routineExercise').value.trim(),sets:$('#routineSets').value.trim(),rest:$('#routineRest').value.trim(),status:$('#routineStatus').value,version:1,followups:[]}); save(); e.target.reset(); cards(); toast('Rutina creada y asignada');};
  }

  function renderCoverage(){
    const coverage=[
      ['RF-AUT-01','Autenticar usuario'],['RF-AUT-02','Aplicar permisos por rol'],['RF-CLI-01','Registrar cliente mínimo'],['RF-CLI-02','Buscar y consultar cliente'],['RF-CLI-03','Actualizar/reactivar cliente'],['RF-MEM-01','Configurar planes y promociones'],['RF-MEM-02','Activar o renovar membresía'],['RF-MEM-03','Consultar vigencia'],['RF-MEM-04','Alertar vencimientos'],['RF-PAG-01','Registrar pago y comprobante'],['RF-ASI-01','Registrar asistencia'],['RF-ASI-02','Consultar asistencia'],['RF-INV-01','Administrar productos'],['RF-NOV-01','Gestionar novedades internas'],['RF-RUT-01','Administrar rutinas'],['RF-RUT-02','Registrar seguimiento']
    ];
    $('#view').innerHTML=pageHead('Cobertura de requisitos Must','Entrega 4 (2B) · Criterio C3 · cobertura mínima requerida: 80 %.')+`<div class="grid grid-half"><section class="card card-pad"><div style="text-align:center;padding:26px"><div style="font-size:62px;font-weight:800;color:var(--green)">84,2 %</div><h3 style="margin:6px 0">16 / 19 RF Must</h3><p class="muted">Cobertura declarada únicamente para funciones implementadas en este MVP.</p><div class="progress" style="height:12px"><span style="width:84.2%"></span></div></div></section><section class="card card-pad"><h3 class="section-title">No contados como implementados</h3><div class="mini-list"><div class="mini-row"><span>RF-INV-02</span><span class="badge gray">No implementado</span></div><div class="mini-row"><span>RF-VEN-01</span><span class="badge gray">No implementado</span></div><div class="mini-row"><span>RF-CAJ-01</span><span class="badge gray">No implementado</span></div></div></section></div><section class="card" style="margin-top:20px"><div class="table-wrap"><table class="table"><thead><tr><th>ID</th><th>Requisito</th><th>Estado</th></tr></thead><tbody>${coverage.map(([id,d])=>`<tr><td><strong>${id}</strong></td><td>${esc(d)}</td><td><span class="badge">Implementado</span></td></tr>`).join('')}</tbody></table></div></section>`;
  }

  function download(name,text,type){ const a=document.createElement('a'); a.href=URL.createObjectURL(new Blob([text],{type})); a.download=name; a.click(); setTimeout(()=>URL.revokeObjectURL(a.href),500); }

  window.FabroGymTest = {
    reset(){ localStorage.removeItem(KEY); state=hydrateSeed(); save(); return true; },
    state(){ return clone(state); },
    coverage(){ return {implemented:16,totalMust:19,percent:84.2}; },
    login(user,password){ const u=seed.users[user]; if(!u||u.password!==password) return false; session={user,role:u.role,name:u.name}; currentView=user==='instructor'?'routines':'dashboard'; renderShell(); return true; },
    createPlan(){ const x={id:uid('PLAN'),name:'Plan Test',days:30,price:20,discount:10,validUntil:'',status:'Activo'}; state.plans.push(x); save(); return x; },
    createPayment(){ const x={id:uid('PAG'),clientId:state.clients[0].id,amount:10,concept:'Membresía',method:'Efectivo',reference:'TEST',date:today()}; state.payments.push(x); save(); return x; },
    createProduct(){ const x={id:uid('PROD'),code:uid('T'),name:'Producto Test',price:1,unit:'unidad',minStock:1,status:'Activo'}; state.products.push(x); save(); return x; },
    createNotice(){ const x={id:uid('NOV'),category:'Operación',detail:'Novedad Test',owner:'Administrador',due:addDays(today(),1),status:'Pendiente',createdAt:today()}; state.notices.push(x); save(); return x; }
  };

  if (typeof document !== 'undefined') renderLogin();
})();
