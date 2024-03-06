document.addEventListener('DOMContentLoaded', function () {
    // Lógica adicional si es necesario
  });
  
  function agregarCliente() {
    // Obtén los valores del formulario
    const nombre = document.getElementById('nombreCliente').value;
    const idCliente = document.getElementById('id_client').value;
    const direccion = document.getElementById('direccionCliente').value;
    const telefono = document.getElementById('telefono_cliente').value;
    const correo = document.getElementById('correo').value;
    const descripcion = document.getElementById('Descripcion').value;
  
    // Validar que los campos no estén vacíos
    if (!nombre || !idCliente || !direccion || !telefono || !correo || !descripcion) {
      alert('Por favor, completa todos los campos.');
      return;
    }
  
    // Resto del código para agregar el cliente
    // Puedes utilizar estos valores para agregar la nueva fila a la tabla, por ejemplo
    // Recuerda que esto es solo un ejemplo y deberás adaptarlo según la estructura de tu aplicación
    const nuevaFila = `<tr>
                          <td>${idCliente}</td>
                          <td>${nombre}</td>
                          <td>${direccion}</td>
                          <td>${telefono}</td>
                          <td>${correo}</td>
                          <td>${descripcion}</td>
                          <td>Trabajador A</td>
                          <td>
                            <button onclick="eliminarCliente(${idCliente})">Eliminar</button>
                            <button onclick="verCliente(${idCliente})">Ver</button>
                          </td>
                      </tr>`;
  
    // Inserta la nueva fila en la tabla (puedes ajustar esto según tu estructura)
    const tabla = document.querySelector('#clientes tbody');
    tabla.innerHTML += nuevaFila;
  
    // Cierra la ventana o realiza otras acciones según sea necesario
    cerrarVentana();
  }
  
  function cerrarVentana() {
    // Cierra la ventana o pestaña del formulario sin hacer ninguna acción
    window.close();
  }
  