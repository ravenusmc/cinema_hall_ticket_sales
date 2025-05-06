import Vue from 'vue';
import Vuex from 'vuex';
// import axios from 'axios';
// import store from '@/store/index';

Vue.use(Vuex);

const data = { 
	ticketSalesByMovieGenre: [
        ['Horror',310],
        ['Action',299],
        ['Comedy',287],
        ['Drama',286],
        ['Sci-Fi',258],
    ],
	ageRangeData: [
		['10-20',100],
		['20-30',338],
		['31-40',329],
		['41-50',338],
		['51-60',335],
	],
	repeatCustomersData: [
		['Yes', 707], 
		['No', 733],
	],
	seatPreferanceData: [
		['Genre', 'Standard', 'VIP', 'Premium'], 
		['Comedy', 91, 103, 93], 
		['Drama', 102, 89, 95], 
		['Horror', 92, 108, 99], 
		['Action', 100, 104, 106], 
		['Sci-Fi', 90, 90, 78]], 
	ticketPriceSeatPrice: [
		{'seat_type': 'Premium', 'min': 10.01, 'q1': 13.815000000000001, 'median': 17.37, 'q3': 21.435000000000002, 'max': 24.99}, 
		{'seat_type': 'Standard', 'min': 10.03, 'q1': 13.475000000000001, 'median': 16.67, 'q3': 21.26, 'max': 24.97}, 
		{'seat_type': 'VIP', 'min': 10.03, 'q1': 13.585, 'median': 17.655, 'q3': 21.4175, 'max': 24.98}
	],
};

const getters = {
	ticketSalesByMovieGenre: (state) => state.ticketSalesByMovieGenre,
	ageRangeData: (state) => state.ageRangeData,
	repeatCustomersData: (state) => state.repeatCustomersData,
	seatPreferanceData: (state) => state.seatPreferanceData,
	ticketPriceSeatPrice: (state) => state.ticketPriceSeatPrice,
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
};

const mutations = {

	setTicketSalesByMovieGenre(state, value) {
		state.ticketSalesByMovieGenre = value;
	},

	setAgeRangeData(state, value) {
		state.ageRangeData = value;
	},

	setRepeatCustomersData(state, value) {
		state.repeatCustomersData = value;
	},

	setSeatPreferanceData(state, value) {
		state.seatPreferanceData = value;
	}

};

export default {
	namespaced: true,
	state: data,
	getters,
	actions,
	mutations,
};