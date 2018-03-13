import 'stupid-table-plugin'
import flatpickr from "flatpickr"
import Service from './service'
import Feature from './feature'
import FeatureViewModel from './feature-view-model'

class App {
  constructor() {
    this.formDataOpts = [
      "clients",
      "product-area"
    ];

    this.vm = null;
    this.editing = false;
  }

  retreiveFeatures() {
    const self = this;
    //this.vm.clearFeatures();
    Service
      .getAllFeature()
      .then((data) => self.loadTableData(data));
  }

  loadTableData(data) {
    // get all feature data
    data.features.forEach(
      feature => this.vm.addNewFeature(new Feature(feature))
    );
    $("#feature-table").stupidtable();
  }

  loadFeatureFormData() {
    // get all form feature option data
    Service
      .getFormFeatureData(this.formDataOpts)
      .forEach((promise) => {
        promise.then((data) => {
          delete data.code;
          this.vm.addFormOption(data);
        });
      });
  }

  logNewFeature(e, data) {
    this.vm.clearFeatures();
    Service
      .addFeature(JSON.stringify(data))
      .then((res) => {
        console.log(res);
        //self.loadTableData(data);
      });
  }

  toggleFeatureModal(e) {
    e.preventDefault();
    console.log(this.editing);
    if (!this.editing) {
      this.editing = true;
      $("#new-feature-modal").modal('show');
    } else {
      this.editing = false;
      $("#new-feature-modal").modal('hide');
    }
  }

  initDatePicker() {
    var today = new Date();
    var year = today.getFullYear();
    var month = today.getMonth();
    var day = today.getDate()+1;
    console.log(year);
    console.log(month);
    console.log(day);
    $( "#datepicker" ).datepicker({
      minDate: new Date(year, month, day)
    });
  }

  init() {
    this.vm = new FeatureViewModel();
    ko.applyBindings(this.vm);
    console.log(this.vm);
    this.retreiveFeatures();
    this.loadFeatureFormData();
    this.initDatePicker();

    // Events
    $(".add-feature").on("click", this.toggleFeatureModal.bind(this));
    $("#new-feature-form").on("captureData", this.logNewFeature.bind(this));
  }
}

export default App;
