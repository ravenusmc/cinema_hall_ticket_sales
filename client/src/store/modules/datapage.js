import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';
import store from '@/store/index';

Vue.use(Vuex);

const data = { 
	ticketSalesByMovieGenre: [
        ['Horror',310],
        ['Action',299],
        ['Comedy',287],
        ['Drama',286],
        ['Sci-Fi',258],
    ],
};

const getters = {
	ticketSalesByMovieGenre: (state) => state.ticketSalesByMovieGenre,
};

const actions = {

	// submitSelectedYearToServer: ({ commit }, { payload }) => {
	// 	commit('setYear', payload['year'])
	// 	const path = 'http://localhost:5000/getDataForGraphs';
	// 	axios.post(path, payload)
	// 		.then((res) => {
	// 			console.log(res.data)
	// 			commit('setAverageAgaData', res.data['average_age_data'])
	// 			commit('setDeathsByGroupData', res.data['deaths_by_group_data'])
	// 			commit('setDeathsByRegionData', res.data['death_count_by_region'])
	// 			commit('setDeathsOfPeopleInEventData', res.data['took_part_in_event'])
	// 		})
	// 		.catch((error) => {
	// 			console.log(error);
	// 		});
	// },

	// submitSelectedInjuryAndYearToServer: ({commit}, { payload }) => {
	// 	commit('setYearTwo', payload['yearTwo'])
	// 	const path = 'http://localhost:5000/getDataForGraphsTwo';
	// 	axios.post(path, payload)
	// 	.then((res) => {
    //   		console.log(res.data)
	// 		if (res.data['injury_data']['Israeli Count'] === 0 && res.data['injury_data']['Palestinian Count'] === 0) {
	// 			commit('setHideInjuryGraph', true)
	// 		}else {
	// 			commit('setHideInjuryGraph', false)
	// 		}
	// 		commit('setTypeOfInjuryData', res.data['injury_data'])
	// 		commit('setTypeOfAmmoData', res.data['ammo_data'])
	// 		commit('setKilledByData', res.data['killed_by_data'])
	// 	})
	// 	.catch((error) => {
	// 		console.log(error);
	// 	});
	// },
};

const mutations = {

	setTicketSalesByMovieGenre(state, value) {
		state.ticketSalesByMovieGenre = value;
	},

};

export default {
	namespaced: true,
	state: data,
	getters,
	actions,
	mutations,
};