import pandas as pd
# ייבוא שתי המחלקות
from anigmas import AnigmasAnalyzer as Anigmas1
from anigmas2 import Anigmas2
import draw_gauge
import plotly
from graph_manager import Gauge_Graph_type, Spider_Graph_type   
import streamlit as st   
import texts               

class SchoolInfo:
    def __init__(self, df, anigma_name): 
        
        self.df = df
        self.anigma_name = anigma_name
        
        # בחירת המחלקה הנכונה לפי anigma_name
        self.anigmas_class = self._get_anigmas_class(anigma_name)
        
        # חישוב כל האניגמות באמצעות המחלקה שנבחרה
        self.ici = self.round_number(self.anigmas_class.ici_result(df))
        self.risc = self.round_number(self.anigmas_class.risc_result(df))
        self.future_negetive_past = self.round_number(self.anigmas_class.future_negative_past_result(df))
        self.future_positive_past = self.round_number(self.anigmas_class.future_positive_past_result(df))
        self.future_fatalic_present = self.round_number(self.anigmas_class.future_fatalistic_present_result(df))
        self.future_hedonistic_present = self.round_number(self.anigmas_class.future_hedonistic_present_result(df))
        self.future_future = self.round_number(self.anigmas_class.future_future_result(df))

        self.worst_anigma = self.return_biggest_delata_from_global_positive_wrost_anigma()[0]
        self.worst_anigma_value = self.round_number(self.return_biggest_delata_from_global_positive_wrost_anigma()[1])
        self.worst_anigma_name = texts.return_translate_anigma_name(self, self.worst_anigma)
        self.best_anigma = self.return_biggest_delata_from_global_negetive_best_anigma()[0]
        self.best_anigma_value = self.round_number(self.return_biggest_delata_from_global_negetive_best_anigma()[1])
        self.best_anigma_name = texts.return_translate_anigma_name(self, self.best_anigma)
        self.worst_heg1_text = self.return_first_and_second_worst_heg_according_to_wrost_anigma()[0]
        
        self.round_delta_as_dict = self.return_round_delta_from_global_as_dict()
        self.ici_delta_present = self.return_int_from_round_delta("ici")
        self.risc_delta_present = self.return_int_from_round_delta("risc")
        self.future_negetive_past_delta_present = self.return_int_from_round_delta("future_negetive_past")
        self.future_positive_past_delta_present = self.return_int_from_round_delta("future_positive_past")
        self.future_fatalic_present_delta_present = self.return_int_from_round_delta("future_fatalic_present")
        self.future_hedonistic_present_delta_present = self.return_int_from_round_delta("future_hedonistic_present")
        self.future_future_delta_present = self.return_int_from_round_delta("future_future")

    def _get_anigmas_class(self, anigma_name):
        """בחירת המחלקה הנכונה לפי anigma_name"""
        
        # הגדרת איזה אניגמות שייכות לכל מחלקה
        anigmas1_list = list(Anigmas1.ANIGMA_COLUMNS.keys())
        anigmas2_list = list(Anigmas2.ANIGMA_COLUMNS.keys())
        
        if anigma_name in anigmas1_list:
            return Anigmas1
        elif anigma_name in anigmas2_list:
            return Anigmas2
        else:
            # ברירת מחדל - אם האניגמה לא נמצאת, נשתמש ב-Anigmas1
            st.warning(f"Anigma '{anigma_name}' not found in either class. Using Anigmas1 as default.")
            return Anigmas1

    @classmethod
    def get_all_available_anigmas(cls):
        """מחזיר רשימה של כל האניגמות הזמינות משתי המחלקות"""
        anigmas1_list = list(Anigmas1.ANIGMA_COLUMNS.keys())
        anigmas2_list = list(Anigmas2.ANIGMA_COLUMNS.keys())
        
        return {
            "anigmas1": anigmas1_list,
            "anigmas2": anigmas2_list,
            "all": anigmas1_list + anigmas2_list
        }

    @classmethod
    def get_anigma_source(cls, anigma_name):
        """מחזיר איזו מחלקה מכילה את האניגמה הנתונה"""
        anigmas1_list = list(Anigmas1.ANIGMA_COLUMNS.keys())
        anigmas2_list = list(Anigmas2.ANIGMA_COLUMNS.keys())
        
        if anigma_name in anigmas1_list:
            return "Anigmas1"
        elif anigma_name in anigmas2_list:
            return "Anigmas2"
        else:
            return "Not Found"

    def return_exact_precent_delta(self, anigma_name):
        delta = self.round_delta_as_dict[anigma_name]
        return delta * 100

    def return_int_from_round_delta(self, anigma_name):
        delta = self.round_delta_as_dict[anigma_name]
        
        if delta >= 0.3:
            return -30
        if delta <= -0.3:
            return 30
        
        match delta:
            case 0:
                return 0
            case -0.1:
                return 10
            case -0.2:
                return 20
            case 0.1:
                return -10
            case 0.2:
                return -20
           
    def return_text_from_round_delta(self, anigma_name):
        delta = self.round_delta_as_dict.get(anigma_name)
        
        if delta is None:
            return "לא ניתן לקבוע (נתון חסר)"
            
        if delta >= 0.3:
            return "מעל הממוצע הארצי בצורה משמעותית מאוד (30%+)"
        if delta <= -0.3:
            return "מעל הממוצע הארצי בצורה משמעותית מאוד (30%+)"
        
        match delta:
            case 0:
                return "במידה שווה לממוצע הארצי"
            case -0.1:
                return "מעט מעל הממוצע הארצי (10%+)"
            case -0.2:
                return "(20%+) מעל הממוצע הארצי בצורה משמעותית"
            case 0.1:
                return "מתחתת לממוצע הארצי (10%-)"
            case 0.2:
                return "מעט מתחת לממוצע הארצי (20%-)"
             
    def round_number(self, number):
        return round(number, 1)
  
    def return_anigmas_result_as_dict(self):
        result = {
            "ici": self.ici,
            "risc": self.risc,
            "future_negetive_past": self.future_negetive_past,
            "future_positive_past": self.future_positive_past,
            "future_fatalic_present": self.future_fatalic_present,
            "future_hedonistic_present": self.future_hedonistic_present,
            "future_future": self.future_future
        }
        return result
    
    def return_delta_from_global_as_dict(self):
        result = {
            "ici": self.get_precentage_diffrent_from_global_anigmas("ici"),
            "risc": self.get_precentage_diffrent_from_global_anigmas("risc"),
            "future_negetive_past": self.get_precentage_diffrent_from_global_anigmas("future_negetive_past"),
            "future_positive_past": self.get_precentage_diffrent_from_global_anigmas("future_positive_past"),
            "future_fatalic_present": self.get_precentage_diffrent_from_global_anigmas("future_fatalic_present"),
            "future_hedonistic_present": self.get_precentage_diffrent_from_global_anigmas("future_hedonistic_present"),
            "future_future": self.get_precentage_diffrent_from_global_anigmas("future_future")
        }
        return result
  
    def return_round_delta_from_global_as_dict(self):
        delta_dict = self.return_delta_from_global_as_dict()
        rounded_delta_dict = {key: self.round_number(value) for key, value in delta_dict.items()}
        return rounded_delta_dict
  
    def return_biggest_delata_from_global_positive_wrost_anigma(self):
        delta_dict = self.return_delta_from_global_as_dict()
        positive_delta_dict = {key: value for key, value in delta_dict.items() if value > 0}

        if not positive_delta_dict:
            return ("לא נמצא", 0)
            
        max_key = max(positive_delta_dict, key=positive_delta_dict.get)
        max_value = positive_delta_dict[max_key]
        
        return max_key, max_value
    
    def return_biggest_delata_from_global_negetive_best_anigma(self):
        delta_dict = self.return_delta_from_global_as_dict()
        negetive_delta_dict = {key: value for key, value in delta_dict.items() if value < 0}
        
        if not negetive_delta_dict:
            return ("לא נמצא מדד חלש", 0)
    
        min_key = min(negetive_delta_dict, key=negetive_delta_dict.get)
        min_value = negetive_delta_dict[min_key]
        
        return min_key, min_value

    def print_anigma_result(self):
        anigma_max_abs = self.return_biggest_delata_from_global()
        self.anigmas_class.get_max_average_higed_from_anigma(self.df, anigma_max_abs)

    def get_fig_ici(self, name):
        graph = Gauge_Graph_type("ici", name, self.ici)
        fig = graph.get_fig()
        return fig

    def get_fig_risc(self, name):
        graph = Gauge_Graph_type("risc", name, self.risc)
        fig = graph.get_fig()
        return fig
  
    def get_fig_spider(self, mobile=False):
        graph = Spider_Graph_type("spider", self.return_anigmas_result_as_dict())
        if mobile:
            fig = graph.get_fig_mobile()
        else:
            fig = graph.get_fig()
        return fig
  
    def get_precentage_diffrent_from_global_anigmas(self, anigma_name):
        global_anigmas = st.session_state.global_average
        
        local = self.return_anigmas_result_as_dict()[anigma_name]
        global_ = global_anigmas[anigma_name]
        
        delta = (global_ - local) / global_
        
        return delta
        
    def return_worst_heg_according_to_wrost_anigma(self):
        worst_heg = self.anigmas_class.return_worst_heg_from_anigma_according_to_delta_from_global(self.df, self.worst_anigma) 
        return worst_heg

    def return_first_and_second_worst_heg_according_to_wrost_anigma(self):
        key1, value1, key2, value2 = self.anigmas_class.return_first_and_second_heg_for_worst_heg(self.df, self.worst_anigma)
        key1_name = texts.return_translate_heg_name(key1)
        key2_name = texts.return_translate_heg_name(key2) 
        
        return key1_name, value1, key2_name, value2