function cargarDetallesCliente() {
    // Lógica para cargar los detalles del cliente desde la base de datos o datos simulados
    // Puedes obtener el ID del cliente de la URL o de algún otro lugar
    const idCliente = obtenerIdClienteDesdeURL();
  
    // Simulación de datos
    const detallesCliente = obtenerDetallesCliente(idCliente);
  
    // Construir el HTML con los detalles
    const detallesHTML = `
      <h2>${detallesCliente.nombre}</h2>
      <p>Id: ${detallesCliente.id}</p>
      <p>Dirección: ${detallesCliente.direccion}</p>
      <p>Teléfono: ${detallesCliente.telefono}</p>
      <p>Email: ${detallesCliente.email}</p>
      <p>Descripción: ${detallesCliente.descripcion}</p>
      
      <p>Contrato: ${detallesCliente.contrato}</p>
      <!-- Agrega más detalles según sea necesario -->
    `;
  
    // Agregar los detalles al contenedor
    document.getElementById('detalles').innerHTML = detallesHTML;
  }
  
  function cerrarVentana() {
    // Lógica para cerrar la ventana emergente
    window.close();
  }
  
  function obtenerIdClienteDesdeURL() {
    // Lógica para obtener el ID del cliente desde la URL
    // En este ejemplo, se devuelve un valor simulado
    return 1;
  }
  
  function obtenerDetallesCliente(idCliente) {
    // Lógica para obtener los detalles del cliente desde la base de datos o datos simulados
    // En este ejemplo, se devuelven valores simulados
    return {
      nombre: 'Cliente A',
      id: '1',
      direccion: 'Dirección A',
      telefono: '123-456-7890',
      email: 'clienteA@example.com',
      descripcion: 'Descripción del Cliente A',
      contrato: 'Contrato A',
    };
  }
  
  // Al cargar la ventana, se cargan automáticamente los detalles del cliente
  window.onload = cargarDetallesCliente;
  