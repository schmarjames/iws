import Service from './service'

class FeatureViewModel {
  constructor() {
    this.feature_collection = ko.observableArray([]);
    this.feature_form_options = {};
    this.clients = ko.observableArray([]);
    this.priorities = ko.observableArray([]);
    this.productArea = ko.observableArray([]);

    this.formData = {
      title: ko.observable(""),
      description: ko.observable(""),
      client: ko.observable(""),
      target_date: ko.observable(""),
      priority: ko.observable(""),
      product_area: ko.observable("")
    };
  }

  addNewFeature(new_feature) {
    this.feature_collection.push(ko.observable(new_feature));
  }

  clearFeatures() {
    this.feature_collection = ko.observableArray([]);
  }

  getFeatureCollection() {
    return this.feature_collection;
  }

  addFormOption(formOptions) {
    const key = Object.keys(formOptions).shift();
    if (this.hasOwnProperty(key)) {
      formOptions[key].forEach((opt) => this[key].push(opt));
    }
  }

  submitFeature(formEl) {
    var data = {
      title: this.formData.title(),
      description: this.formData.description(),
      client_id: parseInt(this.formData.client().pop().id),
      priority: parseInt(this.formData.priority()),
      target_date: this.formData.target_date(),
      product_area_id: parseInt(this.formData.product_area().pop().id)
    };

    $("#new-feature-form").trigger("captureData", data);
  }
}

export default FeatureViewModel;
