// script.js

// Objeto que contiene los datos simulados
const datos = {
    clientes: [
      { id: 1, nombre: 'Ever', direccion: 'Dirección A', telefono: '123-456-7890', email: 'clienteA@example.com', descripcion: 'Descripción Cliente A' },
      { id: 2, nombre: 'Cliente B', direccion: 'Dirección B', telefono: '987-654-3210', email: 'clienteB@example.com', descripcion: 'Descripción Cliente B' },
      // Agrega más clientes según sea necesario
    ],
    monedas: [
      { id: 1, nombre: 'CUP', descripcion: 'Peso Cubano' },
      { id: 2, nombre: 'MLC', descripcion: 'Moneda Libremente Convertible' },
      // Agrega más tipos de moneda según sea necesario
    ],
    contratos: [
      { idContrato: 1, titulo: 'Contrato A', tipo: 'Tipo A', manager: 'Manager A' },
      { idContrato: 2, titulo: 'Contrato B', tipo: 'Tipo B', manager: 'Manager B' },
      // Agrega más contratos según sea necesario
    ],
    trabajadores: [
      { id: 1, nombre: 'Ever', rol: 'Administrador de Sistema', direccion: 'Dirección A', telefono: '123-456-7890', email: 'everazcuy29@gmail.com', departamento: 'Departamento A', cuenta: '123456789', seguridad: 'ever2909' },
      { id: 2, nombre: 'Trabajador B', rol: 'Administrador', direccion: 'Dirección B', telefono: '987-654-3210', email: 'trabajadorB@example.com', departamento: 'Departamento B', cuenta: '987654321' },
      // Agrega más trabajadores según sea necesario
    ],
    servicios: [
      { idService: 1, idContrato: 'Contrato A', productos: 'Producto A, Producto B', duracion: 8, idTrabajadores: '1, 2' },
      { idService: 2, idContrato: 'Contrato B', productos: 'Producto C, Producto D', duracion: 12, idTrabajadores: '3, 4' },
      // Agrega más servicios según sea necesario
    ],
  };
  
  // Función para obtener detalles de un cliente por ID
  function obtenerDetallesCliente(idCliente) {
    return datos.clientes.find(cliente => cliente.id === idCliente);
  }
  
  // Función para obtener detalles de una moneda por ID
  function obtenerDetallesMoneda(idMoneda) {
    return datos.monedas.find(moneda => moneda.id === idMoneda);
  }
  
  // Función para obtener detalles de un contrato por ID
  function obtenerDetallesContrato(idContrato) {
    return datos.contratos.find(contrato => contrato.idContrato === idContrato);
  }
  
  // Función para obtener detalles de un trabajador por ID
  function obtenerDetallesTrabajador(idTrabajador) {
    return datos.trabajadores.find(trabajador => trabajador.id === idTrabajador);
  }
  
  // Función para obtener detalles de un servicio por ID
  function obtenerDetallesServicio(idServicio) {
    return datos.servicios.find(servicio => servicio.idService === idServicio);
  }
  document.addEventListener('DOMContentLoaded', function () {
    llenarTablaClientes();
  });
  
  function llenarTablaClientes() {
    const clientesTableBody = document.getElementById('clientes-table-body');
    clientesTableBody.innerHTML = '';
  
    datos.clientes.forEach(cliente => {
      const fila = `
        <tr>
          <td>${cliente.id}</td>
          <td>${cliente.nombre}</td>
          <td>${cliente.direccion}</td>
          <td>${cliente.telefono}</td>
          <td>${cliente.email}</td>
          <td>${cliente.descripcion}</td>
          
          <td>
            <button onclick="eliminarCliente(${cliente.id})">Eliminar</button>
            <button onclick="verCliente(${cliente.id})">Ver</button>
          </td>
        </tr>
      `;
  
      clientesTableBody.innerHTML += fila;
    });
  }
  
  function abrirFormularioCliente() {
    // Abre el formulario para agregar cliente en una nueva ventana o pestaña
    window.open('nuevoCliente.html', '_blank');
  }
  
  function agregarClienteDesdeFormulario(cliente) {
    // Agrega el nuevo cliente a la lista de datos
    datos.clientes.push(cliente);
    // Vuelve a llenar la tabla de clientes para reflejar los cambios
    llenarTablaClientes();
  }
  document.addEventListener('DOMContentLoaded', function () {
    // Puedes agregar aquí lógica adicional si es necesario
  });
  
  function agregarCliente() {
    // Obtén los valores del formulario
    const nombre = document.getElementById('nombre').value;
    // Obten los demás valores según sea necesario
  
    // Crea un nuevo objeto cliente con los valores del formulario
    const nuevoCliente = {
      id: datos.clientes.length + 1, // Asigna un nuevo ID único
      nombre: nombre,
      // Asigna los demás campos del cliente según sea necesario
    };
  
    // Cierra la ventana o pestaña del formulario
    window.close();
  
    // Llama a la función en el script principal para agregar el cliente
    window.opener.agregarClienteDesdeFormulario(nuevoCliente);
  }
  
  // Resto de las funciones (eliminarCliente, verCliente, etc.) permanecen igual
  document.addEventListener('DOMContentLoaded', function () {
    llenarTablaMonedas();
    llenarTablaContratos();
    llenarTablaTrabajadores();
    llenarTablaServicios();
  });
  
  function llenarTablaMonedas() {
    const monedasTableBody = document.getElementById('monedas-table-body');
    monedasTableBody.innerHTML = '';
  
    datos.monedas.forEach(moneda => {
      const fila = `
        <tr>
          <td>${moneda.id}</td>
          <td>${moneda.nombre}</td>
          <td>${moneda.descripcion}</td>
          <td>
            <button onclick="eliminarMoneda(${moneda.id})">Eliminar</button>
            <button onclick="verMoneda(${moneda.id})">Ver</button>
          </td>
        </tr>
      `;
  
      monedasTableBody.innerHTML += fila;
    });
  }
  
  function llenarTablaContratos() {
    const contratosTableBody = document.getElementById('contratos-table-body');
    contratosTableBody.innerHTML = '';
  
    datos.contratos.forEach(contrato => {
      const fila = `
        <tr>
          <td>${contrato.idContrato}</td>
          <td>${contrato.titulo}</td>
          <td>${contrato.tipo}</td>
          <td>${contrato.manager}</td>
          <td>
            <button onclick="eliminarContrato(${contrato.idContrato})">Eliminar</button>
            <button onclick="verContrato(${contrato.idContrato})">Ver</button>
          </td>
        </tr>
      `;
  
      contratosTableBody.innerHTML += fila;
    });
  }
  
  function llenarTablaTrabajadores() {
    const trabajadoresTableBody = document.getElementById('trabajadores-table-body');
    trabajadoresTableBody.innerHTML = '';
  
    datos.trabajadores.forEach(trabajador => {
      const fila = `
        <tr>
          <td>${trabajador.id}</td>
          <td>${trabajador.nombre}</td>
          <td>${trabajador.rol}</td>
          <td>${trabajador.direccion}</td>
          <td>${trabajador.telefono}</td>
          <td>${trabajador.email}</td>
          <td>${trabajador.departamento}</td>
          <td>${trabajador.cuenta}</td>
          <td>
            <button onclick="eliminarTrabajador(${trabajador.id})">Eliminar</button>
            <button class="ver" onclick="verDetallesTrabajador(${trabajador.id})">Ver</button>
          </td>
        </tr>
      `;
  
      trabajadoresTableBody.innerHTML += fila;
    });
  }
  
  function llenarTablaServicios() {
    const serviciosTableBody = document.getElementById('servicios-table-body');
    serviciosTableBody.innerHTML = '';
  
    datos.servicios.forEach(servicio => {
      const fila = `
        <tr>
          <td>${servicio.idService}</td>
          <td>${servicio.idContrato}</td>
          <td>${servicio.productos}</td>
          <td>${servicio.duracion}</td>
          <td>${servicio.idTrabajadores}</td>
          <td>
            <button onclick="eliminarServicio(${servicio.idService})">Eliminar</button>
            <button class="ver" onclick="verServicio(${servicio.idService})">Ver</button>
          </td>
        </tr>
      `;
  
      serviciosTableBody.innerHTML += fila;
    });
  }
  
  // Funciones de agregar (agregarMoneda, agregarContrato, agregarTrabajador, agregarServicio) y resto de las funciones (eliminar, ver, etc.) permanecen igual
  