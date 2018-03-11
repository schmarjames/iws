class FeatureViewModel {
  constructor() {
    this.feature_collection = ko.observableArray([]);
    this.feature_form_options = {};
  }

  addNewFeature(new_feature) {
    this.feature_collection.push(ko.observable(new_feature));
  }

  getFeatureCollection() {
    return this.feature_collection;
  }

  addFormOption(formOptions) {
    console.log(formOptions);
    this.feature_form_options = Object.assign(this.feature_form_options, formOptions);
    console.log(this.feature_form_options);

  }
}

export default FeatureViewModel;
