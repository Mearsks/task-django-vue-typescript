import { config } from 'vuex-module-decorators';
import Vue from 'vue';
import Vuex from 'vuex';


Vue.use(Vuex);
config.rawError = true;

export default new Vuex.Store({
    state: {},
    mutations: {},
    actions: {},
    modules: {}
});
