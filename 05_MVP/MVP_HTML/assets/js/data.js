'use strict';
window.FABRO_SEED = {
  users: {
    admin: { password: 'admin123', role: 'Administrador', name: 'Administrador Demo' },
    recepcion: { password: 'recep123', role: 'Recepción', name: 'Recepción Demo' },
    instructor: { password: 'instr123', role: 'Instructor', name: 'Instructor Demo' }
  },
  plans: [
    { id:'PLAN-001', name:'Mensual', days:30, price:25, discount:0, validUntil:'', status:'Activo' },
    { id:'PLAN-002', name:'Trimestral', days:90, price:65, discount:5, validUntil:'', status:'Activo' },
    { id:'PLAN-003', name:'Pase diario', days:1, price:3, discount:0, validUntil:'', status:'Activo' }
  ],
  clients: [
    { id:'CLI-001', doc:'0999999901', name:'Andrea Torres', phone:'0990000001', status:'Activo', planId:'PLAN-001', start:'', expiry:'', createdAt:'' },
    { id:'CLI-002', doc:'0999999902', name:'Carlos Mendoza', phone:'0990000002', status:'Activo', planId:'PLAN-002', start:'', expiry:'', createdAt:'' },
    { id:'CLI-003', doc:'0999999903', name:'Daniela Ruiz', phone:'0990000003', status:'Inactivo', planId:'PLAN-001', start:'', expiry:'', createdAt:'' },
    { id:'CLI-004', doc:'0999999904', name:'Javier León', phone:'0990000004', status:'Activo', planId:'PLAN-001', start:'', expiry:'', createdAt:'' }
  ],
  payments: [],
  attendance: [],
  products: [
    { id:'PROD-001', code:'AGUA-500', name:'Agua 500 ml', price:1, unit:'unidad', minStock:10, status:'Activo' },
    { id:'PROD-002', code:'BARRA-01', name:'Barra energética demo', price:2.5, unit:'unidad', minStock:5, status:'Activo' }
  ],
  notices: [
    { id:'NOV-001', category:'Operación', detail:'Revisar cierre de puerta secundaria.', owner:'Administrador', due:'', status:'Pendiente', createdAt:'' }
  ],
  routines: [
    { id:'RUT-001', clientId:'CLI-001', instructor:'Instructor Alfa', name:'Adaptación general', exercise:'Prensa guiada', sets:'3 × 12', rest:'60 segundos', status:'Activa', version:1, followups:[] }
  ]
};
