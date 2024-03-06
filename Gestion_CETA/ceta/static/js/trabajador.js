function cargarDetallesTrabajador() {
    // Lógica para cargar los detalles del trabajador desde la base de datos o datos simulados
    // Puedes obtener el ID del trabajador de la URL o de algún otro lugar
    const idTrabajador = obtenerIdTrabajadorDesdeURL();
  
    // Simulación de datos
    const detallesTrabajador = obtenerDetallesTrabajador(idTrabajador);
  
    // Construir el HTML con los detalles
    const detallesHTML = `
      <h2>${detallesTrabajador.nombre}</h2>
      <p>Dirección: ${detallesTrabajador.direccion}</p>
      <p>Teléfono: ${detallesTrabajador.telefono}</p>
      <p>Email: ${detallesTrabajador.email}</p>
      <p>Departamento: ${detallesTrabajador.departamento}</p>
      <p>Número de Cuenta: ${detallesTrabajador.numeroCuenta}</p>
      <p>Servicios Participantes: ${detallesTrabajador.servicios.join(', ')}</p>
      <p>Horas Participadas: ${detallesTrabajador.horasParticipadas}</p>
      <p>Entregables Presentados: ${detallesTrabajador.entregablesPresentados}</p>
      <p>Pago Mensual: ${detallesTrabajador.pagoMensual}</p>
      <p>Pago Total: ${detallesTrabajador.pagoTotal}</p>
    `;
  
    // Agregar los detalles al contenedor
    document.getElementById('detalles').innerHTML = detallesHTML;
  }
  
  function cerrarVentana() {
    // Lógica para cerrar la ventana emergente
    window.close();
  }
  
  function obtenerIdTrabajadorDesdeURL() {
    // Lógica para obtener el ID del trabajador desde la URL
    // En este ejemplo, se devuelve un valor simulado
    return 1;
  }
  
  function obtenerDetallesTrabajador(idTrabajador) {
    // Lógica para obtener los detalles del trabajador desde la base de datos o datos simulados
    // En este ejemplo, se devuelven valores simulados
    return {
      nombre: 'Trabajador A',
      direccion: 'Dirección A',
      telefono: '123-456-7890',
      email: 'trabajadorA@example.com',
      departamento: 'Departamento A',
      numeroCuenta: '123456789',
      servicios: ['Servicio A', 'Servicio B'],
      horasParticipadas: 20,
      entregablesPresentados: 5,
      pagoMensual: 1000,
      pagoTotal: 5000
    };
  }
  
  // Al cargar la ventana, se cargan automáticamente los detalles del trabajador
  window.onload = cargarDetallesTrabajador;
  