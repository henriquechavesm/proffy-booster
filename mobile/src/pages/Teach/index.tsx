import React from "react";
import { View, Text, ImageBackground } from "react-native";
import { RectButton } from "react-native-gesture-handler";
import { useNavigation } from "@react-navigation/native";

import teachBgImage from "../../assets/images/give-classes-background.png";

import styles from "./styles";

const Teach = () => {
  const { goBack } = useNavigation();

  function handleNavigateBack() {
      goBack();
  }

  return (
    <View style={styles.container}>
      <ImageBackground
        source={teachBgImage}
        style={styles.content}
        resizeMode="contain"
      >
        <Text style={styles.title}>Quer ser um Proffy?</Text>
        <Text style={styles.description}>
          Para começar, você precisa se cadastrar como professor na nossa
          plataforma web.
        </Text>
      </ImageBackground>

      <RectButton onPress={handleNavigateBack} style={styles.okButton}>
        <Text style={styles.okButtonText}>Tudo Bem</Text>
      </RectButton>
    </View>
  );
};

export default Teach;
