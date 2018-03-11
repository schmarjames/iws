import Service from './service'
import Feature from './feature'
import FeatureViewModel from './feature-view-model'

class App {
  constructor() {
    this.formDataOpts = [
      "clients",
      "priorities",
      "product-area"
    ];

    this.vm = null;
  }

  loadTableData() {
    // get all feature data
    Service
      .getAllFeature()
      .then((data) => {
          data.features.forEach(
            feature => this.vm.addNewFeature(new Feature(feature))
          )
          console.log('obj ', this.vm);
        }
      );
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

  init() {
    this.vm = new FeatureViewModel();
    ko.applyBindings(this.vm);
    this.loadTableData();
    this.loadFeatureFormData();
  }
}

export default App;
