/* ===================================== */
/* AJAX MODAL EDITAR/EXCLUÍR (Registro) */
/* =================================== */
function editarRegistro(id) {
	
	$.ajax({
		url: "Views/editar.cgi",
		type:'GET',
		data:{id:id},
		beforeSend:function(){
			$('#ModalRegistro').find('.modal-body').html('<center><img src="Views/unnamed.gif"></center>');
			$('#ModalRegistro').modal('show');
		},
		success:function(html){
			$('#ModalRegistro').find('.modal-body').html(html);

			$('#ModalRegistro').modal('show');
		}
	});
}