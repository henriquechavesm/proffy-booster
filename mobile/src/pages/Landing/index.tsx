import React from "react";
import { View, Text, Image } from "react-native";
import { useNavigation } from "@react-navigation/native";
import { RectButton } from "react-native-gesture-handler";

import landingImg from "../../assets/images/landing.png";
import studyIcon from "../../assets/images/icons/study.png";
import teachIcon from "../../assets/images/icons/give-classes.png";
import heartIcon from "../../assets/images/icons/heart.png";

import styles from "./styles";

const Landing = () => {
  const { navigate } = useNavigation();

  function handleNavigateToTeachPage() {
    navigate("Teach");
    {
      /*Name on Screen component in AppStack */
    }
  }

  return (
    <View style={styles.container}>
      <Image source={landingImg} style={styles.banner} />
      <Text style={styles.title}>
        Seja bem-vindo, {"\n"}
        <Text style={styles.titleBold}>O que deseja fazer?</Text>
      </Text>

      <View style={styles.buttonsContainer}>
        <RectButton style={[styles.button, styles.buttonPrimary]}>
          <Image source={studyIcon} />
          <Text style={styles.buttonText}>Estudar</Text>
        </RectButton>

        <RectButton
          onPress={handleNavigateToTeachPage}
          style={[styles.button, styles.buttonSecondary]}
        >
          <Image source={teachIcon} />
          <Text style={styles.buttonText}>Ensinar</Text>
        </RectButton>
      </View>

      <Text style={styles.totalConnections}>
        Total de 285 conexões já realizadas <Image source={heartIcon} />
      </Text>
    </View>
  );
};

export default Landing;
