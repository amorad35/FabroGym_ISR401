'use strict';

const STORAGE_KEYS = {
  attendance: 'fabrogym_mvp_attendance',
  routines: 'fabrogym_mvp_routines',
  availability: 'fabrogym_mvp_instructor_availability'
};

const clients = [
  { id: 'CLI-S01', name: 'Andrea Torres', level: 'Principiante' },
  { id: 'CLI-S02', name: 'Carlos Mendoza', level: 'Intermedio' },
  { id: 'CLI-S03', name: 'Daniela Ruiz', level: 'Principiante' },
  { id: 'CLI-S04', name: 'Javier León', level: 'Avanzado' },
  { id: 'CLI-S05', name: 'María Vera', level: 'Intermedio' }
];

const instructors = [
  { id: 'INS-S01', name: 'Instructor Alfa' },
  { id: 'INS-S02', name: 'Instructor Beta' }
];

const todayISO = () => new Date().toISOString().slice(0, 10);
const currentTime = () => new Date().toTimeString().slice(0, 5);
const uid = (prefix) => `${prefix}-${Date.now()}-${Math.random().toString(16).slice(2, 7)}`;

const seedAttendance = [
  {
    id: 'ASI-DEMO-01',
    clientId: 'CLI-S02',
    date: todayISO(),
    time: '07:18',
    shift: 'Mañana',
    channel: 'Recepción',
    status: 'Habilitado',
    registeredBy: 'Usuario de prueba'
  },
  {
    id: 'ASI-DEMO-02',
    clientId: 'CLI-S03',
    date: todayISO(),
    time: '15:12',
    shift: 'Tarde',
    channel: 'Recepción',
    status: 'Habilitado',
    registeredBy: 'Usuario de prueba'
  }
];

const seedRoutines = [
  {
    id: 'RUT-DEMO-01',
    clientId: 'CLI-S01',
    instructorId: 'INS-S01',
    name: 'Adaptación general',
    start: todayISO(),
    end: '',
    note: 'Rutina de demostración con parámetros operativos.',
    version: 1,
    active: true,
    exercises: [
      { name: 'Bicicleta estática', series: '1', reps: '10 min', rest: '—' },
      { name: 'Prensa guiada', series: '3', reps: '12', rest: '60 s' }
    ],
    followups: []
  }
];

const seedAvailability = [
  {
    id: 'DISP-DEMO-01',
    instructorId: 'INS-S01',
    date: todayISO(),
    from: '07:00',
    to: '12:00',
    status: 'Disponible',
    note: 'Horario de demostración.'
  },
  {
    id: 'DISP-DEMO-02',
    instructorId: 'INS-S02',
    date: todayISO(),
    from: '15:00',
    to: '20:00',
    status: 'Retraso',
    note: 'Llegará 15 minutos tarde.'
  }
];

let attendance = load(STORAGE_KEYS.attendance, seedAttendance);
let routines = load(STORAGE_KEYS.routines, seedRoutines);
let availability = load(STORAGE_KEYS.availability, seedAvailability);

const $ = (selector) => document.querySelector(selector);
const $$ = (selector) => [...document.querySelectorAll(selector)];

function load(key, fallback) {
  try {
    const saved = localStorage.getItem(key);
    return saved ? JSON.parse(saved) : structuredClone(fallback);
  } catch (error) {
    console.warn(`No se pudo leer ${key}`, error);
    return structuredClone(fallback);
  }
}

function save() {
  localStorage.setItem(STORAGE_KEYS.attendance, JSON.stringify(attendance));
  localStorage.setItem(STORAGE_KEYS.routines, JSON.stringify(routines));
  localStorage.setItem(STORAGE_KEYS.availability, JSON.stringify(availability));
}

function clientName(id) {
  return clients.find(c => c.id === id)?.name ?? 'Cliente desconocido';
}

function instructorName(id) {
  return instructors.find(i => i.id === id)?.name ?? 'Instructor desconocido';
}

function showMessage(element, text, type = 'success') {
  element.textContent = text;
  element.className = `message ${type}`;
  window.setTimeout(() => {
    element.className = 'message';
    element.textContent = '';
  }, 4000);
}

function fillSelect(select, items, includeAll = false) {
  select.innerHTML = '';
  if (includeAll) {
    const all = document.createElement('option');
    all.value = '';
    all.textContent = 'Todos';
    select.appendChild(all);
  }
  items.forEach(item => {
    const option = document.createElement('option');
    option.value = item.id;
    option.textContent = item.name;
    select.appendChild(option);
  });
}

function setDefaultDates() {
  $('#attendanceDate').value = todayISO();
  $('#attendanceTime').value = currentTime();
  $('#routineStart').value = todayISO();
  $('#followupDate').value = todayISO();
  if ($('#availabilityDate')) $('#availabilityDate').value = todayISO();
}

function navigate(viewId) {
  $$('.view').forEach(view => view.classList.toggle('active', view.id === viewId));
  $$('.nav-link').forEach(button => button.classList.toggle('active', button.dataset.view === viewId));
  const titles = {
    dashboard: 'Resumen operativo',
    attendance: 'Gestión de asistencias',
    routines: 'Gestión de rutinas',
    instructors: 'Gestión de instructores'
  };
  $('#pageTitle').textContent = titles[viewId] || 'Fabro Gym';
  if (viewId === 'attendance') renderAttendance();
  if (viewId === 'routines') renderRoutines();
  if (viewId === 'instructors') renderInstructors();
  if (viewId === 'dashboard') renderDashboard();
}

function renderDashboard() {
  const todays = attendance.filter(item => item.date === todayISO());
  $('#statAttendance').textContent = todays.length;
  $('#statRoutines').textContent = routines.filter(item => item.active).length;
  $('#statClients').textContent = clients.length;
  $('#statFollowups').textContent = routines.reduce((sum, routine) => sum + routine.followups.length, 0);

  const recentAttendance = [...attendance]
    .sort((a, b) => `${b.date} ${b.time}`.localeCompare(`${a.date} ${a.time}`))
    .slice(0, 4);

  $('#recentAttendance').innerHTML = recentAttendance.length
    ? recentAttendance.map(item => `
      <div class="activity-item">
        <div>
          <strong>${escapeHTML(clientName(item.clientId))}</strong>
          <small>${escapeHTML(item.shift)} · ${escapeHTML(item.channel)}</small>
        </div>
        <time>${escapeHTML(item.date)} ${escapeHTML(item.time)}</time>
      </div>`).join('')
    : '<div class="empty-row">No existen asistencias registradas.</div>';

  const recentRoutines = [...routines].slice(-4).reverse();
  $('#recentRoutines').innerHTML = recentRoutines.length
    ? recentRoutines.map(item => `
      <div class="activity-item">
        <div>
          <strong>${escapeHTML(item.name)}</strong>
          <small>${escapeHTML(clientName(item.clientId))} · v${item.version}</small>
        </div>
        <span class="tag">${item.active ? 'Activa' : 'Inactiva'}</span>
      </div>`).join('')
    : '<div class="empty-row">No existen rutinas registradas.</div>';
}

function renderAttendance() {
  const clientFilter = $('#filterAttendanceClient').value;
  const dateFilter = $('#filterAttendanceDate').value;
  const shiftFilter = $('#filterAttendanceShift').value;

  const filtered = attendance
    .filter(item => !clientFilter || item.clientId === clientFilter)
    .filter(item => !dateFilter || item.date === dateFilter)
    .filter(item => !shiftFilter || item.shift === shiftFilter)
    .sort((a, b) => `${b.date} ${b.time}`.localeCompare(`${a.date} ${a.time}`));

  $('#attendanceTableBody').innerHTML = filtered.length
    ? filtered.map(item => `
      <tr>
        <td><strong>${escapeHTML(clientName(item.clientId))}</strong><br><small>${escapeHTML(item.clientId)}</small></td>
        <td>${escapeHTML(item.date)}</td>
        <td>${escapeHTML(item.time)}</td>
        <td>${escapeHTML(item.shift)}</td>
        <td>${escapeHTML(item.channel)}</td>
        <td>${escapeHTML(item.registeredBy)}</td>
      </tr>`).join('')
    : '<tr><td colspan="6" class="empty-row">No hay registros para los filtros seleccionados.</td></tr>';

  $('#attendanceCount').textContent = filtered.length;
  renderDashboard();
}

function addExerciseRow(values = {}) {
  const fragment = $('#exerciseTemplate').content.cloneNode(true);
  const row = fragment.querySelector('.exercise-row');

  row.querySelector('.exercise-name').value = values.name || '';
  row.querySelector('.exercise-series').value = values.series || '3';
  row.querySelector('.exercise-reps').value = values.reps || '12';
  row.querySelector('.exercise-rest').value = values.rest || '60 s';

  row.querySelector('.remove-exercise').addEventListener('click', () => {
    if ($$('#exerciseRows .exercise-row').length === 1) {
      showMessage($('#routineMessage'), 'La rutina debe contener al menos un ejercicio.', 'error');
      return;
    }
    row.remove();
  });

  $('#exerciseRows').appendChild(fragment);
}

function readExercises() {
  return $$('#exerciseRows .exercise-row').map(row => ({
    name: row.querySelector('.exercise-name').value.trim(),
    series: row.querySelector('.exercise-series').value.trim(),
    reps: row.querySelector('.exercise-reps').value.trim(),
    rest: row.querySelector('.exercise-rest').value.trim()
  }));
}

function renderRoutines() {
  const clientFilter = $('#filterRoutineClient').value;
  const filtered = routines.filter(routine => !clientFilter || routine.clientId === clientFilter);

  $('#routineCards').innerHTML = filtered.length
    ? filtered.map(routine => `
      <article class="routine-card">
        <div class="routine-card-top">
          <div>
            <h3>${escapeHTML(routine.name)}</h3>
            <div class="routine-meta">
              ${escapeHTML(clientName(routine.clientId))} · ${escapeHTML(instructorName(routine.instructorId))}
              · versión ${routine.version}
            </div>
          </div>
          <span class="tag">${routine.active ? 'Activa' : 'Inactiva'}</span>
        </div>
        <ul class="exercise-list">
          ${routine.exercises.map(ex => `<li>${escapeHTML(ex.name)} — ${escapeHTML(ex.series)} series × ${escapeHTML(ex.reps)} · descanso ${escapeHTML(ex.rest)}</li>`).join('')}
        </ul>
        ${routine.note ? `<p class="routine-meta">${escapeHTML(routine.note)}</p>` : ''}
        <div class="routine-actions">
          <button class="btn btn-secondary" data-followup="${routine.id}">Registrar seguimiento</button>
          <button class="btn btn-ghost" data-version="${routine.id}">Crear nueva versión</button>
          <button class="btn btn-ghost" data-toggle="${routine.id}">${routine.active ? 'Desactivar' : 'Activar'}</button>
        </div>
        <div class="followup-list">
          <strong>Seguimientos (${routine.followups.length})</strong>
          ${routine.followups.length
            ? `<ul>${routine.followups.slice().reverse().map(item => `<li>${escapeHTML(item.date)} · ${escapeHTML(item.compliance)}${item.note ? ` — ${escapeHTML(item.note)}` : ''}</li>`).join('')}</ul>`
            : '<span class="routine-meta">Todavía no existen seguimientos.</span>'}
        </div>
      </article>`).join('')
    : '<div class="empty-row">No existen rutinas para el filtro seleccionado.</div>';

  $$('[data-followup]').forEach(button => {
    button.addEventListener('click', () => openFollowup(button.dataset.followup));
  });
  $$('[data-version]').forEach(button => {
    button.addEventListener('click', () => createVersion(button.dataset.version));
  });
  $$('[data-toggle]').forEach(button => {
    button.addEventListener('click', () => toggleRoutine(button.dataset.toggle));
  });

  renderDashboard();
}

function openFollowup(routineId) {
  const routine = routines.find(item => item.id === routineId);
  if (!routine) return;
  $('#followupRoutineId').value = routineId;
  $('#followupTitle').textContent = `Seguimiento: ${routine.name}`;
  $('#followupDate').value = todayISO();
  if ($('#availabilityDate')) $('#availabilityDate').value = todayISO();
  $('#followupCompliance').value = 'Completa';
  $('#followupNote').value = '';
  $('#followupDialog').showModal();
}

function createVersion(routineId) {
  const routine = routines.find(item => item.id === routineId);
  if (!routine) return;

  fillRoutineForm(routine);
  navigate('routines');
  showMessage($('#routineMessage'), `Se cargó la versión ${routine.version}. Al guardar se creará una versión nueva.`);
  $('#routineForm').dataset.sourceRoutine = routineId;
  window.scrollTo({ top: 0, behavior: 'smooth' });
}

function fillRoutineForm(routine) {
  $('#routineClient').value = routine.clientId;
  $('#routineInstructor').value = routine.instructorId;
  $('#routineName').value = routine.name;
  $('#routineStart').value = todayISO();
  $('#routineEnd').value = routine.end || '';
  $('#routineNote').value = routine.note || '';
  $('#exerciseRows').innerHTML = '';
  routine.exercises.forEach(addExerciseRow);
}

function toggleRoutine(routineId) {
  const routine = routines.find(item => item.id === routineId);
  if (!routine) return;
  routine.active = !routine.active;
  save();
  renderRoutines();
}


function activeRoutineFor(clientId, instructorId) {
  return routines
    .filter(item => item.clientId === clientId && item.instructorId === instructorId && item.active)
    .sort((a, b) => b.version - a.version)[0] || null;
}

function renderInstructors() {
  const instructorId = $('#assignedInstructor').value || instructors[0]?.id || '';
  const assigned = clients
    .map(client => ({ client, routine: activeRoutineFor(client.id, instructorId) }))
    .filter(item => item.routine);

  $('#assignedStudentsBody').innerHTML = assigned.length
    ? assigned.map(({ client, routine }) => `
      <tr>
        <td><strong>${escapeHTML(client.name)}</strong><br><small>${escapeHTML(client.id)}</small></td>
        <td>${escapeHTML(client.level)}</td>
        <td>${escapeHTML(routine.name)}</td>
        <td>v${escapeHTML(routine.version)}</td>
      </tr>`).join('')
    : '<tr><td colspan="4" class="empty-row">El instructor seleccionado no tiene alumnos con rutina activa.</td></tr>';
  $('#assignedCount').textContent = assigned.length;

  const history = [...availability].sort((a, b) => `${b.date} ${b.from}`.localeCompare(`${a.date} ${a.from}`));
  $('#availabilityTableBody').innerHTML = history.length
    ? history.map(item => `
      <tr>
        <td>${escapeHTML(instructorName(item.instructorId))}</td>
        <td>${escapeHTML(item.date)}</td>
        <td>${escapeHTML(item.from)} - ${escapeHTML(item.to)}</td>
        <td><span class="tag status-${escapeHTML(item.status.toLowerCase())}">${escapeHTML(item.status)}</span></td>
        <td>${escapeHTML(item.note || 'Sin observación')}</td>
      </tr>`).join('')
    : '<tr><td colspan="5" class="empty-row">No existen novedades registradas.</td></tr>';
}

function resetAvailabilityForm() {
  $('#availabilityForm').reset();
  $('#availabilityDate').value = todayISO();
  $('#availabilityFrom').value = '08:00';
  $('#availabilityTo').value = '12:00';
  $('#availabilityStatus').value = 'Disponible';
}

function resetAttendanceForm() {
  $('#attendanceForm').reset();
  setDefaultDates();
  $('#attendanceShift').value = inferShift($('#attendanceTime').value);
}

function resetRoutineForm() {
  $('#routineForm').reset();
  delete $('#routineForm').dataset.sourceRoutine;
  $('#exerciseRows').innerHTML = '';
  addExerciseRow();
  setDefaultDates();
}

function inferShift(time) {
  const hour = Number((time || '00:00').split(':')[0]);
  if (hour < 12) return 'Mañana';
  if (hour < 18) return 'Tarde';
  return 'Noche';
}

function exportText(filename, content, type = 'text/plain;charset=utf-8') {
  const blob = new Blob([content], { type });
  const url = URL.createObjectURL(blob);
  const link = document.createElement('a');
  link.href = url;
  link.download = filename;
  link.click();
  URL.revokeObjectURL(url);
}

function escapeCSV(value) {
  const text = String(value ?? '');
  return `"${text.replaceAll('"', '""')}"`;
}

function escapeHTML(value) {
  return String(value ?? '')
    .replaceAll('&', '&amp;')
    .replaceAll('<', '&lt;')
    .replaceAll('>', '&gt;')
    .replaceAll('"', '&quot;')
    .replaceAll("'", '&#039;');
}

document.addEventListener('DOMContentLoaded', () => {
  fillSelect($('#attendanceClient'), clients);
  fillSelect($('#filterAttendanceClient'), clients, true);
  fillSelect($('#routineClient'), clients);
  fillSelect($('#filterRoutineClient'), clients, true);
  fillSelect($('#routineInstructor'), instructors);
  fillSelect($('#assignedInstructor'), instructors);
  fillSelect($('#availabilityInstructor'), instructors);
  setDefaultDates();
  resetAttendanceForm();
  resetRoutineForm();
  resetAvailabilityForm();

  $$('.nav-link').forEach(button => button.addEventListener('click', () => navigate(button.dataset.view)));
  $$('[data-jump]').forEach(button => button.addEventListener('click', () => navigate(button.dataset.jump)));

  $('#attendanceTime').addEventListener('change', event => {
    $('#attendanceShift').value = inferShift(event.target.value);
  });

  $('#attendanceForm').addEventListener('submit', event => {
    event.preventDefault();

    if ($('#attendanceStatus').value !== 'Habilitado') {
      showMessage($('#attendanceMessage'), 'El estado operativo no permite confirmar el ingreso.', 'error');
      return;
    }

    const item = {
      id: uid('ASI'),
      clientId: $('#attendanceClient').value,
      date: $('#attendanceDate').value,
      time: $('#attendanceTime').value,
      shift: $('#attendanceShift').value,
      channel: $('#attendanceChannel').value,
      status: $('#attendanceStatus').value,
      registeredBy: 'Usuario de prueba'
    };

    const duplicate = attendance.some(existing =>
      existing.clientId === item.clientId &&
      existing.date === item.date &&
      existing.time === item.time
    );

    if (duplicate) {
      showMessage($('#attendanceMessage'), 'Ya existe una asistencia para ese cliente en la misma fecha y hora.', 'error');
      return;
    }

    attendance.push(item);
    save();
    showMessage($('#attendanceMessage'), `Asistencia registrada para ${clientName(item.clientId)}.`);
    resetAttendanceForm();
    renderAttendance();
  });

  $('#attendanceClear').addEventListener('click', resetAttendanceForm);
  $('#filterAttendanceClient').addEventListener('change', renderAttendance);
  $('#filterAttendanceDate').addEventListener('change', renderAttendance);
  $('#filterAttendanceShift').addEventListener('change', renderAttendance);

  $('#exportAttendance').addEventListener('click', () => {
    const header = ['id','cliente','fecha','hora','turno','canal','registrado_por'];
    const rows = attendance.map(item => [
      item.id, clientName(item.clientId), item.date, item.time, item.shift, item.channel, item.registeredBy
    ]);
    const csv = [header, ...rows].map(row => row.map(escapeCSV).join(',')).join('\n');
    exportText('fabrogym_asistencias_demo.csv', '\ufeff' + csv, 'text/csv;charset=utf-8');
  });

  $('#addExercise').addEventListener('click', () => addExerciseRow());
  $('#routineClear').addEventListener('click', resetRoutineForm);
  $('#filterRoutineClient').addEventListener('change', renderRoutines);

  $('#routineForm').addEventListener('submit', event => {
    event.preventDefault();
    const exercises = readExercises();

    if (!exercises.length || exercises.some(item => !item.name)) {
      showMessage($('#routineMessage'), 'Complete al menos un ejercicio válido.', 'error');
      return;
    }

    const sourceId = $('#routineForm').dataset.sourceRoutine;
    let version = 1;

    if (sourceId) {
      const source = routines.find(item => item.id === sourceId);
      if (source) {
        source.active = false;
        version = source.version + 1;
      }
    }

    const routine = {
      id: uid('RUT'),
      clientId: $('#routineClient').value,
      instructorId: $('#routineInstructor').value,
      name: $('#routineName').value.trim(),
      start: $('#routineStart').value,
      end: $('#routineEnd').value,
      note: $('#routineNote').value.trim(),
      version,
      active: true,
      exercises,
      followups: []
    };

    routines.push(routine);
    save();
    showMessage($('#routineMessage'), `Rutina guardada como versión ${version}.`);
    resetRoutineForm();
    renderRoutines();
  });

  $('#exportRoutines').addEventListener('click', () => {
    exportText(
      'fabrogym_rutinas_demo.json',
      JSON.stringify({ clients, instructors, routines }, null, 2),
      'application/json;charset=utf-8'
    );
  });

  $('#followupForm').addEventListener('submit', event => {
    event.preventDefault();
    const routine = routines.find(item => item.id === $('#followupRoutineId').value);
    if (!routine) return;

    routine.followups.push({
      id: uid('SEG'),
      date: $('#followupDate').value,
      compliance: $('#followupCompliance').value,
      note: $('#followupNote').value.trim()
    });

    save();
    $('#followupDialog').close();
    renderRoutines();
  });

  $('#closeDialog').addEventListener('click', () => $('#followupDialog').close());
  $('#cancelDialog').addEventListener('click', () => $('#followupDialog').close());


  $('#assignedInstructor').addEventListener('change', renderInstructors);

  $('#availabilityForm').addEventListener('submit', event => {
    event.preventDefault();
    const from = $('#availabilityFrom').value;
    const to = $('#availabilityTo').value;
    if (from >= to) {
      showMessage($('#availabilityMessage'), 'La hora final debe ser posterior a la hora inicial.', 'error');
      return;
    }
    availability.push({
      id: uid('DISP'),
      instructorId: $('#availabilityInstructor').value,
      date: $('#availabilityDate').value,
      from,
      to,
      status: $('#availabilityStatus').value,
      note: $('#availabilityNote').value.trim()
    });
    save();
    showMessage($('#availabilityMessage'), 'Novedad del instructor registrada correctamente.');
    resetAvailabilityForm();
    renderInstructors();
  });

  $('#availabilityClear').addEventListener('click', resetAvailabilityForm);

  $('#exportAvailability').addEventListener('click', () => {
    const header = ['id','instructor','fecha','hora_desde','hora_hasta','estado','observacion'];
    const rows = availability.map(item => [
      item.id, instructorName(item.instructorId), item.date, item.from, item.to, item.status, item.note
    ]);
    const csv = [header, ...rows].map(row => row.map(escapeCSV).join(',')).join('\n');
    exportText('fabrogym_disponibilidad_instructores_demo.csv', '\ufeff' + csv, 'text/csv;charset=utf-8');
  });

  $('#resetDemo').addEventListener('click', () => {
    const accepted = window.confirm('¿Desea eliminar los registros locales y restablecer los datos de demostración?');
    if (!accepted) return;
    attendance = structuredClone(seedAttendance);
    routines = structuredClone(seedRoutines);
    availability = structuredClone(seedAvailability);
    save();
    resetAttendanceForm();
    resetRoutineForm();
    resetAvailabilityForm();
    renderAttendance();
    renderRoutines();
    renderInstructors();
    navigate('dashboard');
  });

  renderAttendance();
  renderRoutines();
  renderInstructors();
  renderDashboard();
});
