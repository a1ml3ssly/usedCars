package gui;

import java.awt.event.*;
import java.awt.*;
import java.awt.image.BufferedImage;
import javax.imageio.ImageIO;
import javax.swing.*;
import java.awt.*;
import java.awt.image.*;
import java.io.*;
import javax.swing.*;
import javax.imageio.ImageIO;

public class Gui extends JFrame {
    // JFrame
    static JFrame f;

    // JButton
    static JButton b, b1, b2;

    // label to display text
    static JLabel l;

    // main class
    public static void main(String[] args) {
        // create a new frame to store text field and button
        f = new JFrame("המכונאי השמן");
        // create a label to display text
        BufferedImage image = null;
        try {
            image = ImageIO.read(new File("./erez logo.jpg"));
        } catch (IOException e) {
            e.printStackTrace();
        }
        l = new JLabel(new ImageIcon(image));
        l.setSize(100, 100);

        // create a new buttons
        b = new JButton("button1");
        b1 = new JButton("button2");
        b2 = new JButton("button3");
        //f.setLayout(null);
        f.add(b);
        JPanel p = new JPanel();
        p.setBackground(Color.black);
        p.add(b);
        f.add(p);
        // create a panel to add buttons
//        JPanel p = new JPanel(new GridBagLayout());
//
//        GridBagConstraints constraints = new GridBagConstraints();
//        //constraints.anchor = GridBagConstraints.LINE_START;
//
//
//        GridBagConstraints titleConstraints = new GridBagConstraints();
//        //titleConstraints.anchor = GridBagConstraints.PAGE_START;
//        titleConstraints.gridwidth = GridBagConstraints.RELATIVE;
//        titleConstraints.gridx = 0;
//        titleConstraints.gridy = 0;
//        titleConstraints.gridwidth=3;
//
////        constraints.insets = new Insets(10, 10, 10, 10);
//
//        // add buttons and textfield to panel
//        //
//        constraints.fill = GridBagConstraints.HORIZONTAL;
//        constraints.gridx = 0;
//        constraints.gridy = 1;
//        p.add(b, constraints);
//        //constraints.fill = GridBagConstraints.HORIZONTAL;
//        constraints.gridx = 1;
//        constraints.gridy = 1;
//        p.add(b1, constraints);
//        //constraints.fill = GridBagConstraints.HORIZONTAL;
//        constraints.gridx = 2;
//        constraints.gridy = 1;
//        p.add(b2, constraints);
//
//
//        // setbackground of panel
//        p.setBackground(Color.white);
//
//        // add panel to frame
//        f.add(p);

        // set the size of frame
        f.setSize(1280, 720);//size of the scree
        f.setLocationRelativeTo(null);//centers the screen
        f.setVisible(true);
        System.out.println("Test1");

 //       p.add(l, titleConstraints);
    }
}
