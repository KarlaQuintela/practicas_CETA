function cargarDetallesContrato() {
    // Lógica para cargar los detalles del contrato desde la base de datos o datos simulados
    // Puedes obtener el ID del contrato de la URL o de algún otro lugar
    const idContrato = obtenerIdContratoDesdeURL();
  
    // Simulación de datos
    const detallesContrato = obtenerDetallesContrato(idContrato);
  
    // Construir el HTML con los detalles
    const detallesHTML = `
      <h2>${detallesContrato.titulo}</h2>
      <p>ID Contrato: ${detallesContrato.idContrato}</p>
      <p>Tipo: ${detallesContrato.tipo}</p>
      <p>Manager: ${detallesContrato.manager}</p>
      <!-- Agrega más detalles según sea necesario -->
    `;
  
    // Agregar los detalles al contenedor
    document.getElementById('detalles').innerHTML = detallesHTML;
}

function cerrarVentana() {
    // Lógica para cerrar la ventana emergente
    window.close();
}

function obtenerIdContratoDesdeURL() {
    // Lógica para obtener el ID del contrato desde la URL
    // En este ejemplo, se devuelve un valor simulado
    return 1;
}

function obtenerDetallesContrato(idContrato) {
    // Lógica para obtener los detalles del contrato desde la base de datos o datos simulados
    // En este ejemplo, se devuelven valores simulados
    return {
      idContrato: '1',
      titulo: 'Contrato A',
      tipo: 'Tipo A',
      manager: 'Manager A',
      // Agrega más detalles según sea necesario
    };
}

// Al cargar la ventana, se cargan automáticamente los detalles del contrato
window.onload = cargarDetallesContrato;
