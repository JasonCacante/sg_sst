function crearUsuario(){
    let empleado = document.getElementById('selEmpleado');
    let rol = document.getElementById('selRol');
    let id_empleado = document.getElementById('id_empleado');
    let id_rol = document.getElementById('id_rol');
    id_empleado.value = empleado.value;
    id_rol.value = rol.value;
}

function editarUsuario(fila){
    const  usuario = fila.cells[0].innerHTML;
    window.location = `${usuario}`;
}

function borrarUsuario(id){
    window.location = `${borrar/id}`;
}