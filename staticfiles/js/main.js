  function showPleaseWait(waitMessage) {
      var modalLoading = '<div class="modal" id="pleaseWaitDialog" data-backdrop="static" data-keyboard="false role="dialog">\
        <div class="modal-dialog">\
              <div class="modal-content">\
                  <div class="modal-header">\
                      <h4 class="modal-title">'+ waitMessage +'</h4>\
                  </div>\
                  <div class="modal-body">\
                      <div class="progress">\
                        <div class="progress-bar progress-bar-success progress-bar-striped active" role="progressbar"\
                        aria-valuenow="100" aria-valuemin="0" aria-valuemax="100" style="width:100%; height: 40px">\
                        </div>\
                      </div>\
                  </div>\
              </div>\
          </div>\
      </div>';

      if ($("#id_nombre").val()!=="" ||typeof $("#id_nombre") == 'undefined') {
        console.log("WAITING")
        $("#waitingDiv").show()
        $("#waitingDiv").append(modalLoading);
      //$("#divBuscador").append(modalLoading);
        $("#pleaseWaitDialog").modal("show");
        }
  }

  /**
   * Hides "Please wait" overlay. See function showPleaseWait().
   */
  function hidePleaseWait() {
      $("#pleaseWaitDialog").modal("hide");
  }

  function validateForm(){
      if( $("#id_retmax").val()>=10){
        showPleaseWait()
      }
  }
