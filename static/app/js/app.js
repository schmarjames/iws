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
    this.$modal = null;
    this.$addFeatureBtn = null;
    this.$newFeatureForm = null;
    this.$loader = null;
  }

  retreiveFeatures() {
    const self = this;
    this.toggleLoader(true);
    Service
      .getAllFeature()
      .then((data) => self.loadTableData(data));
  }

  loadTableData(data) {
    // get all feature data
    if (Array.isArray(data.features)) {
      data.features.forEach(
        feature => this.vm.addNewFeature(new Feature(feature))
      );
    } else {
      this.vm.addNewFeature(new Feature(data.feature));
    }
    $("#feature-table").stupidtable();
    this.toggleLoader(false);
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
    this.toggleLoader(true);
    Service
      .addFeature(JSON.stringify(data))
      .then((res) => {
        this.loadTableData(res);
        this.$modal.trigger('hidden.bs.modal');
      });
  }

  toggleFeatureModal(e) {
    try{
      e.preventDefault();
    } catch(err) {}

    if (!this.editing) {
      this.editing = true;
      this.$modal.modal('show');
    } else if (this.editing) {
      this.editing = false;
      this.$modal.modal('hide');
    }
  }

  toggleLoader(status) {
    (status) ? this.$loader.show() : this.$loader.hide();
  }

  initDatePicker() {
    var today = new Date();
    var year = today.getFullYear();
    var month = today.getMonth();
    var day = today.getDate()+1;
    $( "#datepicker" ).datepicker({
      minDate: new Date(year, month, day)
    });
  }

  init() {
    // assign elements
    this.$addFeatureBtn = $(".add-feature");
    this.$newFeatureForm = $("#new-feature-form");
    this.$modal = $("#new-feature-modal");
    this.$loader = $("#loader");

    this.vm = new FeatureViewModel();
    ko.applyBindings(this.vm);
    this.retreiveFeatures();
    this.loadFeatureFormData();
    this.initDatePicker();

    // Events
    this.$addFeatureBtn.on("click", this.toggleFeatureModal.bind(this));
    this.$newFeatureForm.on("captureData", this.logNewFeature.bind(this));
    this.$modal.on('hidden.bs.modal', () => this.editing = false);
  }
}

export default App;
