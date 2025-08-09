import pandas as pd
import actions
import streamlit as st
from abc import ABC, abstractmethod

class AbstractAnigmas(ABC):
    """מחלקה אבסטרקטית לניתוח אניגמות"""
    
   

    @staticmethod
    @abstractmethod
    def cut_df_from_dictionary(data_dict, anigma_name):
        """חיתוך Dictionary לפי אניגמה מסוימת"""
        pass

    @staticmethod
    @abstractmethod
    def get_percentage_delta(global_value, local_value):
        """חישוב אחוז הדלתא בין ערכים גלובליים ומקומיים"""
        pass


    @staticmethod
    @abstractmethod
    def return_biggest_delta_from_global(local_dict, global_dict):
        """מחזיר את המפתח והערך עם הדלתא הגדולה ביותר"""
        pass

    @staticmethod
    @abstractmethod
    def return_second_biggest_delta_from_global(local_dict, global_dict, biggest_key):
        """מחזיר את הדלתא השנייה בגודלה"""
        pass

    @staticmethod
    @abstractmethod
    def return_worst_heg_from_anigma_according_to_delta_from_global(df, anigma_name):
        """מחזיר את ה-HEG הגרוע ביותר מאניגמה לפי דלתא מגלובלי"""
        pass

    @staticmethod
    @abstractmethod
    def return_first_and_second_heg_for_worst_heg(df, anigma_name):
        """מחזיר את שני ה-HEG הגרועים ביותר לאניגמה"""
        pass

    @staticmethod
    @abstractmethod
    def get_max_average_higed_from_anigma(df, anigma_name):
        """מחזיר את הממוצע המקסימלי מאניגמה"""
        pass

    @staticmethod
    @abstractmethod
    def get_global_heg_avg_as_dict(df):
        """מחזיר ממוצע גלובלי של כל עמודות ה-HEG כ-Dictionary"""
        pass

    @staticmethod
    @abstractmethod
    def ici_result(df):
        """תוצאת ICI"""
        pass

    @staticmethod
    @abstractmethod
    def risc_result(df):
        """תוצאת RISC"""
        pass

    @staticmethod
    @abstractmethod
    def future_negative_past_result(df):
        """תוצאת Future Negative Past"""
        pass

    @staticmethod
    @abstractmethod
    def future_positive_past_result(df):
        """תוצאת Future Positive Past"""
        pass

    @staticmethod
    @abstractmethod
    def future_fatalistic_present_result(df):
        """תוצאת Future Fatalistic Present"""
        pass

    @staticmethod
    @abstractmethod
    def future_hedonistic_present_result(df):
        """תוצאת Future Hedonistic Present"""
        pass

    @staticmethod
    @abstractmethod
    def future_future_result(df):
        """תוצאת Future Future"""
        pass

   
    
    # @abstractmethod
    # def get_all_anigma_results(cls, df):
    #     """מחזיר תוצאות של כל האניגמות"""
    #     pass
    
    
    # @abstractmethod
    # def get_available_anigmas(cls):
    #     """מחזיר רשימת כל האניגמות הזמינות"""
    #     pass
    
    
    # @abstractmethod
    # def print_anigma_info(cls):
    #     """מדפיס מידע על כל האניגמות"""
    #     pass
    
# מחלקה לניתוח אניגמות, יורשת מהמחלקה האבסטרקטית
class Anigmas1(AbstractAnigmas):
    """מחלקה לניתוח אניגמות"""
    
    # קבועים של העמודות לכל אניגמה
    ANIGMA_COLUMNS = {
        "ici": ('heg_1', 'heg_5', 'heg_10', 'heg_12', 'heg_24', 'heg_26'),
        "risc": ("heg_4", "heg_14", "heg_18", "heg_19"),
        "future_negetive_past": ('heg_2', 'heg_13', 'heg_23'),
        "future_positive_past": ('heg_6', 'heg_16', 'heg_21'),
        "future_fatalic_present": ('heg_3', 'heg_15', 'heg_22'),
        "future_hedonistic_present": ('heg_11', 'heg_17', 'heg_25'),
        "future_future": ('heg_7', 'heg_8', 'heg_9', 'heg_27')
    }
    
    @staticmethod
    def cut_df(df, anigma_name):
        match anigma_name:
            case "ici":
                cols=('heg_1','heg_5','heg_10','heg_12','heg_24','heg_26')
            case "risc":
                cols=("heg_4","heg_14","heg_18","heg_19")
            case "future_negetive_past":
                cols=('heg_2','heg_13','heg_23')
            case "future_positive_past":
                cols=('heg_6','heg_16','heg_21')
            case "future_fatalic_present":
                cols=('heg_3','heg_15','heg_22')
            case "future_hedonistic_present":
                cols=('heg_11','heg_17','heg_25')
            case "future_future":
                cols=('heg_7','heg_8','heg_9','heg_27')
            case _:
                print("anigma name not found")
            
        df_cuted = df.filter(items=cols)
        return df_cuted

    @staticmethod
    def cut_df_from_dictionary(dict,anigma_name):
        match anigma_name:
            case "ici":
                cols=('heg_1','heg_5','heg_10','heg_12','heg_24','heg_26')
            case "risc":
                cols=("heg_4","heg_14","heg_18","heg_19")
            case "future_negetive_past":
                cols=('heg_2','heg_13','heg_23')
            case "future_positive_past":
                cols=('heg_6','heg_16','heg_21')
            case "future_fatalic_present":
                cols=('heg_3','heg_15','heg_22')
            case "future_hedonistic_present":
                cols=('heg_11','heg_17','heg_25')
            case "future_future":
                cols=('heg_7','heg_8','heg_9','heg_27')
            case _:
                print("anigma name not found")
                
        dict_cuted = {k: dict[k] for k in cols}
        return dict_cuted

    @staticmethod
    def return_wrost_heg_from_anigma_acoording_to_delta_from_global(df,anigma_name):
        current_df_cuted=Anigmas1.cut_df(df,anigma_name)
        current_mean = current_df_cuted.mean()
        current_mean_dict = current_mean.to_dict()

        global_mean_dict=Anigmas1.cut_df_from_dictionary(st.session_state.heg_avg,anigma_name)

        key=return_biggest_delta_from_global(current_mean_dict,global_mean_dict)[0]
        value=return_biggest_delta_from_global(current_mean_dict,global_mean_dict)[1]
    
        return_second_biggest_delta_from_global(current_mean_dict,global_mean_dict,key)
    

    
    
    @staticmethod
    def get_precentage_delta(global_,local):
        
        delta=(global_-local)/global_
        return delta

    @staticmethod        
    def return_biggest_delta_from_global(local_dict,global_dict):
        delta_dict={}
        for key in local_dict.keys():
            delta=get_precentage_delta(global_dict[key],local_dict[key])
            delta_dict[key]=delta
        
        #finds the max key from the delta dict
        max_key = max(delta_dict, key=delta_dict.get)
        max_value = delta_dict[max_key]
        
      
        return max_key,max_value

    @staticmethod
    def return_second_biggest_delta_from_global(local_dict,global_dict,biggest_key):
        delta_dict={}
        for key in local_dict.keys():
            if key != biggest_key:
                delta=get_precentage_delta(global_dict[key],local_dict[key])
                delta_dict[key]=delta
        
        #finds the max key from the delta dict
        max_key = max(delta_dict, key=delta_dict.get)
        max_value = delta_dict[max_key]
        
        return max_key,max_value
        
    @staticmethod       
    def return_first_and_second_heg_for_worst_heg(df,anigma_name):
        current_df_cuted=Anigmas1.cut_df(df,anigma_name)
        current_mean = current_df_cuted.mean()
        current_mean_dict = current_mean.to_dict()

        global_mean_dict=Anigmas1.cut_df_from_dictionary(st.session_state.heg_avg,anigma_name)

        key=return_biggest_delta_from_global(current_mean_dict,global_mean_dict)[0]
        value=return_biggest_delta_from_global(current_mean_dict,global_mean_dict)[1]
    
        key2,value2=return_second_biggest_delta_from_global(current_mean_dict,global_mean_dict,key)
    
        return key,value,key2,value2
    
    
    
    
    
    
    @staticmethod
    def get_max_average_higed_from_anigma(df,anigma_name):
        df_cuted=Anigmas1.cut_df(df,anigma_name)
        result=actions.return_sum_dict(df_cuted)
    # st.write(f"chosen anigma:{anigma_name}")
    # st.write(result)
        st.dataframe(df)
        return result


            
             
    @staticmethod
    def ici_result(df):
        ici_cols=('heg_1','heg_5','heg_10','heg_12','heg_24','heg_26')
        df_ici = df.filter(items=ici_cols)
        return actions.return_mean_from_df(df_ici)

    @staticmethod
    def risc_result(df):
        risc_cols=("heg_4","heg_14","heg_18","heg_19")
        df_risc=df.filter(items=risc_cols)
        return actions.return_mean_from_df(df_risc)

    @staticmethod
    def future_negetive_past_result(df):
        future_negetive_past_cols=('heg_2','heg_13','heg_23')
        df_future_negetive_past=df.filter(items=future_negetive_past_cols)
        return actions.return_mean_from_df(df_future_negetive_past)

    @staticmethod
    def future_positive_past_result(df):
        future_positive_past_cols=('heg_6','heg_16','heg_21')
        df_future_positive_past=df.filter(items=future_positive_past_cols)
        return actions.return_mean_from_df(df_future_positive_past)

    @staticmethod
    def future_fatalic_present_result(df):
        future_fatalic_present_cols=('heg_3','heg_15','heg_22')
        df_future_fatalic_present=df.filter(items=future_fatalic_present_cols)
        return actions.return_mean_from_df(df_future_fatalic_present)

    @staticmethod
    def future_hedonistic_present_result(df):
        future_hedonistic_present_cols=('heg_11','heg_17','heg_25')
        df_future_hedonistic_present=df.filter(items=future_hedonistic_present_cols)
        return actions.return_mean_from_df(df_future_hedonistic_present)

    @staticmethod
    def future_future_result(df):
        future_future_cols=('heg_7','heg_8','heg_9','heg_27')
        df_future_future=df.filter(items=future_future_cols)
        return actions.return_mean_from_df(df_future_future)
    

    @staticmethod
    def get_global_heg_avg_as_dict(df):
        cols=('heg_1','heg_2','heg_3','heg_4','heg_5','heg_6','heg_7','heg_8','heg_9',
                'heg_10','heg_11','heg_12','heg_13','heg_14','heg_15','heg_16',
                'heg_17','heg_18','heg_19','heg_21','heg_22','heg_23','heg_24',
                'heg_25','heg_26','heg_27')
        df_heg = df.filter(items=cols)
    #יוצר שורה חדשה עם ממוצע של כל עמודה 
        df_heg.loc['average'] = df_heg.mean() 
    #מעביר את שורת הממוצע לdictonary
        heg_dict = df_heg.loc['average'].to_dict()
    
        return heg_dict



###### Anigmas2

class Anigmas2(AbstractAnigmas):
    """מחלקה לניתוח אניגמות"""
    
    # קבועים של העמודות לכל אניגמה
    ANIGMA_COLUMNS = {
        "ici": ('heg_3', 'heg_7', 'heg_10', 'heg_12', 'heg_20'),
        "risc": ("heg_1", "heg_5", "heg_13", "heg_16", "heg_19"),
        "future_negetive_past": ('heg_6', 'heg_15'),
        "future_positive_past": ('heg_11', 'heg_17'),
        "future_fatalic_present": ('heg_8', 'heg_18'),
        "future_hedonistic_present": ('heg_2', 'heg_9'),
        "future_future": ('heg_4', 'heg_14')
    }
    
    @staticmethod
    def cut_df( df, anigma_name):
        match anigma_name:
            case "ici":
                cols=('heg_3', 'heg_7', 'heg_10', 'heg_12', 'heg_20')
            case "risc":
                cols=("heg_1", "heg_5", "heg_13", "heg_16", "heg_19")
            case "future_negetive_past":
                cols=('heg_6','heg_15')
            case "future_positive_past":
                cols=('heg_11','heg_17')
            case "future_fatalic_present":
                cols=('heg_8', 'heg_18')
            case "future_hedonistic_present":
                cols=('heg_2', 'heg_9'),
            case "future_future":
                cols=('heg_4', 'heg_14')
            case _:
                print("anigma name not found")
            
        df_cuted = df.filter(items=cols)
        return df_cuted

    @staticmethod
    def cut_df_from_dictionary(dict,anigma_name):
        match anigma_name:
            case "ici":
                cols=('heg_3', 'heg_7', 'heg_10', 'heg_12', 'heg_20')
            case "risc":
                cols=("heg_1", "heg_5", "heg_13", "heg_16", "heg_19")
            case "future_negetive_past":
                cols=('heg_6','heg_15')
            case "future_positive_past":
                cols=('heg_11','heg_17')
            case "future_fatalic_present":
                cols=('heg_8', 'heg_18')
            case "future_hedonistic_present":
                cols=('heg_2', 'heg_9'),
            case "future_future":
                cols=('heg_4', 'heg_14')
            case _:
                print("anigma name not found")
                
        dict_cuted = {k: dict[k] for k in cols}
        return dict_cuted

    @staticmethod
    def return_worst_heg_from_anigma_according_to_delta_from_global(df,anigma_name):
        current_df_cuted=Anigmas2.cut_df(df,anigma_name)
        current_mean = current_df_cuted.mean()
        current_mean_dict = current_mean.to_dict()

        global_mean_dict=Anigmas2.cut_df_from_dictionary(st.session_state.heg_avg,anigma_name)

        key=return_biggest_delta_from_global(current_mean_dict,global_mean_dict)[0]
        value=return_biggest_delta_from_global(current_mean_dict,global_mean_dict)[1]
    
        return_second_biggest_delta_from_global(current_mean_dict,global_mean_dict,key)
    
    # st.write(f"chosen anigma:{anigma_name}")
    # st.write(f"current mean: {current_mean_dict}")
    # st.write(f"global mean: {global_mean_dict}")
    
    

    @staticmethod
    def get_precentage_delta(global_,local):
        
        delta=(global_-local)/global_
        return delta

    @staticmethod
    def return_biggest_delta_from_global(local_dict,global_dict):
        delta_dict={}
        for key in local_dict.keys():
            delta=Anigmas2.get_precentage_delta(global_dict[key],local_dict[key])
            delta_dict[key]=delta
        
        #finds the max key from the delta dict
        max_key = max(delta_dict, key=delta_dict.get)
        max_value = delta_dict[max_key]
        
        
        return max_key,max_value

    @staticmethod
    def return_second_biggest_delta_from_global(local_dict,global_dict,biggest_key):
        delta_dict={}
        for key in local_dict.keys():
            if key != biggest_key:
                delta=Anigmas2.get_precentage_delta(global_dict[key],local_dict[key])
                delta_dict[key]=delta
        
        #finds the max key from the delta dict
        max_key = max(delta_dict, key=delta_dict.get)
        max_value = delta_dict[max_key]
        
        return max_key,max_value


    @staticmethod
    def return_first_and_second_heg_for_worst_heg(df,anigma_name):
        current_df_cuted=Anigmas2.cut_df(df,anigma_name)
        current_mean = current_df_cuted.mean()
        current_mean_dict = current_mean.to_dict()

        global_mean_dict=Anigmas2.cut_df_from_dictionary(st.session_state.heg_avg,anigma_name)

        key=return_biggest_delta_from_global(current_mean_dict,global_mean_dict)[0]
        value=return_biggest_delta_from_global(current_mean_dict,global_mean_dict)[1]
    
        key2,value2=return_second_biggest_delta_from_global(current_mean_dict,global_mean_dict,key)
    
    # st.write(f"chosen anigma:{anigma_name}")
    # st.write(f"current mean: {current_mean_dict}")
    # st.write(f"global mean: {global_mean_dict}")
    
    # st.write(f"worst heg: {key} with value: {value}")
    # st.write(f"second worst heg: {key2} with value: {value2}")
    
        return key,value,key2,value2
    
    
    
    
    
    
    @staticmethod
    def get_max_average_higed_from_anigma(df,anigma_name):
        df_cuted=Anigmas2.cut_df(df,anigma_name)
        result=actions.return_sum_dict(df_cuted)
    # st.write(f"chosen anigma:{anigma_name}")
    # st.write(result)
        st.dataframe(df)
        return result


    @staticmethod
    def ici_result(df):
        ici_cols=('heg_3', 'heg_7', 'heg_10', 'heg_12', 'heg_20')
        df_ici = df.filter(items=ici_cols)
        return actions.return_mean_from_df(df_ici)

    @staticmethod
    def risc_result(df):
        risc_cols=("heg_1", "heg_5", "heg_13", "heg_16", "heg_19")
        df_risc=df.filter(items=risc_cols)
        return actions.return_mean_from_df(df_risc)

    def future_negetive_past_result(df):
        future_negetive_past_cols=('heg_6','heg_15')
        df_future_negetive_past=df.filter(items=future_negetive_past_cols)
        return actions.return_mean_from_df(df_future_negetive_past)

    @staticmethod
    def future_positive_past_result(df):
        future_positive_past_cols=('heg_11', 'heg_17')
        df_future_positive_past=df.filter(items=future_positive_past_cols)
        return actions.return_mean_from_df(df_future_positive_past)

    @staticmethod
    def future_fatalic_present_result(df):
        future_fatalic_present_cols=('heg_8', 'heg_18')
        df_future_fatalic_present=df.filter(items=future_fatalic_present_cols)
        return actions.return_mean_from_df(df_future_fatalic_present)

    @staticmethod
    def future_hedonistic_present_result(df):
        future_hedonistic_present_cols=('heg_2', 'heg_9')
        df_future_hedonistic_present=df.filter(items=future_hedonistic_present_cols)
        return actions.return_mean_from_df(df_future_hedonistic_present)

    @staticmethod
    def future_future_result(df):
        future_future_cols=('heg_4', 'heg_14')
        df_future_future=df.filter(items=future_future_cols)
        return actions.return_mean_from_df(df_future_future)
    
    @staticmethod
    def get_global_heg_avg_as_dict(df):
        cols=('heg_1','heg_2','heg_3','heg_4','heg_5','heg_6','heg_7','heg_8','heg_9',
                'heg_10','heg_11','heg_12','heg_13','heg_14','heg_15','heg_16',
                'heg_17','heg_18','heg_19','heg_21','heg_22','heg_23','heg_24',
                'heg_25','heg_26','heg_27')
        df_heg = df.filter(items=cols)
    #יוצר שורה חדשה עם ממוצע של כל עמודה 
        df_heg.loc['average'] = df_heg.mean() 
    #מעביר את שורת הממוצע לdictonary
        heg_dict = df_heg.loc['average'].to_dict()
    
        return heg_dict
