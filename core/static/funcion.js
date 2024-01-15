$(document).ready(function(){
	// Activate tooltip
	$('[data-toggle="tooltip"]').tooltip();
	
	// Select/Deselect checkboxes
	var checkbox = $('table tbody input[type="checkbox"]');
	$("#selectAll").click(function(){
		if(this.checked){
			checkbox.each(function(){
				this.checked = true;                        
			});
		} else{
			checkbox.each(function(){
				this.checked = false;                        
			});
		} 
	});
	checkbox.click(function(){
		if(!this.checked){
			$("#selectAll").prop("checked", false);
		}
	});
});

function showRegistro(sw){
    var login = document.querySelector("#login");
    var regis = document.querySelector("#registro");
    login.classList.add(sw?"hide":"showLogin");
    regis.classList.add(sw?"show":"hide");
    login.classList.remove(!sw?"hide":"showLogin");
    regis.classList.remove(!sw?"show":"hide");
    return false;
}